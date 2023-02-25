# socketio basic client

import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("connection established")
    sio.emit("my_message", {"data": "foo"})


@sio.event
def my_response(data):
    print("received response", data)


sio.connect("http://localhost:5000")
sio.wait()
