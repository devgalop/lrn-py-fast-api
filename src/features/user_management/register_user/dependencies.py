from typing import Annotated
from fastapi import Depends

from infrastructure.database.file_user_repository import FileUserRepository
from infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher
from features.user_management.shared.user_repository import UserRepository
from features.user_management.shared.password_hasher import PasswordHasher
from .register_user_handler import RegisterUserHandler


def get_user_repository() -> UserRepository:
    return FileUserRepository(file_path="users.csv")


def get_password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()


def get_register_user_handler(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    password_hasher: Annotated[PasswordHasher, Depends(get_password_hasher)],
) -> RegisterUserHandler:
    return RegisterUserHandler(user_repository, password_hasher)
