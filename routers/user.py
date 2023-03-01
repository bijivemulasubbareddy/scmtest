from fastapi import APIRouter, Request
from model.user import User
from config.db import connection
from schemas.user import userEntity, usersEntity
from bson import ObjectId
from fastapi.templating import Jinja2Templates


user = APIRouter()
templates = Jinja2Templates(directory="Templates")



@user.get('/')
async def find_all_users(request: Request):
    print(connection.local.user.find())
    print(usersEntity(connection.local.user.find()))
    return templates.TemplateResponse("SignUp.html", {"request": request})
    # return usersEntity(connection.local.user.find())

@user.get('/{id}')
async def find_one_user(id, user: User):
    return userEntity(connection.local.user.find_one({"_id":ObjectId(id)}))


@user.post('/')
async def create_user(user: User):
    connection.local.user.insert_one(dict(user))
    return usersEntity(connection.local.user.find())


@user.put('/{id}')
async def update_user(id, user: User):
    connection.local.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return userEntity(connection.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id, user: User):
    return userEntity(connection.local.user.find_one_and_delete({"_id": ObjectId(id)}))