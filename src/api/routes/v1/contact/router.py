from fastapi import APIRouter
from src.services.contact import ContactServices
from src.interfaces.contact import Contact

contact = APIRouter()


@contact.post("/")
async def saveContact(contact: Contact):
    return await ContactServices.save(contact)


@contact.get("/")
async def getContacts():
    return await ContactServices.findAll()


@contact.get("/{id}")
async def getContact(id: int):
    return await ContactServices.findOne(id)


@contact.put("/{id}")
async def updateContact(id: int, contact: Contact):
    return await ContactServices.update(id, contact)
