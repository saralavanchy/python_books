from fastapi import APIRouter, HTTPException
from typing import Optional
from model.user import UserIn
from service.user_service import UserService

router = APIRouter()
user_service = UserService()

@router.get("/user/{user_id}/hello", tags=["user"])
def say_hello(user_id: int):
    user = user_service.getUserById(user_id)
    if(user == None):
        raise HTTPException(status_code=404, detail="User not found")
    return { "data": f"Hello {user.fullName()}!", "user": user }

@router.get("/user/{user_id}", tags=["user"])
def say_hello(user_id: int):
    user = user_service.getUserById(user_id)
    if(user == None):
        raise HTTPException(status_code=404, detail="User not found")
    return { "data": user }

@router.get("/user", tags=["user"])
def get_user(name: Optional[str] = None):
    if(name is None):
        return {"data": user_service.getUsers()}
    if not user_service.existsUser(name = name):
        raise HTTPException(status_code=404, detail=f"A user with name {name} was not found")
    return { "data": user_service.getUserByName(name) }

@router.post("/user", tags=["user"])
def create_user(userIn: UserIn):
    if user_service.existsUser(user=userIn):
        raise HTTPException(status_code=400, detail="User already exists")
    user = user_service.addUser(userIn)
    return user

@router.delete("/user/{user_id}", tags=["user"])
def delete_user(user_id: int):
    user = user_service.getUserById(user_id)
    if user == None:
        raise HTTPException(status_code=404, detail=f"A user with id {user_id} was not found")
    user_service.deleteUser(user_id)
    return user

@router.put("/user/{user_id}", tags=["user"])
def update_user(user_id: int, userIn: UserIn):
    user = user_service.getUserById(user_id)
    if user == None:
        raise HTTPException(status_code=404, detail=f"A user with id {user_id} was not found")
    user_service.updateUser(userIn, user_id)