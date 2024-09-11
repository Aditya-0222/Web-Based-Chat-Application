const socket = io('http://localhost:5000');  // Update URL if deploying to a different server

const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatWindow = document.getElementById('chat-window');

sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message) {
        socket.emit('message', { message: message, user: 'User', user_id: 1 }); // Adjust user_id as needed
        messageInput.value = '';
    }
});

socket.on('message', (data) => {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${data.user}: ${data.message}`;
    chatWindow.appendChild(messageElement);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Auto scroll to bottom
});
