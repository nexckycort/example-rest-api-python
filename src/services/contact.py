from src.models.contact import ContactModel
from src.interfaces.contact import Contact


class ContactServices:
    @staticmethod
    async def setup():
        await ContactModel.setup()
        print("create table contact")

    @staticmethod
    async def save(contact: Contact):
        return await ContactModel.save(contact)

    @staticmethod
    async def findAll():
        return await ContactModel.findAll()

    @staticmethod
    async def findOne(id):
        return await ContactModel.findOne(id)

    @staticmethod
    async def update(id: int, contact: Contact):
        return await ContactModel.update(id, contact)
