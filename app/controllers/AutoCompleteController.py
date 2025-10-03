from fastapi import APIRouter, Query
from app.ai.AutoComplete import autocomplete

router = APIRouter(prefix="/autocomplete", tags=["Autocomplete"])

@router.get("/ping")
def ping():
    return {"status": "ok"}
