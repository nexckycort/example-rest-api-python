from pydantic import BaseModel
from typing import Optional


class Contact(BaseModel):
    id: Optional[int] = None
    name: str
    cellphone: str
