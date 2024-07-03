import json
import os

def save_message_history():
  """ 
  Salva o histórico de mensagens em arquivos JSON.
  """ 
  for lang, messages in message_history.items():
    file_path = f'message_history_{lang}.json'
    with open(file_path, 'w', encoding='utf-8') as f: 
      json.dump(messages, f, ensure_ascii=False, indent=2)
# Chamar a função sempre que uma nova mensagem for adicionada ao histórico
@socketio.on('message')
def handle_message(data):
    # Código anterior para lidar com a mensagem
    save_message_history()
