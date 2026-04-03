from fastapi import APIRouter
from .register_user_request import RegisterUserRequest
from .register_user_handler import RegisterUserHandler

router = APIRouter()
handler = RegisterUserHandler()

@router.post("/register")
async def register_user(request: RegisterUserRequest):
    return handler.handle(request)