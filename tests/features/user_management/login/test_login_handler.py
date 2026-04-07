from unittest.mock import Mock, AsyncMock
import pytest

@pytest.mark.asyncio
async def test_when_credentials_are_valid_should_login_user():
    from features.user_management.login.login_handler import LoginHandler
    from features.user_management.login.login_request import LoginRequest
    from features.user_management.shared.token_generator import TokenResponse
    from features.user_management.shared.user import User
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    token_generator = Mock()
    
    user_repository.get_user_by_username.return_value = User(username="valid_user", email="valid_user@example.com", password="hashed_password")
    
    password_hasher.verify_password.return_value = True
    
    token_generator.generate_token.return_value = TokenResponse(
        token="valid_token")
    
    handler = LoginHandler(user_repository, password_hasher, token_generator)
    await handler.handle(LoginRequest(
        username="valid_user",
        password="Password123*"
    ))
    
    user_repository.get_user_by_username.assert_called_once_with("valid_user")
    password_hasher.verify_password.assert_called_once_with("Password123*", "hashed_password")
    token_generator.generate_token.assert_called_once()
    
@pytest.mark.asyncio
async def test_when_user_does_not_exist_should_return_error():
    from features.user_management.login.login_handler import LoginHandler
    from features.user_management.login.login_request import LoginRequest
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    token_generator = Mock()
    
    user_repository.get_user_by_username.return_value = None
    
    handler = LoginHandler(user_repository, password_hasher, token_generator)
    with pytest.raises(ValueError, match= "Invalid username or password"):
        await handler.handle(LoginRequest(
            username="nonexistent_user",
            password="Password123*"
        ))
    
    user_repository.get_user_by_username.assert_called_once_with("nonexistent_user")
    password_hasher.verify_password.assert_not_called()
    token_generator.generate_token.assert_not_called()
    
@pytest.mark.asyncio
async def test_when_password_is_incorrect_should_return_error():
    from features.user_management.login.login_handler import LoginHandler
    from features.user_management.login.login_request import LoginRequest
    from features.user_management.shared.user import User
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    token_generator = Mock()
    
    user_repository.get_user_by_username.return_value = User(username="valid_user", email="valid_user@example.com", password="hashed_password")
    password_hasher.verify_password.return_value = False

    handler = LoginHandler(user_repository, password_hasher, token_generator)
    with pytest.raises(ValueError, match="Invalid username or password"):
        await handler.handle(LoginRequest(
            username="valid_user",
            password="WrongPassword123*"
        ))
    
    user_repository.get_user_by_username.assert_called_once_with("valid_user")
    password_hasher.verify_password.assert_called_once_with("WrongPassword123*", "hashed_password")
    token_generator.generate_token.assert_not_called()
