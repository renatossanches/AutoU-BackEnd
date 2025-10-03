from fastapi import APIRouter, Query
from app.ai.AutoComplete import autocomplete


router = APIRouter(prefix="/autocomplete", tags=["Autocomplete"])

@router.get("/")
def get_autocomplete(q: str = Query(..., min_length=1), n: int = Query(5, gt=0)):
    """
    Retorna sugestões de autocomplete baseadas nos emails.
    """
    return {"suggestions": autocomplete(q, n)}