import os
import jwt
from datetime import datetime, timedelta, timezone 
from dotenv import load_dotenv

from features.user_management.shared.token_generator import TokenGenerator, TokenPayload, TokenResponse
load_dotenv()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")

class TokenBody:
    def __init__(self, user_id: str, username: str, roles: list[str], exp: datetime):
        self.user_id = user_id
        self.username = username
        self.roles = roles
        self.exp = exp

class JwtTokenGenerator(TokenGenerator):
    def generate_token(self, payload: TokenPayload) -> TokenResponse:
        """Generates a JWT token based on the provided payload.

        Args:
            payload (TokenPayload): The payload containing user information and token expiration.

        Returns:
            TokenResponse: A JWT token wrapped in a TokenResponse object.
        """
        expiration_time = datetime.now(tz=timezone.utc) + timedelta(minutes=payload.expiration_minutes)
        token_payload = TokenBody(
            user_id=payload.user_id,
            username=payload.username,
            roles=payload.roles,
            exp=expiration_time
        ).__dict__
        return TokenResponse(token=jwt.encode(token_payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM))
    