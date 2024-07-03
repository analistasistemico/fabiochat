from flask import Flask, render_template, request from flask_socketio import SocketIO, emit

app = Flask(name) app.config['SECRET_KEY'] = 'your_secret_key' socketio = SocketIO(app)
