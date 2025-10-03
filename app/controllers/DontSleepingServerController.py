from fastapi import APIRouter

router = APIRouter(prefix="/server", tags=["server"])

@router.api_route("/ping", methods=["GET", "HEAD"])
def ping():
    return {"status": "ok"}