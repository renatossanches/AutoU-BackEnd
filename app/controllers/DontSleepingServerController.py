from fastapi import APIRouter

router = APIRouter(prefix="/server", tags=["server"])
@router.get("/ping")
def ping():
    return {"status": "ok"}