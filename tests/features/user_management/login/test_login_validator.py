
def test_when_is_valid_should_return_login_request():
    from features.user_management.login.login_request import LoginRequest
    request = LoginRequest(username="testuser", password="Password123*")
    assert request.username == "testuser"
    assert request.password == "Password123*"

def test_when_username_is_empty_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="", password="Password123*")
def test_when_username_is_too_long_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="a" * 51, password="Password123*")
        
def test_when_username_is_too_short_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="ab", password="Password123*")

def test_when_username_contains_invalid_characters_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="invalid username", password="Password123*")

def test_when_password_is_too_short_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    SHORT_PASS = "short"
    with pytest.raises(ValueError):
        LoginRequest(username="testuser", password=SHORT_PASS)

def test_when_password_is_too_long_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="testuser", password="P" * 129)

def test_when_password_does_not_contain_digit_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="testuser", password="Password*")

def test_when_password_does_not_contain_letter_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    NUMERIC_PASS = "123456*"
    with pytest.raises(ValueError):
        LoginRequest(username="testuser", password=NUMERIC_PASS)

def test_when_password_does_not_contain_special_character_should_raise_validation_error():
    from features.user_management.login.login_request import LoginRequest
    import pytest
    
    with pytest.raises(ValueError):
        LoginRequest(username="testuser", password="Password123")