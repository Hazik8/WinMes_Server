from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

import uuid

from app.database import get_db
from app.models import Device



router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)



@router.post("/register")
def register_device(

    user_id:str,

    device_name:str,

    device_type:str,

    push_token:str="",

    db:Session=Depends(get_db)

):


    device = Device(

        id=str(uuid.uuid4()),

        user_id=user_id,

        device_name=device_name,

        device_type=device_type,

        push_token=push_token

    )


    db.add(device)

    db.commit()


    return {

        "status":"registered",

        "device_id":device.id

    }



@router.get("/{user_id}")
def get_devices(

    user_id:str,

    db:Session=Depends(get_db)

):


    devices = db.query(Device).filter(

        Device.user_id == user_id

    ).all()



    return [

        {

        "id":d.id,

        "name":d.device_name,

        "type":d.device_type,

        "online":d.active

        }

        for d in devices

    ]