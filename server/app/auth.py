from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import RegisterRequest
from app.schemas import LoginRequest

from app.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.id_generator import generate_user_id

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.username == request.username
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    user = User(

        id=generate_user_id(),

        username=request.username,

        nickname=request.nickname,

        password=hash_password(
            request.password
        )

    )

    db.add(user)

    db.commit()

    db.refresh(user)

    token = create_access_token(
        user.id
    )

    return {

        "status": "ok",

        "id": user.id,

        "nickname": user.nickname,

        "token": token

    }


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.id == request.id
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        request.password,
        user.password
    ):

        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    token = create_access_token(
        user.id
    )

    return {

        "status": "ok",

        "id": user.id,

        "nickname": user.nickname,

        "token": token

    }