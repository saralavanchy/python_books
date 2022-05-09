import strawberry
from model.user import User
from service.user_service import UserService

user_service = UserService()

@strawberry.experimental.pydantic.type(model=User, all_fields=True)
class UserType:
    pass
