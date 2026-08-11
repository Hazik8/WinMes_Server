from fastapi import APIRouter


router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)



notifications = {}



@router.post("/{user_id}")
def send_notification(

    user_id:str,

    text:str

):


    if user_id not in notifications:

        notifications[user_id] = []



    notifications[user_id].append(

        text

    )


    return {

        "status":"sent"

    }



@router.get("/{user_id}")
def get_notifications(

    user_id:str

):


    return {

        "notifications":

        notifications.get(

            user_id,

            []

        )

    }