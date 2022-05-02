from pydantic import BaseModel
from typing import List, Optional
from app.model.email import Email

class User(BaseModel):
    name: str
    surname: str
    id: int
    address: str
    email: str
    dni: Optional[int]

    def fullName(self) -> str:
        if not self.surname or not  self.name:
            return ""
        return f"{self.name.capitalize()} {self.surname.capitalize()}"

    def __eq__(self, other):
        if(isinstance(other, User)):
            return self.id == other.id or self.fullName() == other.fullName() or self.dni == other.dni()
        if(isinstance(other, UserIn)):
            return self.fullName() == other.fullName() or self.dni == other.dni
        return self.id == other or self.name.lower() == str(other).lower()

class UserIn(BaseModel):
    name: str
    surname: str
    address: str
    email: str
    dni: Optional[int]

    def fullName(self) -> str:
        return f"{self.name.capitalize()} {self.surname.capitalize()}"

    def mapUser(self, id: int) -> User:
        return User(name = self.name, surname = self.surname, address = self.address, email = self.email, dni = self.dni, id = id )