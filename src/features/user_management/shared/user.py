
from enum import Enum

class UserStatus(Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User:
    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = password
        self.status = UserStatus.ACTIVE

    def deactivate(self):
        self.status = UserStatus.INACTIVE
    
    def suspend(self):
        self.status = UserStatus.SUSPENDED
