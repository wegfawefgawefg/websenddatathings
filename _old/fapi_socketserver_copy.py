import asyncio
import random
import time
from fastapi import FastAPI, WebSocket

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        # data = await websocket.receive_text()
        # await asyncio.sleep(0.5)
        # print("sending data")
        random_x = random.randint(0, 100)
        random_y = random.randint(0, 100)
        await websocket.send_json({"x": random_x, "y": random_y})
        # await websocket.send_text(data)
