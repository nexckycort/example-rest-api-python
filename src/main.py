from fastapi import FastAPI
from src.loaders.db import database
from src.api.routes.v1.contact.router import contact
from src.services.contact import ContactServices

app = FastAPI()


@app.on_event("startup")
async def startup():
    print("database connect")
    await database.connect()
    await ContactServices.setup()


@app.on_event("shutdown")
async def shutdown():
    print("database disconnect")
    await database.disconnect()


app.include_router(contact, prefix="/api/v1/contact")
