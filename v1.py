from tkinter import *
tk = Tk()
canvas = Canvas()

def drawline(x1,y1,x2,y2,width,color):
    canvas.create_line(x1,y1,x2,y2,width=width,fill=color)