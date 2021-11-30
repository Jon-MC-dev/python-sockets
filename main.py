from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/hola")
def hello_world():
    return "<p>Hello, Jonathan v1!</p>"

@socketio.on('message')
def handle_message(data):
    print('received message: ' + str(data))
    socketio.emit('regreso', data)

@socketio.on('numero')
def handle_numero(data):
    while(True):
        time.sleep(4)  # Sleep for 3 seconds
        numero = random.randint(0, 1)
        socketio.emit('hey', 'Hola desde el canal hey')


if __name__ == '__main__':
    socketio.run(app, port=5000)