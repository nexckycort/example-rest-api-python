from fastapi import FastAPI
from src.api.routes.v1.contact.router import contact

app = FastAPI()

app.include_router(contact, prefix="/api/v1/contact")
