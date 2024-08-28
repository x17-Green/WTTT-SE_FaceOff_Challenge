"""Game Model and Routes"""
from flask import jsonify, request, Blueprint
from bson.objectid import ObjectId
from datetime import datetime


game_bp = Blueprint('game', __name__)

@game_bp.route('/start_game', methods=['POST'])
def start_game():
    
    player1_id = request.json.get('player1_id')
    if player1_id is None:
        return jsonify({"error": "Player 1 ID is required!"}), 400

    player2_id = request.json.get('player2_id')  # Optional for computer opponent
    difficulty = request.json.get('difficulty')  # Optional, used if playing against computer

    from app import mongo
    games = mongo.db.games
    users = mongo.db.users

    # Create a new game document
    game_id = games.insert_one({
        "player1_id": ObjectId(player1_id),
        "player2_id": ObjectId(player2_id) if player2_id else None,  # None if playing against the computer
        "winner_id": None,  # Gets updated when game ends
        "timestamp": datetime.now(), # Can be changed to local time if needed
        "difficulty": difficulty if player2_id is None else None  # Only relevant if playing against the computer
    }).inserted_id

    return jsonify({"message": "Game started!", "game_id": str(game_id)}), 201

@game_bp.route('/end_game/<game_id>', methods=['POST'])
def end_game(game_id):
    winner_id = request.json.get('winner_id')  # ID of the winner, or None for a draw

    from app import mongo
    games = mongo.db.games
    users = mongo.db.users
    game = games.find_one({"_id": ObjectId(game_id)})
    
    if game is None:
        return jsonify({"error": "Game not found!"}), 404
    player1_id = game.get('player1_id')
    player2_id = game.get('player2_id')

    if winner_id is None:
        for player in [player1_id, player2_id]:
            if player:
                games_played = users.find_one({"_id": ObjectId(player)})['games_played']
                if game_id not in games_played:
                    users.update_one({"_id": ObjectId(player)}, {"$inc": {"games_drawn": 1}})

        return jsonify({"message": "Game ended in a draw!"}), 200

    # Update the game document with the winner
    games.update_one(
        {"_id": ObjectId(game_id)},
        {"$set": {"winner_id": ObjectId(winner_id) if winner_id else None}}
    )
    # Update the winner's games_won field
    users.update_one({"_id": ObjectId(winner_id)}, {"$inc": {"games_won": 1}})
    if player2_id != winner_id:
        users.update_one({"_id": ObjectId(player2_id)}, {"$inc": {"games_lost": 1}})
    else:
        users.update_one({"_id": ObjectId(player1_id)}, {"$inc": {"games_lost": 1}})
    
    # Update the games_played field in users collection for both players
    users.update_one({"_id": ObjectId(player1_id)}, {"$push": {"games_played": game_id}})
    if player2_id:
        users.update_one({"_id": ObjectId(player2_id)}, {"$push": {"games_played": game_id}})

    return jsonify({"message": "Game ended!", "winner_id": str(winner_id)}), 200

@game_bp.route('/get_game/<game_id>', methods=['GET'])
def get_game(game_id):
    from app import mongo
    games = mongo.db.games

    game = games.find_one({"_id": ObjectId(game_id)})
    if game:
        game['_id'] = str(game['_id'])
        game['player1_id'] = str(game['player1_id'])
        game['player2_id'] = str(game['player2_id']) if game['player2_id'] else None
        # Can be used to check who won, if None is returned then the game is a draw
        game['winner_id'] = str(game['winner_id']) if game['winner_id'] else None
        return jsonify(game), 200
    else:
        return jsonify({"error": "Game not found!"}), 404

@game_bp.route('/get_all_games', methods=['GET'])
def get_all_games():
    from app import mongo
    games = mongo.db.games

    games_list = []
    for game in games.find():
        game['_id'] = str(game['_id'])
        game['player1_id'] = str(game['player1_id'])
        game['player2_id'] = str(game['player2_id']) if game['player2_id'] else None
        # Can be used to check who won, if None is returned then the game is a draw
        game['winner_id'] = str(game['winner_id']) if game['winner_id'] else None
        games_list.append(game)

    return jsonify(games_list), 200