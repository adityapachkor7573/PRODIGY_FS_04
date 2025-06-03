
# 💬 Chat Application

A real-time chat application built using Flask, Flask-SocketIO, and MongoDB. This application allows users to register, log in, join chat rooms, send messages, and share multimedia files. It also includes features like chat history, user presence indicators, and notifications.

## ✨ Features

- ✅ **User Authentication**: Secure user registration and login using hashed passwords.
- ✅ **Real-time Messaging**: Instant message delivery using WebSockets (Socket.IO).
- ✅ **Chat History**: View all past messages from any room.
- ✅ **User Presence Indicators**: See who is online in real-time.
- ✅ **Notifications**: Receive alerts when users join or leave a room.
- ✅ **Multimedia File Sharing**: Upload and share files (optional—pending implementation).

## 🛠 Technologies Used

- 💻 **Backend**: Flask, Flask-SocketIO, Flask-CORS, bcrypt.
- 🗄 **Database**: MongoDB (NoSQL).
- 🌐 **Frontend**: HTML, CSS, JavaScript.
- 📡 **WebSocket**: Socket.IO.

## 🚀 Installation & Setup

1. **Clone the repository**:
   <!--
   git clone https://github.com/yourusername/chat-app.git](https://github.com/adityapachkor7573/PRODIGY_FS_04.git
   cd chat-app/backend
   -->

2. **Create and activate a virtual environment**:
   <!--
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate          # Windows
   -->

3. **Install Python dependencies**:
   <!--
   pip install flask flask-socketio flask-cors pymongo bcrypt
    -->

   Optional: Create a `requirements.txt` file:
   <!-- 
   txt
   flask
   flask-socketio
   flask-cors
   pymongo
   bcrypt
   -->

## 🗃 MongoDB Setup

Ensure MongoDB is installed and running.

**Default MongoDB URI**:
<!--
mongodb://localhost:27017
 -->

**Example database connection (backend/database.py)**:
<!--
python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.chatapp
-->

**Collections**:
- `users` — Stores registered users.
- `messages` — Stores messages by room.

To run MongoDB locally:
<!-- 
mongod
 -->

## ⚙️ Run the Application

Start the MongoDB server first, then:
<!-- 
python app.py
 -->

The app will be available at:
<!-- 
http://localhost:5000 
-->


## 📡 WebSocket Events

| Event        | Description               |
|--------------|---------------------------|
| `connect`    | When a user connects      |
| `join`       | Join a room               |
| `leave`      | Leave a room              |
| `message`    | Send message to a room    |
| `disconnect` | When a user disconnects   |

## 🔌 REST API Endpoints

| Method | Endpoint           | Description               |
|--------|--------------------|---------------------------|
| POST   | `/register`        | Register a new user       |
| POST   | `/login`           | Authenticate user         |
| GET    | `/history/<room>`  | Get chat history          |

## 📁 Project Structure

chat-app/
├── backend/
│   ├── app.py              
│   ├── database.py         
│   └── README.md           
├── frontend/               

## 👨‍💻 Author

Made with ❤️ by Aditya Pachkor
