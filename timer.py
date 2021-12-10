import tkinter,sys,time
from tkinter import *
root = Tk()
root.minsize(200, 50)

LabelT=tkinter.Label(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
LabelT.pack()
def trickit():
    currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    LabelT.config(text=currentTime)
    root.update()
    LabelT.after(100, trickit)
    
LabelT.after(100, trickit)

canvas = Canvas(root)
canvas.config(width=300, height=50)
canvas.pack()
time2 = 36000
def tick():
    global time2
    canvas.delete(ALL)
    time2 -= 1
    canvas.create_text(150, 20, text=time2)
    if time2 != 0:
        canvas.after(100, tick)

canvas.after(1, tick)

root.mainloop()
