"""
use socketio for server
"""

import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.event
def disconnect(sid):
    print("disconnect ", sid)


@sio.event
def my_message(sid, data):
    print("message ", data)
    sio.emit("my response", {"response": "my response"}, room=sid)


if __name__ == "__main__":
    from wsgiref import simple_server

    srv = simple_server.make_server("localhost", 5000, app)
    srv.serve_forever()
