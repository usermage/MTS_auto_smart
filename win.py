from tkinter import *
from PIL import ImageTk, Image
from threading import Thread
import time

root = Tk()
root.geometry('1000x1000')
canvas = Canvas(root,width=999,height=999)
canvas.pack()

def prescript(num):
    time.sleep(3000)
    global canvas
    pilImage = Image.open("../../../Downloads/cats3.jpg.jpg")
    image = ImageTk.PhotoImage(pilImage)
    canvas.image = image
                    
thread1 = Thread(target=prescript, args=(200,))
thread1.start()

pilImage = Image.open("../../../Downloads/irochka.jpg")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(400,400,image=image)
root.mainloop()