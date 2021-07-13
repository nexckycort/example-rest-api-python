from fastapi import APIRouter
from src.services.contact import ContactServices
from src.interfaces.contact import Contact

contact = APIRouter()


@contact.post("/")
async def saveContact(contact: Contact):
    return ContactServices.save(contact)


@contact.get("/")
async def getContacts():
    return ContactServices.findAll()


@contact.get("/{id}")
async def getContact(id: int):
    return ContactServices.findOne(id)


@contact.put("/{id}")
async def updateContact(id: int, contact: Contact):
    return ContactServices.update(id, contact)
