from fastapi import APIRouter, Query

router = APIRouter(prefix="/dont_sleeping_server", tags=["dont_sleeping_server"])

@router.get("/")