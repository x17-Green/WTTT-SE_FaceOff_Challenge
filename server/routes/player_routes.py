"""Player Model and Routes"""
from flask import jsonify, request, Blueprint
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

player_bp = Blueprint('player', __name__)

@player_bp.route('/register', methods=['POST'])
def register_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    confirmPassword = request.json['confirmPassword']
    
    if username is None:
        return jsonify({"error": "Username is required!"}), 400
    
    if email is None:
        return jsonify({"error": "Email is required!"}), 400
    
    if password is None:
        return jsonify({"error": "Password is required!"}), 400
    
    if confirmPassword is None:
        return jsonify({"error": "Password confirmation is required!"}), 400
    
    from app import mongo
    users = mongo.db.users

    if users.find_one({"email": email}):
        return jsonify({"error": "Player already exists!"}), 400
    
    if password != confirmPassword:
        return jsonify({"error": "Passwords do not match!"}), 400

    hashed_password = generate_password_hash(password)
    user_id = users.insert_one({
        "username": username,
        "email": email,
        "password_hash": hashed_password,
        "games_won": 0,
        "games_lost": 0,
        "games_drawn": 0,
        "games_played": []
    }).inserted_id

    return jsonify({"message": "Player registered!", "user_id": str(user_id)}), 201

@player_bp.route('/login', methods=['POST'])
def login_user():
    email = request.json['email']
    password = request.json['password']

    from app import mongo
    users = mongo.db.users    

    user = users.find_one({"email": email})
    if user and check_password_hash(user['password_hash'], password):
        return jsonify({"message": "Login successful!", "user_id": str(user['_id'])}), 200
    else:
        return jsonify({"error": "Invalid credentials!"}), 401

@player_bp.route('/get_player/<player_id>', methods=['GET'])
def get_player(player_id):
    from app import mongo
    users = mongo.db.users

    user = users.find_one({"_id": ObjectId(player_id)})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({"error": "Player not found!"}), 404

@player_bp.route('/update_player/<player_id>', methods=['POST'])
def update_player(player_id):
    from app import mongo
    users = mongo.db.users

    users.update_one({"_id": ObjectId(player_id)}, {"$set": request.json})
    return jsonify({"message": "Player updated!"}), 200

@player_bp.route('/delete_player/<player_id>', methods=['DELETE'])
def delete_player(player_id):
    from app import mongo
    users = mongo.db.users

    users.delete_one({"_id": ObjectId(player_id)})
    return jsonify({"message": "Player deleted!"}), 200