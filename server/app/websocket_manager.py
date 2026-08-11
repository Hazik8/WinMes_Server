from fastapi import WebSocket
from typing import Dict


class ConnectionManager:

    def __init__(self):

        self.connections: Dict[
            str,
            WebSocket
        ] = {}


    async def connect(

        self,

        user_id: str,

        websocket: WebSocket

    ):

        await websocket.accept()

        self.connections[
            user_id
        ] = websocket


    def disconnect(

        self,

        user_id: str

    ):

        self.connections.pop(
            user_id,
            None
        )


    async def send(

        self,

        receiver: str,

        message: dict

    ):

        socket = self.connections.get(
            receiver
        )

        if socket:

            await socket.send_json(
                message
            )


manager = ConnectionManager()