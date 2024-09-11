# Web Chat Application

## Table of Contents
* Introduction
* Features
* Demo
* Tech Stack
* Installation
* Usage
* API Endpoints
* Contributing
* License
* Contact
* Acknowledgments

### Introduction
Welcome to the Web Chat Application, a real-time, web-based chat platform that allows users to communicate seamlessly. Whether you're looking to create a community, collaborate with team members, or simply chat with friends, our application provides a robust and user-friendly interface to meet your needs.

### Features
Real-Time Messaging: Instant communication with low latency.
User Authentication: Secure sign-up and login using JWT.
Private and Group Chats: Create private conversations or group discussions.
Typing Indicators: See when others are typing.
Message Notifications: Receive real-time notifications for new messages.
Responsive Design: Accessible on desktops, tablets, and mobile devices.
Emoji Support: Enhance your messages with emojis.
File Sharing: Share images, documents, and other files seamlessly.
### Demo

Access the live demo here.

### Tech Stack


Frontend
* ReactJS: JavaScript library for building user interfaces.
* Redux: State management.
* Socket.io Client: Real-time communication.
* Material-UI: UI component library for React.


Backend
* Node.js: JavaScript runtime.
* Express.js: Web framework for Node.js.
* Socket.io: Real-time communication.
* MongoDB: NoSQL database.
* Mongoose: MongoDB object modeling.


Tools & Platforms
* Git & GitHub: Version control and repository hosting.
* Heroku/Vercel: Deployment platforms.
* Postman: API testing.


Installation
* Prerequisites
* Node.js and npm installed on your machine.
* MongoDB installed or access to a MongoDB Atlas cluster.

### Steps

1. Clone the Repository
   git clone https://github.com/your-username/web-chat-application.git
cd web-chat-application

2. Install Backend Dependencies
   cd backend
   npm install

3. Configure Environment Variables
   Create a .env file in the backend directory and add the following:
   PORT=5000
   MONGODB_URI=your_mongodb_connection_string
   JWT_SECRET=your_jwt_secret

4. Start the Backend Server
   npm start

5. Install Frontend Dependencies
   Open a new terminal window and navigate to the frontend directory:
   cd frontend
   npm install

6. Configure Frontend Environment Variables
   Create a .env file in the frontend directory and add the following:
   REACT_APP_API_URL=http://localhost:5000

7. Start the Frontend Development Server
   npm start

8. Access the Application
   Open your browser and navigate to http://localhost:3000.

### Usage
1. Sign Up / Log In

Create a new account or log in with existing credentials.

2. Create or Join a Chat
* Private Chat: Search for a user and start a conversation.
* Group Chat: Create a new group and invite members.

3. Start Messaging
   Send and receive messages in real-time. Use emojis, share files, and enjoy seamless communication.

## API Endpoints
Authentication
* POST /api/auth/register
  Register a new user.

* POST /api/auth/login
  Authenticate a user and return a JWT.

Users
* GET /api/users
  Retrieve a list of users.

* GET /api/users/:id
  Get user details by ID.

Chats
* GET /api/chats
  Retrieve all chats for the authenticated user.

* POST /api/chats
  Create a new chat.

Messages
* GET /api/messages/:chatId
  Retrieve messages for a specific chat.

* POST /api/messages
  Send a new message.

### Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project

2. Create your Feature Branch
   git checkout -b feature/AmazingFeature

3. Commit your Changes
  git commit -m 'Add some AmazingFeature'

4. Push to the Branch
   git push origin feature/AmazingFeature
   
5. Open a Pull Request

### License

Distributed under the MIT License. See LICENSE for more information.

## Contact
    Aditya Thakur
    adityathakur6626@gmail.com






