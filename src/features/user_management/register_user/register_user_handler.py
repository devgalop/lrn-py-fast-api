from features.user_management.shared.user import User

from .register_user_request import RegisterUserRequest
from ..shared.user_repository import UserRepository
from ..shared.password_hasher import PasswordHasher

class RegisterUserHandler:
    
    def __init__(self, 
                 user_repository: UserRepository,
                 password_hasher: PasswordHasher):
        self.user_repository = user_repository
        self.password_hasher = password_hasher
    
    async def handle(self, request: RegisterUserRequest) -> dict[str, str]:
        """Register a user into database

        Args:
            request (RegisterUserRequest): The request object containing user registration details.

        Returns:
            dict: A dictionary containing a success message.
        """
        user_found = await self.user_repository.get_user_by_username(request.username)
        if user_found:
            return {"status": "400", "message": f"User {request.username} already exists"}
        
        user_found = await self.user_repository.get_user_by_email(request.email)
        if user_found:
            return {"status": "400", "message": f"Email {request.email} is already registered"}
        
        hashed_password = self.password_hasher.hash_password(request.password)
        user = User(username=request.username, email=request.email, password=hashed_password)
        await self.user_repository.save(user)
        return {"status": "200", "message": f"User {request.username} registered successfully"}