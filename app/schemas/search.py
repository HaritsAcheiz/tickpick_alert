from pydantic import BaseModel
from typing import List, Optional


class SearchResult(BaseModel):
    """
    Schema for the results returned by the TickPick search scraper.
    """
    results: List[str]
    search_term: str
    status: str = "success"
    message: Optional[str] = None


class SearchError(BaseModel):
    """
    Schema for error responses from scraper-related endpoints.
    """
    detail: str
