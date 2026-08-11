from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

import uuid
import shutil
import os


router = APIRouter(
    prefix="/media",
    tags=["Media"]
)


UPLOAD_DIR = "uploads/files"


os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)



@router.post("/upload")
async def upload(

    user_id:str = Form(...),

    file:UploadFile = File(...)

):


    filename = (

        str(uuid.uuid4())

        +

        "_"

        +

        file.filename

    )


    path = (

        UPLOAD_DIR

        +

        "/"

        +

        filename

    )


    with open(
        path,
        "wb"
    ) as buffer:


        shutil.copyfileobj(

            file.file,

            buffer

        )


    return {

        "status":"uploaded",

        "file":filename

    }