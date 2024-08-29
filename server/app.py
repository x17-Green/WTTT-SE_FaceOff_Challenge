# from flask import Flask, render_template, request, session
# from flask_socketio import SocketIO, join_room, leave_room, emit
# from flask_sqlalchemy import SQLAlchemy
# import random
# import string

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tictactoe.db'
# socketio = SocketIO(app)
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(50), unique=True, nullable=False)
#     wins = db.Column(db.Integer, default=0)
#     losses = db.Column(db.Integer, default=0)

# class Game(db.Model):
#     id = db.Column(db.String(8), primary_key=True)
#     player_x = db.Column(db.String(50), db.ForeignKey('user.username'))
#     player_o = db.Column(db.String(50), db.ForeignKey('user.username'))
#     board_state = db.Column(db.String(9), default=' ' * 9)
#     current_turn = db.Column(db.String(1), default='X')

# # Create tables
# with app.app_context():
#     db.create_all()

# @app.route('/')
# def index():
#     return render_template('game.html')

# @socketio.on('join_game')
# def on_join_game(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)

#     game = Game.query.filter_by(id=room).first()
#     if not game:
        
#         # Create a new game room
#         new_game = Game(id=room, player_x=username, board_state=' ' * 9, current_turn='X')
#         db.session.add(new_game)
#         db.session.commit()
#         emit('waiting_for_player', {'message': 'Waiting for another player to join...'}, room=room)
#     else:
#         # If player O is not assigned yet
#         if game.player_o is None:
#             game.player_o = username
#             db.session.commit()
#             emit('start_game', {
#                 'message': 'Game started! Player X goes first.',
#                 'current_turn': game.current_turn,
#                 'player_x': game.player_x,
#                 'player_o': game.player_o
#             }, room=room)
#         else:
#             emit('room_full', {'message': 'Room is full!'}, room=room)

# @socketio.on('make_move')
# def on_make_move(data):
#     room = data['room']
#     index = data['index']
#     current_player = data['player']

#     game = Game.query.filter_by(id=room).first()
#     if game and game.current_turn == current_player:
#         board = list(game.board_state)
#         board[int(index)] = current_player
#         game.board_state = ''.join(board)
#         game.current_turn = 'O' if current_player == 'X' else 'X'
#         db.session.commit()

#         emit('update_board', {'board': game.board_state, 'next_turn': game.current_turn}, room=room)

#         if check_win(game.board_state, current_player):
#             emit('game_over', {'message': f'Player {current_player} wins!'}, room=room)
#             update_stats(current_player, winner=True)
#         elif ' ' not in game.board_state:
#             emit('game_over', {'message': "It's a draw!"}, room=room)
#     else:
#         emit('invalid_move', {'message': 'Invalid move!'}, room=room)

# def check_win(board, player):
#     winning_combinations = [
#         [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#         [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#         [0, 4, 8], [2, 4, 6]             # Diagonals
#     ]
#     for combo in winning_combinations:
#         if all(board[i] == player for i in combo):
#             return True
#     return False

# def update_stats(player, winner=False):
#     user = User.query.filter_by(username=player).first()
#     if user:
#         if winner:
#             user.wins += 1
#         else:
#             user.losses += 1
#         db.session.commit()

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

##################################################
# #app.py
# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, join_room, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# rooms = {}

# @app.route('/')
# def index():
#     return render_template('index.html')


# @socketio.on('join_game')
# def handle_join_game(data):
#     room = data['room']
#     player_name = data['playerName']

#     if room not in rooms:
#         # Initialize room with players and game_state
#         rooms[room] = {
#             'players': [],
#             'game_state': [[' ' for _ in range(3)] for _ in range(3)]
#         }
    
#     room_info = rooms[room]

#     if len(room_info['players']) < 2:
#         room_info['players'].append({'id': request.sid, 'name': player_name})
#         join_room(room)
#         emit('connection_success', {'message': f'{player_name} joined room {room}', 'player_count': len(room_info['players'])}, room=room)
#         emit('update_player_count', {'player_count': len(room_info['players'])}, room=room)

#         if len(room_info['players']) == 2:
#             # Start the game when two players have joined
#             emit('start_game', room_info['game_state'], room=room)
#     else:
#         emit('room_full', {'message': 'Room is full'}, room=request.sid)

# @socketio.on('make_move')
# def handle_make_move(data):
#     room = data['room']
#     move = data['move']

#     room_info = rooms[room]
#     game_state = room_info['game_state']

#     # Determine player symbol based on the socket ID
#     symbol = 'X' if room_info['players'][0]['id'] == request.sid else 'O'

#     # Update the game state based on the move
#     game_state[move['row']][move['col']] = symbol

#     emit('update_board', {'board': game_state}, room=room)

#     # Check for game over
#     winner = check_game_over(game_state)
#     if winner:
#         emit('game_over', {'winner': winner}, room=room)

# def check_game_over(game_state):
#     # Check rows
#     for row in game_state:
#         if row.count(row[0]) == len(row) and row[0] != ' ':
#             return row[0]

#     # Check columns
#     for col in range(len(game_state[0])):
#         check = []
#         for row in game_state:
#             check.append(row[col])
#         if check.count(check[0]) == len(check) and check[0] != ' ':
#             return check[0]

#     # Check diagonals
#     if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != ' ':
#         return game_state[0][0]
#     if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != ' ':
#         return game_state[0][2]

#     # Check for draw
#     if all(cell != ' ' for row in game_state for cell in row):
#         return 'draw'

#     return None


# @socketio.on('disconnect')
# def handle_disconnect():
#     for room, players in rooms.items():
#         if request.sid in players:
#             players.remove(request.sid)
#             emit('update_player_count', {'player_count': len(players)}, room=room)
#             if len(players) == 0:
#                 del rooms[room]
#             else:
#                 emit('player_disconnected', {'message': f'A player left the room', 'player_count': len(players)}, room=room)
#             break

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

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
            'game_state': [[' ' for _ in range(3)] for _ in range(3)]
        }

    room_info = rooms[room]

    if len(room_info['players']) < 2:
        room_info['players'].append({'id': request.sid, 'name': player_name})
        join_room(room)
        emit('connection_success', {'message': f'{player_name} joined room {room}', 'player_count': len(room_info['players'])}, room=room)

        if len(room_info['players']) == 2:
            emit('start_game', room=room)
    else:
        emit('room_full', {'message': 'Room is full'}, room=request.sid)


@socketio.on('start_game')
def handle_start_game():
    emit('start_game', room=request.sid)


@socketio.on('make_move')
def handle_make_move(data):
    room = data['room']
    move = data['move']

    room_info = rooms[room]
    game_state = room_info['game_state']

    symbol = 'X' if room_info['players'][0]['id'] == request.sid else 'O'
    game_state[move['row']][move['col']] = symbol

    emit('update_board', {'board': game_state}, room=room)

    winner = check_game_over(game_state)
    if winner:
        emit('game_over', {'winner': winner}, room=room)


def check_game_over(game_state):
    for row in game_state:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return row[0]

    for col in range(len(game_state[0])):
        check = []
        for row in game_state:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != ' ':
            return check[0]

    if game_state[0][0] == game_state[1][1] == game_state[2][2] and game_state[0][0] != ' ':
        return game_state[0][0]
    if game_state[0][2] == game_state[1][1] == game_state[2][0] and game_state[0][2] != ' ':
        return game_state[0][2]

    if all(cell != ' ' for row in game_state for cell in row):
        return 'draw'

    return None


@socketio.on('disconnect')
def handle_disconnect():
    for room, room_info in rooms.items():
        players = room_info['players']
        player = next((p for p in players if p['id'] == request.sid), None)
        if player:
            players.remove(player)
            emit('update_player_count', {'player_count': len(players)}, room=room)
            if len(players) == 0:
                del rooms[room]
            else:
                emit('player_disconnected', {'message': f'{player["name"]} left the room', 'player_count': len(players)}, room=room)
            break


if __name__ == '__main__':
    socketio.run(app, debug=True)
