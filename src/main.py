from fastapi import FastAPI

from .router import api_router

app = FastAPI(title="Case Pilar")

app.include_router(api_router)
