from fastapi import APIRouter
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from app.websocket_manager import manager
from app.models import Message
from app.utils import generate_message_id

router = APIRouter()


@router.websocket("/ws/{user_id}")
async def websocket_chat(

    websocket: WebSocket,

    user_id: str

):

    await manager.connect(

        user_id,

        websocket

    )


    try:

        while True:

            data = await websocket.receive_json()

            receiver = data["receiver"]

            text = data["message"]


            await manager.send(

                receiver,

                {

                    "sender": user_id,

                    "message": text

                }

            )


    except WebSocketDisconnect:

        manager.disconnect(
            user_id
        )

    message = Message(

    id=generate_message_id(),

    sender=user_id,

    receiver=receiver,

    text=text

    )

    db.add(message) # type: ignore

    db.commit() # type: ignore
