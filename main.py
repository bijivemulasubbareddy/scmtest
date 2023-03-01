from fastapi import FastAPI, Request, Form, Body, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bson import ObjectId
from pydantic import BaseModel
from pydantic import BaseSettings
import pymongo
from pymongo import MongoClient
import os
import uvicorn
from config.db import MONGO_URI
from dotenv import dotenv_values
from schemas.user import usersEntity, userEntity
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from model.user import Login, User, Createshipment
from typing import List
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def hash_password(password: str):  
    return pwd_context.hash(password)
def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


templates = Jinja2Templates(directory="Templates")

config = dotenv_values(".env")
connection=MongoClient(config["MONGO_URI"])
app = FastAPI()
router_login = APIRouter()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="Templates")
list_of_usernames = list()


# generate name using all categories


# client = pymongo.MongoClient(os.getenv("connection"))
# print("mongo_Commection",client)

db = connection['Scmxpert1']

### login post and get methods ######


@app.get("/", response_class=HTMLResponse, name="samplesignup")
async def root(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request})


@app.post('/Dashboard', response_class=HTMLResponse, name="Login",)
async def login(request: Request, email: str = Form(...), password: str = Form(...)):
    UserEmail = email
    UserPassword = password
    col = db["Users"]
    logindata = col.find_one({"Email": UserEmail})
    # print(Useremail)
    if not logindata:
        print("no records")
        return templates.TemplateResponse('Invalid.html', {'message': "invalid email", 'request': request})
    else:
        # print(logindata['Password'])
        # if logindata['Password'] == Userpassword:
        if verify_password(UserPassword,logindata['Password']):
            return templates.TemplateResponse('Dashboard.html', {'request': request, 'user': db})
        else:
            return templates.TemplateResponse('Invalid.html', {'message': 'invalid password', 'request': request})

#################### login API end ###################

## ************** Forgot API START*********##########


@app.get('/Forgot', response_class=HTMLResponse, name="Forgot")
async def forgot(request: Request):
    return templates.TemplateResponse("ForgotPassword.html", {"request": request})

##### ************** Forgot API END*********##########

## ************** Dashboard API START *********##########


@app.get('/Dashboard', response_class=HTMLResponse, name="Dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("Dashboard.html", {"request": request})

## ************** Dashboard API END *********##########

## ************** Shipment API START *********##########


@app.get('/Shipment', response_class=HTMLResponse, name="Shipment")
async def shipment(request: Request):
    return templates.TemplateResponse("Shipment.html", {"request": request})


@app.post('/Submitshipmentdetails', response_class=HTMLResponse, name="submitshipmentdetails")
async def submitshipmentdetails(request: Request, Shipmentinvoice: int = Form(...), Containernumber: int = Form(...), Shipmentdescription: str = Form(...), Routedetails: str = Form(...),
                                Goodtypes: str = Form(...),
                                Device: str = Form(...),
                                Expecteddelivery: str = Form(...),
                                POnumber: int = Form(...),
                                Delivarynumber: int = Form(...),
                                NDCnumber: int = Form(...),
                                BatchId: str = Form(...),
                                Serialnumber: str = Form(...)
                                ):

    shipmentdata = Createshipment(Shipment_invoicenumber=Shipmentinvoice,
                                  Container_Number=Containernumber,
                                  Shipment_Description=Shipmentdescription,
                                  Route_Details=Routedetails,
                                  Goods_Type=Goodtypes,
                                  Device=Device,
                                  Expected_Delivary_Date=Expecteddelivery,
                                  PO_Number=POnumber,
                                  Deliver_Number=Delivarynumber,
                                  NDC_Number=NDCnumber,
                                  Batch_ID=BatchId,
                                  Serial_Number_of_Goods=Serialnumber
                                  )
    shipment = db['Shipment'].insert_one(dict(shipmentdata))

    return templates.TemplateResponse("Shipment.html", {"request": request, "shipmentData": shipment})


## ************** Shipment API END *********##########

## ************** Devicedata API START *********##########

@app.get('/Devicedata', response_class=HTMLResponse, name="Devicedata")
async def shipment(request: Request):
    shipments = []
    shipments_all = db["Device_data"].find({}, {"_id": 0})
    for d in shipments_all:
        shipments.append(d)

    return templates.TemplateResponse("Devicedata.html", {"request": request, "shipments": shipments})

## ************** Devicedata API END *********##########

## ************** SignUp API'S START *********##########


@app.post('/SignUp', response_class=HTMLResponse, name="signup")
async def signup(request: Request, username: str = Form(...), email: str = Form(...),  password: str = Form(...), Confirmpassword: str = Form(...)):
    hashed_password = hash_password(password)
    data = User(Username=username, Email=email,
                Password=hashed_password, Confirmpassword=hashed_password)
    logindata = db['Users'].find_one({"Email": email})
    # print("login data",logindata)
    if not logindata:
        # print("no records")
        new_signup = db['Users'].insert_one(dict(data))
        return templates.TemplateResponse("SignUp.html", {"request": request, "user_login": new_signup})
    else:
        return templates.TemplateResponse('Invalid.html', {'message': "invalid email", 'request': request})
    # print(data, "data at signup")
    


@app.get('/SignUp', response_class=HTMLResponse, name="sign")
async def login(request: Request):
    return templates.TemplateResponse("SignUp.html", {"request": request})

## ************** SignUp API END *********##########
