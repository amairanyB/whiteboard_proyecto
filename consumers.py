import asyncio
import json
from channels.consumer import AsyncConsumer

class BoardConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('connected', event)
        board_room = "boardroom"  # Nombre del grupo de WebSocket
        self.board_room = board_room
        await self.channel_layer.group_add(
            board_room,  # Añadir a un grupo de WebSocket
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"  # Aceptar la conexión
        })

    async def websocket_receive(self, event):
        drawing_data = event.get('text', None)
        # Enviar el dato de dibujo a todos los miembros del grupo
        await self.channel_layer.group_send(
            self.board_room,
            {
                "type": "board_message",
                "text": drawing_data
            })

    async def board_message(self, event):
        # Enviar el mensaje de vuelta a todos los miembros del grupo
        await self.send({
            "type": 'websocket.send',
            'text': event['text']
        })

    async def websocket_disconnect(self, event):
        print('disconnected', event)

