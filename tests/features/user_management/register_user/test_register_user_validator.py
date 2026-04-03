
def test_when_request_is_valid_should_return_user():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    request = RegisterUserRequest(username="testuser", email="testuser@example.com", password="Password123*")
    assert request.username == "testuser"
    assert request.email == "testuser@example.com"
    assert request.password == "Password123*"

def test_when_username_is_empty_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="", email="testuser@example.com", password="Password123*")

def test_when_username_is_too_long_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="a" * 51, email="testuser@example.com", password="Password123*")
        
def test_when_username_is_too_short_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="ab", email="testuser@example.com", password="Password123*")

def test_when_username_contains_invalid_characters_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="invalid username", email="testuser@example.com", password="Password123*")

def test_when_email_is_invalid_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="invalidemail", password="Password123*")

def test_when_password_is_too_short_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    SHORT_PASS = "short"
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="testuser@example.com", password=SHORT_PASS)

def test_when_password_is_too_long_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="testuser@example.com", password="P" * 129)
        
def test_when_password_does_not_contain_digit_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="testuser@example.com", password="PasswordWithoutDigit*")

def test_when_password_does_not_contain_letter_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    NUMERIC_PASS = "12345678*"
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="testuser@example.com", password=NUMERIC_PASS)

def test_when_password_does_not_contain_special_character_should_raise_validation_error():
    from features.user_management.register_user.register_user_request import RegisterUserRequest
    import pytest
    
    with pytest.raises(ValueError):
        RegisterUserRequest(username="testuser", email="testuser@example.com", password="Password123")
