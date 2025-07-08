from fastapi import FastAPI
from app.api.v1.endpoints import search

app = FastAPI(
    title="Tickpick Alert",
    description="A simple API for Ticker Alert Notification",
    version="0.0.1"
)

app.include_router(search.router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "Welcome to the API! Check /docs for endpoints."}
