"""Main module for the FastAPI application.

This module initializes the FastAPI application and defines the main API
    routes.
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.adapters import router

app = FastAPI()


@app.get('/', include_in_schema=False)
def root():
    """Redirects to the '/kombat' route."""
    return RedirectResponse(url='/kombat/', status_code=307)


# Include the 'fight' router with the prefix '/kombat'
app.include_router(router.router, prefix='/kombat', tags=['kombat'])
