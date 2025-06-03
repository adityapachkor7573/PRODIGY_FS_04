# database.py

from pymongo import MongoClient

# Connect to your local MongoDB instance (as per your screenshot)
client = MongoClient("mongodb://localhost:27017/")

# Use a database named 'chat_app'
db = client['chat-app']

# Helper to find a user by username
def get_user_by_username(username):
    return db.users.find_one({'username': username})

# Helper to save chat messages to a room
def save_message(room, message):
    db.messages.insert_one({
        'room': room,
        'user': message['user'],
        'text': message['text']
    })
