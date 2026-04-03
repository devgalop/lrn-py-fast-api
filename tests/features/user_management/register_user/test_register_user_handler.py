from unittest.mock import Mock, AsyncMock
import pytest

@pytest.mark.asyncio
async def test_when_user_is_valid_should_register_user():
    from features.user_management.register_user.register_user_handler import RegisterUserHandler
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    
    user_repository.get_user_by_username.return_value = None
    user_repository.get_user_by_email.return_value = None
    
    password_hasher.hash_password.return_value = "hashed_password"
    
    handler = RegisterUserHandler(user_repository, password_hasher)
    await handler.handle(RegisterUserRequest(
        username="valid_user",
        email="valid_user@example.com",
        password="Password123*"
    ))
    
    user_repository.get_user_by_username.assert_called_once_with("valid_user")
    user_repository.get_user_by_email.assert_called_once_with("valid_user@example.com")
    password_hasher.hash_password.assert_called_once_with("Password123*")
    user_repository.save.assert_called_once()

@pytest.mark.asyncio
async def test_when_user_already_exists_should_return_error():
    from features.user_management.register_user.register_user_handler import RegisterUserHandler
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    
    user_repository.get_user_by_username.return_value = {"username": "existing_user"}
    
    handler = RegisterUserHandler(user_repository, password_hasher)
    response = await handler.handle(RegisterUserRequest(
        username="existing_user",
        email="existing_user@example.com",
        password="Password123*"
    ))
    
    assert response == {"status": "400", "message": "User existing_user already exists"}
    user_repository.get_user_by_username.assert_called_once_with("existing_user")
    user_repository.get_user_by_email.assert_not_called()
    password_hasher.hash_password.assert_not_called()
    user_repository.save.assert_not_called()
    
@pytest.mark.asyncio
async def test_when_email_already_registered_should_return_error():
    from features.user_management.register_user.register_user_handler import RegisterUserHandler
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    
    user_repository = AsyncMock()
    password_hasher = Mock()
    
    user_repository.get_user_by_username.return_value = None
    user_repository.get_user_by_email.return_value = {"email": "existing_email@example.com"}
    
    handler = RegisterUserHandler(user_repository, password_hasher)
    response = await handler.handle(RegisterUserRequest(
        username="new_user",
        email="existing_email@example.com",
        password="Password123*"
    ))
    
    assert response == {"status": "400", "message": "Email existing_email@example.com is already registered"}
    user_repository.get_user_by_username.assert_called_once_with("new_user")
    user_repository.get_user_by_email.assert_called_once_with("existing_email@example.com")
    password_hasher.hash_password.assert_not_called()
    user_repository.save.assert_not_called()
