from pydantic import BaseModel, field_validator
import re

USERNAME_PATTERN = r'\w+$'

class LoginRequest(BaseModel):
    username: str
    password: str
    
    @field_validator('username')
    def validate_username(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Username must be at least 3 characters long")
        if len(value) > 20:
            raise ValueError("Username must be no more than 20 characters long")
        if not re.match(USERNAME_PATTERN, value):
            raise ValueError("Username can only contain letters, numbers, and underscores")
        return value
    
    @field_validator('password')
    def validate_password(cls, value : str) -> str:
        if len(value) < 6:
            raise ValueError("Password must be at least 6 characters long")
        if len(value) > 20:
            raise ValueError("Password must be no more than 20 characters long")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit")
        if not any(char.isalpha() for char in value):
            raise ValueError("Password must contain at least one letter")
        if not any(char in "!@#$%^&*()_+-=[]{}|;':,.<>?/" for char in value):
            raise ValueError("Password must contain at least one special character")
        return value