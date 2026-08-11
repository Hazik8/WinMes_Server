from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Message


router = APIRouter(
    prefix="/sync",
    tags=["Sync"]
)



@router.get("/messages/{user_id}")
def sync_messages(

    user_id:str,

    db:Session=Depends(get_db)

):

    messages = db.query(Message).filter(

        (Message.sender == user_id) |

        (Message.receiver == user_id)

    ).all()


    return [

        {

        "id":m.id,

        "sender":m.sender,

        "receiver":m.receiver,

        "text":m.text,

        "read":m.is_read

        }

        for m in messages

    ]