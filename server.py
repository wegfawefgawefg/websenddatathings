import asyncio
import random
from dataclasses import dataclass
from typing import Any
from fastapi import FastAPI, WebSocket

from hand_mp import start_gettin_handy_info
from hand_mp import hand_info

app = FastAPI()


@dataclass
class SharedData:
    data: Any = None


shared_hand_data = SharedData()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # await asyncio.sleep(0.5)
        await websocket.send_json(shared_hand_data.data)


from threading import Thread

Thread(target=start_gettin_handy_info, args=(shared_hand_data,)).start()
