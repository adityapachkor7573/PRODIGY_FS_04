from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS
import bcrypt
from database import db, get_user_by_username, save_message

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# --- Authantication Routes ---
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
    if db.users.find_one({'username': username}):
        return jsonify({"error": "User already exists"}), 400
    db.users.insert_one({'username': username, 'password': password})
    return jsonify({"success": True})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = db.users.find_one({'username': data['username']})
    if user and bcrypt.checkpw(data['password'].encode(), user['password']):
        return jsonify({"success": True})
    return jsonify({"error": "Invalid credentials"}), 401

# --- WebSocket Events ---
@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('notification', f"{data['username']} has joined the room.", to=room)

@socketio.on('leave')
def handle_leave(data):
    leave_room(data['room'])
    emit('notification', f"{data['username']} has left the room.", to=data['room'])

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = {'user': data['username'], 'text': data['message']}
    save_message(room, message)  # Save to DB if needed
    emit('message', message, to=room)


# --- Main ---
if __name__ == '__main__':
    socketio.run(app, debug=True)
