"""Main module for the FastAPI application.

This module initializes the FastAPI application and defines the main API routes.
"""

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routers import fight

app = FastAPI()


@app.get('/', include_in_schema=False)
def root():
    """Redirects to the '/kombat' route."""
    return RedirectResponse(url='/kombat/')


# Include the 'fight' router with the prefix '/kombat'
app.include_router(fight.router, prefix='/kombat', tags=['kombat'])
