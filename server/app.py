from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_sqlalchemy import SQLAlchemy
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tictactoe.db'
socketio = SocketIO(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)

class Game(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    player_x = db.Column(db.String(50), db.ForeignKey('user.username'))
    player_o = db.Column(db.String(50), db.ForeignKey('user.username'))
    board_state = db.Column(db.String(9), default=' ' * 9)
    current_turn = db.Column(db.String(1), default='X')

# Create tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('game.html')

@socketio.on('join_game')
def on_join_game(data):
    username = data['username']
    room = data['room']
    join_room(room)

    game = Game.query.filter_by(id=room).first()
    if not game:
        
        # Create a new game room
        new_game = Game(id=room, player_x=username, board_state=' ' * 9, current_turn='X')
        db.session.add(new_game)
        db.session.commit()
        emit('waiting_for_player', {'message': 'Waiting for another player to join...'}, room=room)
    else:
        # If player O is not assigned yet
        if game.player_o is None:
            game.player_o = username
            db.session.commit()
            emit('start_game', {
                'message': 'Game started! Player X goes first.',
                'current_turn': game.current_turn,
                'player_x': game.player_x,
                'player_o': game.player_o
            }, room=room)
        else:
            emit('room_full', {'message': 'Room is full!'}, room=room)

@socketio.on('make_move')
def on_make_move(data):
    room = data['room']
    index = data['index']
    current_player = data['player']

    game = Game.query.filter_by(id=room).first()
    if game and game.current_turn == current_player:
        board = list(game.board_state)
        board[int(index)] = current_player
        game.board_state = ''.join(board)
        game.current_turn = 'O' if current_player == 'X' else 'X'
        db.session.commit()

        emit('update_board', {'board': game.board_state, 'next_turn': game.current_turn}, room=room)

        if check_win(game.board_state, current_player):
            emit('game_over', {'message': f'Player {current_player} wins!'}, room=room)
            update_stats(current_player, winner=True)
        elif ' ' not in game.board_state:
            emit('game_over', {'message': "It's a draw!"}, room=room)
    else:
        emit('invalid_move', {'message': 'Invalid move!'}, room=room)

def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

def update_stats(player, winner=False):
    user = User.query.filter_by(username=player).first()
    if user:
        if winner:
            user.wins += 1
        else:
            user.losses += 1
        db.session.commit()

if __name__ == '__main__':
    socketio.run(app, debug=True)
