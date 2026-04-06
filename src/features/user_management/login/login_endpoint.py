from typing import Annotated
from fastapi import APIRouter, Depends
from .login_request import LoginRequest
from .login_handler import LoginHandler
from ..shared.dependencies import get_login_handler

router = APIRouter()

@router.post("/login")
async def login_user(
    request: LoginRequest,
    handler: Annotated[LoginHandler, Depends(get_login_handler)],
):
    return await handler.handle(request)