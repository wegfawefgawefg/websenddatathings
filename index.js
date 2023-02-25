var ws = new WebSocket("ws://localhost:8000/ws");

ws.onmessage = function (event) {
  j = JSON.parse(event.data);

  var xp = document.getElementById("data");
  xp.innerText = `data: ${JSON.stringify(j)}`;
};

function sendMessage(event) {
  var input = document.getElementById("messageText");
  ws.send(input.value);
  input.value = "";
  event.preventDefault();
}
