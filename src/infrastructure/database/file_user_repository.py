from features.user_management.shared.user_repository import UserRepository
from features.user_management.shared.user import User
import aiofiles
from pathlib import Path

class FileUserRepository(UserRepository):
    
    def __init__(self, file_path: str):
        self.file_path = file_path
        file_db = Path(file_path)
        file_db.touch(exist_ok=True)
        

    async def save(self, user : User):
        """Save user into file

        Args:
            user (User): The user instance to save.
        """
        async with aiofiles.open(self.file_path, 'a') as f:
            await f.write(f"{user.username},{user.email},{user.password}\n")

    async def get_user_by_username(self, username: str) -> User|None:
        """Search user by username

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User|None: The user instance with the specified username, or None if not found.
        """
        
        async with aiofiles.open(self.file_path, 'r') as f:
            async for line in f:
                user_data = line.strip().split(',')
                if user_data[0] == username:
                    return User(username=user_data[0], email=user_data[1], password=user_data[2])
        return None

    async def get_user_by_email(self, email: str) -> User|None:
        """Search user by email

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User|None: The user instance with the specified email, or None if not found.
        """
        async with aiofiles.open(self.file_path, 'r') as f:
            async for line in f:
                user_data = line.strip().split(',')
                if user_data[1] == email:
                    return User(username=user_data[0], email=user_data[1], password=user_data[2])
        return None