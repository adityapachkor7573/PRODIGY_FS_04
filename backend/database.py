from pymongo import MongoClient

# Connect to your local MongoDB database
client = MongoClient("mongodb://localhost:27017/")

# database named chat-app 
db = client['chat-app']

def get_user_by_username(username):
    return db.users.find_one({'username': username})

def save_message(room, message):
    db.messages.insert_one({
        'room': room,
        'user': message['user'],
        'text': message['text']
    })
