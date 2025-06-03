const socket = io("http://localhost:5000");
const params = new URLSearchParams(location.search);
const username = params.get("username") || "Guest";
const room = "general";

socket.emit('join', { room, username });

socket.on('message', data => {
  const chatBox = document.getElementById('chat-box');
  chatBox.innerHTML += `<p><strong>${data.user}:</strong> ${data.text}</p>`;
});

socket.on('notification', msg => {
  const chatBox = document.getElementById('chat-box');
  chatBox.innerHTML += `<p><em>${msg}</em></p>`;
});

// Function to send a message
function sendMessage() {
  const msgInput = document.getElementById('message');
  const msg = msgInput.value.trim(); // Trim whitespace

  if (msg === "") {
    alert("Message cannot be blank!"); // Alert for empty message
    return;
  }

  socket.emit('message', { room, username, message: msg });
  msgInput.value = ''; 
}

// Function to handle Enter key press
document.getElementById('message').addEventListener('keypress', function(event) {
  if (event.key === 'Enter') {
    sendMessage(); // Call sendMessage function on Enter key press
    event.preventDefault(); // Prevent default action (form submission)
  }
});


function checkPassword(password) {
  const correctPassword = "yourPassword"; // Replace with your actual password
  if (password !== correctPassword) {
    socket.emit('notification', "Password is incorrect!"); // Notify user
  }
}
