import strawberry
from typing import List
from schema.user import UserType, user_service

@strawberry.type
class Query:

    @strawberry.field
    def users(self) -> List[UserType]:
        return user_service.getUsers()


    
