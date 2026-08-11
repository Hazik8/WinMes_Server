from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import UserSettings


router = APIRouter(

    prefix="/settings",

    tags=["Settings"]

)



@router.get("/{user_id}")

def get_settings(

    user_id:str,

    db:Session=Depends(get_db)

):

    settings = db.query(

        UserSettings

    ).filter(

        UserSettings.user_id == user_id

    ).first()



    if not settings:

        return {

            "theme":"dark",

            "language":"ru",

            "notifications":True

        }



    return {

        "theme":settings.theme,

        "language":settings.language,

        "notifications":settings.notifications

    }




@router.post("/{user_id}")

def update_settings(

    user_id:str,

    theme:str,

    language:str,

    notifications:bool,

    db:Session=Depends(get_db)

):

    settings = UserSettings(

        id=user_id,

        user_id=user_id,

        theme=theme,

        language=language,

        notifications=notifications

    )


    db.add(settings)

    db.commit()


    return {

        "status":"saved"

    }