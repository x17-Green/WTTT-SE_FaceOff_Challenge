# game routes
from flask import Blueprint, request, render_template
from utils.socketio import socketio, rooms
from models.game import Game

game_blueprint = Blueprint('game', __name__)

@game_blueprint.route('/')
def index():
    return render_template('game_index.html')

@socketio.on('join_game')
def handle_join_game(data):
    player_name = data['player']
    player_sid = request.sid  # Get the unique session ID for the player
    room = None

    # Find an available room or create a new one
    for r in rooms:
        if len(rooms[r]['players']) < 2:
            room = r
            break

    if room is None:
        room = str(random.randint(1000, 9999))
        rooms[room] = {'players': [], 'game': Game()}
    
    rooms[room]['players'].append(player_sid)
    join_room(room)

    if len(rooms[room]['players']) == 2:
        initial_turn = 'X' if rooms[room]['players'][0] == player_sid else 'O'
        rooms[room]['game'].turn = initial_turn

        emit('game_start', {
            'room': room,
            'players': rooms[room]['players'],
            'turn': rooms[room]['game'].turn
        }, room=room)
    else:
        emit('waiting_for_opponent', {'message': 'Waiting for opponent...'}, room=room)

@socketio.on('make_move')
def handle_make_move(data):
    room = data['room']
    index = int(data['index'])  # Convert index to integer
    player = data['player']

    # Check if the room exists and the index is valid
    if room not in rooms or index < 0 or index >= len(rooms[room]['game'].board):
        return  # Optionally, you can send an error message back to the client

    # Make the move
    if rooms[room]['game'].make_move(index, player):
        # Debugging output
        print(f"Move made by {player} at index {index}")
        print(f"Board state: {rooms[room]['game'].board}")

        # Check for game over conditions (win or draw)
        winner = rooms[room]['game'].check_winner()
        if winner:
            print(f"Game over! Winner: {winner}")
            emit('game_over', {'winner': winner}, room=room)
            del rooms[room]
        elif '' not in rooms[room]['game'].board:
            print("Game over! It's a draw.")
            emit('game_over', {'winner': 'Draw'}, room=room)
            del rooms[room]
        else:
            emit('move_made', {'index': index, 'player': player, 'turn': rooms[room]['game'].turn}, room=room)