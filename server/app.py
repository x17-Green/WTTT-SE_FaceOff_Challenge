from flask import Flask
from config.config import Config
from utils.socketio import socketio
from routes.game_routes import game_blueprint

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(game_blueprint)

if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, debug=True)
