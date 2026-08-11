from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from app.database import get_db
from app.models import Message
from app.cloud_crypto import encrypt_data



router = APIRouter(

    prefix="/backup",

    tags=["Backup"]

)



@router.get("/{user_id}")

def create_backup(

    user_id:str,

    db:Session=Depends(get_db)

):


    messages = db.query(Message).filter(

        (Message.sender == user_id) |

        (Message.receiver == user_id)

    ).all()



    backup = [

        {

        "sender":m.sender,

        "receiver":m.receiver,

        "text":m.text

        }

        for m in messages

    ]



    return {

    "backup":

    encrypt_data(

        str(backup)

    )

}