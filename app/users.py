from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/{user_id}")
def get_user(

    user_id: str,

    db: Session = Depends(get_db)

):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {

        "id": user.id,

        "username": user.username,

        "nickname": user.nickname,

        "avatar": user.avatar,

        "bio": user.bio,

        "online": user.online

    }


@router.get("/search/{username}")
def search(

    username: str,

    db: Session = Depends(get_db)

):

    users = db.query(User).filter(
        User.username.contains(
            username
        )
    ).all()

    return [

        {

            "id": u.id,

            "username": u.username,

            "nickname": u.nickname

        }

        for u in users

    ]