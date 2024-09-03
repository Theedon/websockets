from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

from utils.capitalize import capitalizeMessage

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <button onclick="callHelloRoute()">Say Hello</button>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
            function callHelloRoute() {
                fetch('/hello')
                    .then(response => response.text())
                    .then(data => {
                        var messages = document.getElementById('messages')
                        var message = document.createElement('li')
                        var content = document.createTextNode(data)
                        message.appendChild(content)
                        messages.appendChild(message)
                    });
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        updated_data = capitalizeMessage(data)
        await websocket.send_text(
            f"Message text converted from {data} to {updated_data}"
        )
        print("the has happened")


@app.get("/hello")
async def hello_world():
    message = "hello world"
    capitalized_message = capitalizeMessage(message)
    return {"message": capitalized_message}
