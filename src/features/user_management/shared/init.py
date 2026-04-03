from fastapi import APIRouter

from  ..register_user.register_user_endpoint import router as register_user_router


router = APIRouter()
router.include_router(register_user_router)