from src.interfaces.contact import Contact
from src.loaders.db import database


class ContactModel:
    @staticmethod
    async def setup():
        query = """CREATE TABLE IF NOT EXISTS contact.contact (id serial PRIMARY KEY, name VARCHAR(100), cellphone VARCHAR(10))"""
        await database.execute(query=query)

    @staticmethod
    async def save(contact: Contact):
        query = "INSERT INTO contact.contact(name, cellphone) VALUES (:name, :cellphone)"
        values = [
            {"name": contact.name, "cellphone": contact.cellphone}
        ]
        await database.execute_many(query=query, values=values)
        return {"message": "contact created"}

    @staticmethod
    async def findAll():
        query = "SELECT * FROM contact.contact"
        contactsRecord = await database.fetch_all(query=query)
        return {
            "message": "downloaded contacts",
            "data": contactsRecord
        }

    @staticmethod
    async def findOne(id):
        query = "SELECT * FROM contact.contact WHERE id = :id"
        contactRecord = await database.fetch_one(query=query, values={"id": id})
        return {
            "message": "contact downloaded",
            "data": contactsRecord
        }

    @staticmethod
    async def update(id: int, contact: Contact):
        query = "UPDATE contact.contact SET name = :name, cellphone = :cellphone WHERE id=1"
        values = [
            {"name": contact.name, "cellphone": contact.cellphone}
        ]
        await database.execute_many(query=query, values=values)
        return {"message": "updated contact"}
