from typing import Annotated
from fastapi import Depends

from infrastructure.database.file_user_repository import FileUserRepository
from infrastructure.security.bcrypt_password_hasher import BcryptPasswordHasher
from infrastructure.security.jwt_token_generator import JwtTokenGenerator
from .user_repository import UserRepository
from .password_hasher import PasswordHasher
from .token_generator import TokenGenerator
from ..register_user.register_user_handler import RegisterUserHandler
from ..login.login_handler import LoginHandler


def get_user_repository() -> UserRepository:
    return FileUserRepository(file_path="users.csv")


def get_password_hasher() -> PasswordHasher:
    return BcryptPasswordHasher()

def get_token_generator() -> TokenGenerator:
    return JwtTokenGenerator()


def get_register_user_handler(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    password_hasher: Annotated[PasswordHasher, Depends(get_password_hasher)],
) -> RegisterUserHandler:
    return RegisterUserHandler(user_repository, password_hasher)

def get_login_handler(
    user_repository: Annotated[UserRepository, Depends(get_user_repository)],
    password_hasher: Annotated[PasswordHasher, Depends(get_password_hasher)],
    token_generator: Annotated[TokenGenerator, Depends(get_token_generator)]
) -> LoginHandler:
    return LoginHandler(user_repository, password_hasher, token_generator)
