from src.models.contact import ContactModel
from src.interfaces.contact import Contact


class ContactServices:
    @staticmethod
    def save(contact: Contact):
        return ContactModel.save(contact)

    @staticmethod
    def findAll():
        return ContactModel.findAll()

    @staticmethod
    def findOne(id):
        return ContactModel.findOne(id)

    @staticmethod
    def update(id: int, contact: Contact):
        return ContactModel.update(id, contact)
