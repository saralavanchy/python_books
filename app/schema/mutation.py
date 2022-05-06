from graphql import GraphQLErrorExtensions
import strawberry
from typing import Optional
from schema.user import UserType, user_service
from model.user import UserIn

@strawberry.type
class Mutation:
    
    @strawberry.mutation
    async def addUser(self, name: str, surname: str, address: str, email: str, dni: Optional[int] ) -> UserType:
        userIn = UserIn(name=name, surname=surname, dni=dni, address=address, email=email)
        user = user_service.addUser(userIn=userIn)
        return user

    @strawberry.mutation
    async def updateUser(self, id: int, name: Optional[str] = None, surname: Optional[str] = None, address: Optional[str] = None, email: Optional[str] = None, dni: Optional[int] = None ) -> UserType:
        user = user_service.getUserById(id)
        if user == None:
            raise Exception("Can't find user")

        userIn = UserIn(name=name or user.name, surname=surname or user.surname, dni=dni or user.dni, address=address or user.address, email=email or user.email)
        updatedUser = user_service.updateUser(userIn=userIn, user_id=id)
        return updatedUser
    
    @strawberry.mutation
    async def deleteUser(self, id: int) -> UserType:
        user = user_service.getUserById(id)
        if not user_service.existsUser(user):
            raise Exception("Can't find user")
        user_service.deleteUser(id)
        return user