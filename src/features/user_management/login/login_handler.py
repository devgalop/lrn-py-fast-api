from features.user_management.shared.user_repository import UserRepository
from features.user_management.shared.password_hasher import PasswordHasher
from features.user_management.shared.token_generator import TokenGenerator, TokenPayload, TokenResponse
from .login_request import LoginRequest

class LoginHandler:
    def __init__(self,
                 user_repository: UserRepository,
                 password_hasher: PasswordHasher,
                 token_generator: TokenGenerator):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
        self.token_generator = token_generator
        
    async def handle(self, login_request: LoginRequest) -> TokenResponse:
        """Handles the login process for a user.
        Args:
            login_request (LoginRequest): The request object containing username and password.
        Returns:
            TokenResponse: A response object containing the generated JWT token.
        """
        user = await self.user_repository.get_user_by_username(login_request.username)
        if not user:
            raise ValueError("Invalid username or password")
        
        if not self.password_hasher.verify_password(login_request.password, user.password):
            raise ValueError("Invalid username or password")
        
        token_payload = TokenPayload(
            user_id=user.email,
            username=user.username,
            roles=["default"],
            expiration_minutes=5
        )
        return self.token_generator.generate_token(token_payload)

    