from threading import Thread
import time
import socket

from flask import Flask
app = Flask(__name__)

port_user = 12388
port_auto = 12377

@app.route("/<int:who>/<mess>", methods=['GET'])
def index(who, mess):
    global port_user, port_auto
    if who == 1: #auto
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('127.0.0.1', port_user))
            s.sendall(mess.encode())
            data = s.recv(1024)
            print("МТС:", data)
        return data
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
            s.connect(('127.0.0.1', port_auto))
            s.sendall(mess.encode())
            data = s.recv(1024)
            print("МТС:", data)
        return data
    return str(what) + str(command) + str(s)#f"{} {} {}".(what, command, s)
    
app.run()