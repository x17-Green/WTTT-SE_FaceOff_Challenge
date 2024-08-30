# socket.io 
from flask_socketio import SocketIO, emit, join_room, leave_room
from config.config import Config


from flask import request
from flask_socketio import SocketIO, emit, join_room, leave_room, Namespace
from config.config import Config

socketio = SocketIO(logging=True, cors_allowed_origins=Config.CORS_ALLOWED_ORIGINS)

class GameNamespace(Namespace):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rooms = {}

    def on_connect(self):
        print('Client connected')

    def on_disconnect(self):
        print('Client disconnected')
        # Remove player from room if necessary
        for room in self.rooms:
            if request.sid in self.rooms[room]['players']:
                self.rooms[room]['players'].remove(request.sid)
                leave_room(room)
                if len(self.rooms[room]['players']) == 0:
                    del self.rooms[room]
                break

    def on_join_room(self, data):
        room_id = data['room_id']
        if room_id not in self.rooms:
            self.rooms[room_id] = {'players': []}
        self.rooms[room_id]['players'].append(request.sid)
        join_room(room_id)
        emit('joined_room', {'room_id': room_id})

    def on_leave_room(self, data):
        room_id = data['room_id']
        if room_id in self.rooms and request.sid in self.rooms[room_id]['players']:
            self.rooms[room_id]['players'].remove(request.sid)
            leave_room(room_id)
            if len(self.rooms[room_id]['players']) == 0:
                del self.rooms[room_id]
            emit('left_room', {'room_id': room_id})

socketio.on_namespace(GameNamespace('/game'))



socketio = SocketIO(logging=True, cors_allowed_origins=Config.CORS_ALLOWED_ORIGINS)

rooms = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    # Remove player from room if necessary
    for room in rooms:
        if request.sid in rooms[room]['players']:
            rooms[room]['players'].remove(request.sid)
            leave_room(room)
            if len(rooms[room]['players']) == 0:
                del rooms[room]
            break