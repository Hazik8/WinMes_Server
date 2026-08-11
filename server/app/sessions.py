from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Device


router = APIRouter(
    prefix="/sessions",
    tags=["Sessions"]
)


@router.delete("/logout-all/{user_id}")
def logout_all(

    user_id: str,

    db: Session = Depends(get_db)

):

    devices = db.query(Device).filter(

        Device.user_id == user_id

    ).all()


    for device in devices:

        device.active = False


    db.commit()


    return {

        "status": "logged_out",

        "devices": len(devices)

    }