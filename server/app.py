from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit

app = Flask(__name__)
socketio = SocketIO(app)

rooms = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join_game')
def handle_join_game(data):
    room = data['room']
    player_name = data['playerName']

    if room not in rooms:
        rooms[room] = {
            'players': [],
            'game_state': [[' ' for _ in range(3)] for _ in range(3)],
            'game_paused': False
        }
    
    room_info = rooms[room]

    if len(room_info['players']) < 2:
        room_info['players'].append({'id': request.sid, 'name': player_name})
        join_room(room)
        emit('connection_success', {'message': f'{player_name} joined room {room}', 'player_count': len(room_info['players'])}, room=room)
        emit('update_player_count', {'player_count': len(room_info['players'])}, room=room)

        if len(room_info['players']) == 2:
            emit('start_game', room_info['game_state'], room=room)
    else:
        emit('room_full', {'message': 'Room is full'}, room=request.sid)

@socketio.on('pause_game')
def handle_pause_game(data):
    room = data['room']
    room_info = rooms[room]
    room_info['game_paused'] = True

    player_name = [p['name'] for p in room_info['players'] if p['id'] == request.sid][0]
    emit('game_paused', {'message': f'Game paused by {player_name}'}, room=room)

@socketio.on('resume_game')
def handle_resume_game(data):
    room = data['room']
    room_info = rooms[room]
    
    if room_info.get('game_paused'):
        room_info['game_paused'] = False
        emit('game_resumed', room=room)

@socketio.on('quit_game')
def handle_quit_game(data):
    room = data['room']
    player_name = [p['name'] for p in rooms[room]['players'] if p['id'] == request.sid][0]

    room_info = rooms[room]
    room_info['players'] = [p for p in room_info['players'] if p['id'] != request.sid]
    
    emit('player_quit', {'message': f'{player_name} has quit the game'}, room=room)
    emit('update_player_count', {'player_count': len(room_info['players'])}, room=room)

    if len(room_info['players']) == 0:
        del rooms[room]

@socketio.on('disconnect')
def handle_disconnect():
    for room, room_info in rooms.items():
        players = room_info['players']
        for player in players:
            if player['id'] == request.sid:
                player_name = player['name']
                players.remove(player)
                emit('update_player_count', {'player_count': len(players)}, room=room)
                emit('player_disconnected', {'message': f'{player_name} left the room', 'player_count': len(players)}, room=room)
                if len(players) == 0:
                    del rooms[room]
                break

def check_game_over(game_state):
    for row in game_state:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    for col in range(len(game_state[0])):
        check = [row[col] for row in game_state]
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return check[0]

    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != ' ':
        return game_state[0][0]
    if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != ' ':
        return game_state[0][2]

    if all(cell != ' ' for row in game_state for cell in row):
        return 'draw'

    return None

if __name__ == '__main__':
    socketio.run(app, debug=True)

