from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, leave_room, emit

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
        # Initialize room with players and game_state
        rooms[room] = {
            'players': [],
            'game_state': [[' ' for _ in range(3)] for _ in range(3)]
        }
    
    room_info = rooms[room]

    if len(room_info['players']) < 2:
        room_info['players'].append({'id': request.sid, 'name': player_name})
        join_room(room)
        emit('connection_success', {'message': f'{player_name} joined room {room}', 'player_count': len(room_info['players'])}, room=room)
        emit('update_player_count', {'player_count': len(room_info['players'])}, room=room)

        if len(room_info['players']) == 2:
            # Notify both players that the game is ready to start
            emit('game_ready', room=room)
    else:
        emit('room_full', {'message': 'Room is full'}, room=request.sid)


@socketio.on('start_game')
def handle_start_game(data):
    room = data['room']
    room_info = rooms.get(room)

    if room_info and len(room_info['players']) == 2:
        # Start the game and notify both players
        emit('start_game', room_info['game_state'], room=room)


@socketio.on('make_move')
def handle_make_move(data):
    room = data['room']
    move = data['move']

    room_info = rooms[room]
    game_state = room_info['game_state']

    # Determine player symbol based on the socket ID
    symbol = 'X' if room_info['players'][0]['id'] == request.sid else 'O'

    # Update the game state based on the move
    game_state[move['row']][move['col']] = symbol

    emit('update_board', {'board': game_state}, room=room)

    # Check for game over
    winner = check_game_over(game_state)
    if winner:
        emit('game_over', {'winner': winner}, room=room)

def check_game_over(game_state):
    # Check rows
    for row in game_state:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    # Check columns
    for col in range(len(game_state[0])):
        check = []
        for row in game_state:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return check[0]

    # Check diagonals
    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != ' ':
        return game_state[0][0]
    if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != ' ':
        return game_state[0][2]

    # Check for draw
    if all(cell != ' ' for row in game_state for cell in row):
        return 'draw'

    return None


@socketio.on('disconnect')
def handle_disconnect():
    for room, room_info in rooms.items():
        player_to_remove = None
        for player in room_info['players']:
            if player['id'] == request.sid:
                player_to_remove = player
                break

        if player_to_remove:
            room_info['players'].remove(player_to_remove)
            emit('player_left', {'message': f'{player_to_remove["name"]} has left the room', 'player_count': len(room_info['players'])}, room=room)
            emit('update_player_count', {'player_count': len(room_info['players'])}, room=room)

            if len(room_info['players']) == 0:
                del rooms[room]
            else:
                leave_room(room)
                emit('player_disconnected', {'message': f'{player_to_remove["name"]} left the game', 'player_count': len(room_info['players'])}, room=room)
            break

if __name__ == '__main__':
    socketio.run(app, debug=True)
