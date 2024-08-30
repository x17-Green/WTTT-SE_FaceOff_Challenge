
# from flask import Flask, render_template
# from flask_socketio import SocketIO

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app, cors_allowed_origins="*")

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')

# @socketio.on('make_move')
# def handle_make_move(data):
#     # Broadcast the move to all clients
#     socketio.emit('move_made', data)

# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     socketio.run(app, debug=True)


from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

rooms = {}

@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('join_game')
def handle_join_game(data):
    player_name = data['player']
    room = None

    # Find an available room or create a new one
    for r in rooms:
        if len(rooms[r]['players']) < 2:
            room = r
            break
    
    if room is None:
        room = str(random.randint(1000, 9999))
        rooms[room] = {'players': [], 'turn': 'X', 'board': ['', '', '', '', '', '', '', '', '']}
    
    rooms[room]['players'].append(player_name)
    join_room(room)

    if len(rooms[room]['players']) == 2:
        # Determine the initial turn based on the player list order
        initial_turn = 'X' if rooms[room]['players'][0] == player_name else 'O'
        rooms[room]['turn'] = initial_turn

        emit('game_start', {
            'room': room,
            'players': rooms[room]['players'],
            'turn': rooms[room]['turn']
        }, room=room)
    else:
        emit('waiting_for_opponent', {'message': 'Waiting for opponent...'}, room=room)

@socketio.on('make_move')
def handle_make_move(data):
    room = data['room']
    index = int(data['index'])  # Convert index to integer
    player = data['player']

    # Check if the room exists and the index is valid
    if room not in rooms or index < 0 or index >= len(rooms[room]['board']):
        return  # Optionally, you can send an error message back to the client

    # Check if the cell is empty and it's the player's turn
    if rooms[room]['board'][index] == '' and rooms[room]['turn'] == player:
        # Make the move
        rooms[room]['board'][index] = player
        # Check for game over conditions (win or draw)
        winner = check_winner(rooms[room]['board'])
        if winner:
            emit('game_over', {'winner': winner}, room=room)
            cleanup_room(room)
        elif '' not in rooms[room]['board']:
            emit('game_over', {'winner': 'Draw'}, room=room)
            cleanup_room(room)
        else:
            # Update the turn
            rooms[room]['turn'] = 'O' if player == 'X' else 'X'
            emit('move_made', {'index': index, 'player': player, 'turn': rooms[room]['turn']}, room=room)



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

def check_winner(board):
    # Define winning combinations
    win_combinations = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Center column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal (top-left to bottom-right)
        [2, 4, 6]   # Diagonal (top-right to bottom-left)
    ]
    for combo in win_combinations:
        if board[combo[0]] != '' and board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return None

def cleanup_room(room):
    # Remove the room from the dictionary if it's empty
    if len(rooms[room]['players']) == 0:
        del rooms[room]

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
