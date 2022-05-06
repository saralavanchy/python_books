from typing import  Optional, Union
from model.user import User, UserIn

class UserService():
    def __init__(self):
        self.users = {}
        self.users[1] = User(name = "sara", surname = "lavanchy", id = 1, address = "some street 1234", email = "sara@email.com")
        self.users[2] = User(name = "juan", surname = "perez", id = 2 , address = "other street 123", email = "juanperez@email.com")
        self.users[3] = User(name = "rodrigo", surname = "soria", id = 3, address = "unknown street 4321", email = "rodrigo@email.com")

    def getUsers(self):
        user_list = []
        for user in self.users.values():
            user_list.append(user)
        return  user_list

    def addUser(self, userIn: UserIn) -> User:
        next_id = len(self.users.values()) + 1
        user = userIn.mapUser(next_id)
        self.users[next_id] = user
        return user

    def deleteUser(self, id: int):
        del self.users[id]

    def getUserById(self, id: int) -> User:
        for user in self.users.values():
            if (user.id == id):
                return user
        return None

    def getUserByName(self, name: str) -> User:
        for user in self.users.values():
            if (user.name.lower() == name.lower()):
                return user
        return None

    def existsUser(self, name: Optional[str] = None, user: Optional[Union[User,UserIn]] = None, id: Optional[int] = -1) -> bool:
        return id in self.users.keys() or name in self.users.values() or user in self.users.values()

    def updateUser(self, userIn: UserIn, user_id: int):
        new_user = userIn.mapUser(user_id)
        self.users[user_id] = new_user
        return new_user