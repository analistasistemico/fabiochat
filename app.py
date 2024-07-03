from flask import Flask, render_template, request 
from flask_socketio import SocketIO, emit

app = Flask(name) app.config['SECRET_KEY'] = 'your_secret_key' socketio = SocketIO(app)

# Dicionário para armazenar o histórico de mensagens por idioma
message_history = {
    'pt-BR': [],
    'en-US': [],
    'es-ES': []
}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

@socketio.on('join')
def handle_join(data):
    language = data['language']
    username = data['username']
    print(f'{username} entrou na sala ({language})')
    emit('join_message', f'{username} entrou na sala', broadcast=True)
    emit('history', message_history[language], room=request.sid)

@socketio.on('message')
 handle_message(data):
    language = data['language']
    username = data['username']
    message = data['message']
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    print(f'{username}: {message} ({language}) - {timestamp}')
    
    # Traduzir a mensagem para todos os idiomas
    translated_messages = {}
    for lang in message_history.keys():
        translated_message = translate_text(message, language, lang)
        translated_messages[lang] = f'{username}: {translated_message} - {timestamp}'
    
    # Adicionar a mensagem ao histórico e emitir para todos os clientes
    for lang, msg in translated_messages.items():
        message_history[lang].append(msg)
        emit('message', msg, room=lang)

    save_message_history()

if __name__ == '__main__':
    socketio.run(app)
