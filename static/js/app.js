document.addEventListener('DOMContentLoaded', function() {
    const socket = io();
    const welcomePage = document.querySelector('.welcome-page');
    const chatRoom = document.querySelector('.chat-room');
    const languageSelect = document.getElementById('language-select');
    const usernameInput = document.getElementById('username-input');
    const messageInput = document.getElementById('message-input');
    const messageArea = document.querySelector('.message-area');
    const statusArea = document.querySelector('.status-area');

    document.getElementById('start-chat').addEventListener('click', function() {
        const language = languageSelect.value;
        const username = usernameInput.value;
        if (language && username) {
            socket.emit('join', { language, username });
            welcomePage.classList.add('hidden');
            chatRoom.classList.remove('hidden');
        }
    });

    document.getElementById('send-button').addEventListener('click', function() {
        const message = messageInput.value.trim();
        if (message) {
            const language = languageSelect.value;
            const username = usernameInput.value;
            socket.emit('message', { language, username, message });
            messageInput.value = '';
        }
    });

    socket.on('message', function(data) {
       const messageElement = document.createElement('div');
        messageElement.textContent = data;
        messageArea.appendChild(messageElement);
        messageArea.scrollTop = messageArea.scrollHeight;
    });

    socket.on('join_message', function(data) {
        const messageElement = document.createElement('div');
        messageElement.textContent = data;
        statusArea.appendChild(messageElement);
        statusArea.scrollTop = statusArea.scrollHeight;
    });

    socket.on('history', function(data) {
        data.forEach(function(message) {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            messageArea.appendChild(messageElement);
        });
        messageArea.scrollTop = messageArea.scrollHeight;
    });
});
