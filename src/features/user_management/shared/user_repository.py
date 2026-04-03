from abc import ABC, abstractmethod
from .user import User

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User):
        """Save user into database

        Args:
            user (User): The user instance to save.
        """
        pass

    @abstractmethod
    async def get_user_by_username(self, username: str) -> User|None:
        """Get user by username

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The user instance with the specified username, or None if not found.
        """
        pass

    @abstractmethod
    async def get_user_by_email(self, email: str) -> User|None:
        """Get user by email

        Args:
            email (str): The email of the user to retrieve.

        Returns:
            User: The user instance with the specified email, or None if not found.
        """
        pass