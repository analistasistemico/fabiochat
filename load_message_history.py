def load_message_history():
  """ 
  Carrega o histórico de mensagens a partir dos arquivos JSON.
  """ 
  for lang in message_history.keys():
    file_path = f'message_history_{lang}.json' 
    if os.path.exists(file_path):
      with open(file_path, 'r', encoding='utf-8') as f:
        message_history[lang] = json.load(f) else: message_history[lang] = []
# Chamar a função quando o servidor for iniciado
if __name__ == '__main__':
    load_message_history()
    socketio.run(app)
