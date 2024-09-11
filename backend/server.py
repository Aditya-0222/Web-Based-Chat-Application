from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from cryptography.fernet import Fernet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_app.db'
db = SQLAlchemy(app)
socketio = SocketIO(app)

# Encryption key (Change this key for production use)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)

# Initialize Database with app context
with app.app_context():
    db.create_all()

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=data['username'], password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password):
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

# SocketIO Events
@socketio.on('message')
def handle_message(data):
    encrypted_message = cipher_suite.encrypt(data['message'].encode('utf-8'))
    new_message = Message(user_id=data['user_id'], content=encrypted_message.decode('utf-8'))
    db.session.add(new_message)
    db.session.commit()
    emit('message', {'user': data['user'], 'message': data['message']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

