from abc import ABC, abstractmethod

class TokenPayload:
    def __init__(self, 
                 user_id: str, 
                 username: str, 
                 roles: list[str],
                 expiration_minutes: int):
        self.user_id = user_id
        self.username = username
        self.roles = roles
        self.expiration_minutes = expiration_minutes
        
class TokenResponse:
    def __init__(self, token: str):
        self.token = token

class TokenGenerator(ABC):
    @abstractmethod
    def generate_token(self, payload: TokenPayload) -> TokenResponse:
        pass