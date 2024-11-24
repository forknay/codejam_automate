from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import CohereCB as Coh

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghijklmnopqrstuvwxyz!' #you should securize this key
socketio = SocketIO(app)

@socketio.on('connect')
def connect_handler():
    initial_message = "Hi! I am your Matador virtual assistant for today, how can I help you?"
    emit('my response',
         {'message': initial_message}
         )
    Coh.chat_log.append({'role': 'Chatbot', 'content': bot_response})


@socketio.on('message') #handle_message is triggered when message is emitted
def handle_message(message):
    Coh.main(message)

if __name__ == '__main__':
    socketio.run(app, host='10.121.158.137', port = 5000, allow_unsafe_werkzeug=True)