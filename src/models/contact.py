from src.interfaces.contact import Contact
from src.loaders.db import database

contacts = [
    {
        'id': 1,
        'name': 'Nestor',
        'cellphone': '3022341426'
    },
    {
        'id': 2,
        'name': 'Juanito',
        'cellphone': '3023348482'
    }
]


class ContactModel:
    @staticmethod
    async def setup():
        query = """CREATE TABLE IF NOT EXISTS contact.contact (id INTEGER PRIMARY KEY, name VARCHAR(100), cellphone VARCHAR(10))"""
        await database.execute(query=query)

    @staticmethod
    def save(contact: Contact):
        contacts.append(contact)
        return contact

    @staticmethod
    def findAll():
        return contacts

    @staticmethod
    def findOne(id):
        contactsFound = [
            contact for contact in contacts if contact['id'] == id]
        if (len(contactsFound) > 0):
            return contactsFound[0]
        return null

    @staticmethod
    def update(id: int, contact: Contact):
        contactsFound = [
            contact for contact in contacts if contact['id'] == id]
        if (len(contactsFound) > 0):
            contactsFound[0]['name'] = contact.name
            contactsFound[0]['cellphone'] = contact.cellphone
            return contactsFound[0]
        return null
