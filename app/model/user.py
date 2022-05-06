from pydantic import BaseModel, validator
from typing import List, Optional
from model.email import Email
from model.errors import InvalidEmailError

class BaseUser(BaseModel):
    name: str
    surname: str
    address: str
    email: str
    dni: Optional[int]

    def fullName(self) -> str:
        if not self.surname or not self.name:
            return ""
        return f"{self.name.capitalize()} {self.surname.capitalize()}"

    @validator("email")
    @classmethod
    def emailIsValid(cls, email: str):
        hasAtSign = email.find("@") != -1
        if not hasAtSign:
            raise InvalidEmailError(message="The email must have at sign", value=email)
        return  email

class User(BaseUser):
    id: int

    def __eq__(self, other):
        if(isinstance(other, User)):
            return self.id == other.id or self.fullName() == other.fullName() or self.dni == other.dni()
        if(isinstance(other, UserIn)):
            return self.fullName() == other.fullName() or self.dni == other.dni
        return self.id == other or self.name.lower() == str(other).lower()

class UserIn(BaseUser):

    def mapUser(self, id: int) -> User:
        return User(name = self.name, surname = self.surname, address = self.address, email = self.email, dni = self.dni, id = id )
