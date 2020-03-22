from threading import Thread
import time
import socket
import requests

root = Tk()
root.geometry('1000x1000')
canvas = Canvas(root,width=999,height=999)
canvas.pack()

def kek():
    return b"mek"
    
def stolen_car():
    print('Кажется, вашу машину угнали!')
    global canvas
    pilImage = Image.open("../../../Downloads/use1.jpg")
    image = ImageTk.PhotoImage(pilImage)
    canvas.image = image
    return b'ok'
	
def Diagnostik():
	print('Пришли результаты диагностики')
    global canvas
    pilImage = Image.open("../../../Downloads/use1.jpg")
    image = ImageTk.PhotoImage(pilImage)
    canvas.image = image
	return b'Diagnostik'
	
def Car_safety_results():
	print('Результаты диагностики системы безопасности')
	return b'Safety Diagnostik'
	
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
                if data == 'stolen_car':
                    conn.sendall(stolen_car())
                    
thread1 = Thread(target=prescript, args=(200,))
thread1.start()

#Запрос к МТС
def getr(command):
    x = requests.get('http://127.0.0.1:5000/2/'+command)
    return x.text

def whereavto():
    print(getr('whereavto'))
    
    
pilImage = Image.open("../../../Downloads/start.jpg")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
root.mainloop()
	 
     
if __name__=='__main__':
    while True:
        print("Введите запрос:")
        i = int(input())
        
        if i == 1:
            whereavto()
        
        if i==0:
            thread1.join()
            break