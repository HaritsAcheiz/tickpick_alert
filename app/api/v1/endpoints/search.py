from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Optional
from app.services.tickpick import TickpickScraper
from app.schemas.search import SearchResult, SearchError

router = APIRouter(
    prefix="",
    tags=["Search"],
    responses={500: {"model": SearchError, "description": "Internal Server Error"}},
)


@router.get(
    "/search",
    response_model=SearchResult,
    summary="Search TickPick for events/tickets by term",
    description="Performs a web scrape on TickPick's search results page for a given term.",
    responses={
        200: {"description": "Successfully scraped and returned results"},
        400: {"description": "Bad Request, e.g., missing search term"},
        424: {"model": SearchError, "description": "Failed Dependency (e.g., scraping error)"},
    }
)

async def search_tickpick(search_term: str = Query(..., min_length=3, max_length=100, description="The term to search for on TickPick.")):
    scraper = TickpickScraper()

    try:
        results = scraper.search_by_term(searchTerm=search_term)

        if not results:
            return SearchResult(results=[], search_term=search_term, message="No results found for the given search term.")
        return SearchResult(results=results, search_term=search_term)
    except Exception as e:
        print(f"Scraping error: {e}")
        raise HTTPException(
            status_code=status.HTTP_424_FAILED_DEPENDENCY,
            detail=f"Failed to scrape TickPick: {str(e)}"
        )
