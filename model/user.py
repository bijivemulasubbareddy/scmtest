from pydantic import BaseModel, Field
from bson import ObjectId
import uuid





class User(BaseModel):

    Username:  str
    Email: str
    Password: str
    Confirmpassword: str

    class Config:
        # arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}
        allow_population_by_field_name = True
        orm_mode = True
        schema_extra = {
            "example": {
                "Username": "Jane Doe",
                "email": "jdoe@example.com",
                "password": "abcdef@123456789",
                "confirmpassword": "abcdef@123456789"
            }
        }


class Login(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    # Name: str = Field(...)
    Email: str = Field(...)
    password: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        # json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                # "_id": "639865485bdc2626b2a294f9",
                # "Name": "DonQuixote",
                "Email": "subbu@gmail.com",
                "password": "..."
            }
        }


class Createshipment(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    Shipment_invoicenumber: int = Field(...)
    Container_Number: str = Field(...)
    Shipment_Description: str = Field(...)
    Route_Details: str = Field(...)
    Goods_Type: str = Field(...)
    Device: str = Field(...)
    Expected_Delivary_Date: str = Field(...)
    PO_Number: int = Field(...)
    Deliver_Number: int = Field(...)
    NDC_Number: int = Field(...)
    Batch_ID: str = Field(...)
    Serial_Number_of_Goods: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        orm_mode = True
        schema_extra = {
            "example": {
                "_id": "066de609-b04a-4b30-b46c-32537c7f1f6e",
                "shipment_invoicenumber": "number123",
                "container_number": "number123",
                "shipment_Description": "number123",
                "Route_Details":"number123",
                "Goods_Type":"number123",
                "Device":"number123",
                "Expected_Date":"number123",
                "PO_Number":"number123",
                "NDC_Number":"number123",
                "Batch_ID":"number123",
                "Serial_Number_of_Goods":"number123",
            }
        }
