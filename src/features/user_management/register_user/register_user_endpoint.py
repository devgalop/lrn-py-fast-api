from typing import Annotated
from fastapi import APIRouter, Depends
from .register_user_request import RegisterUserRequest
from .register_user_handler import RegisterUserHandler
from .dependencies import get_register_user_handler

router = APIRouter()

@router.post("/register")
async def register_user(
    request: RegisterUserRequest,
    handler: Annotated[RegisterUserHandler, Depends(get_register_user_handler)],
):
    return await handler.handle(request)