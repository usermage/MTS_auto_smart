from threading import Thread
import time
import socket

def kek():
    return b"mek"
	
def prescript(num):
    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('127.0.0.1', 12388))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                if not data:
                    break
                data = data.decode()
                if data == 'kek':
                    conn.sendall(kek())
                    
thread1 = Thread(target=prescript, args=(200,))
thread1.start()
	