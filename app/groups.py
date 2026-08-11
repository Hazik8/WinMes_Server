from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

import uuid


from app.database import get_db

from app.models import Group
from app.models import GroupMember



router = APIRouter(
    prefix="/groups",
    tags=["Groups"]
)



@router.post("/create")
def create_group(

    name: str,

    owner: str,

    db: Session = Depends(get_db)

):

    group = Group(

        id=str(uuid.uuid4()),

        name=name,

        owner=owner

    )


    db.add(group)



    member = GroupMember(

        group_id=group.id,

        user_id=owner,

        role="admin"

    )


    db.add(member)

    db.commit()


    return {

        "status":"created",

        "group_id":group.id

    }




@router.post("/{group_id}/add")
def add_member(

    group_id:str,

    user_id:str,

    db:Session=Depends(get_db)

):

    member = GroupMember(

        group_id=group_id,

        user_id=user_id

    )


    db.add(member)

    db.commit()


    return {

        "status":"added"

    }