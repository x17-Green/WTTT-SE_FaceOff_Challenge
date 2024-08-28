"""Main Flask App"""

from flask import Flask
from flask_pymongo import PyMongo

# Initialize the Flask application
app = Flask(__name__)
app.url_map.strict_slashes = False

# Configuration (adjust to your setup)
app.config["MONGO_URI"] = "mongodb://localhost:27017/tictactoe_db"

# Initialize PyMongo
mongo = PyMongo(app)

# Register Blueprints
from routes.player_routes import player_bp
from routes.game_routes import game_bp

app.register_blueprint(player_bp, url_prefix='/player')
app.register_blueprint(game_bp, url_prefix='/game')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
