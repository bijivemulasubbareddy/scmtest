def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "Username": item["Username"],
        "email": item["Email"],
        "password": item["Password"],
        "confirmpassword": item["Confirmpassword"]
    }


def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]


def login(item)->dict:
    return{
        "email": item["Email"],
        "password": item["Password"]
    }

def login(entity) ->list:
    return [login(item) for item in entity]




def shipment(item) -> dict:
    return {
        "id": str(item["_id"]),
        "shipment_invoicenumber": item["Shipment_invoicenumber"],
        "container_number": item["Container_Number"],
        "shipment_Description": item["Shipment_Description"],
        "Route_Details": item["Route_Details"]
    }


def shipments(entity) -> list:
    return [shipment(item) for item in entity]
