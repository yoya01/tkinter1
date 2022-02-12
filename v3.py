from tkinter import *
tk = Tk()

canvas = Canvas(tk, width= 1000, height= 1000)
canvas.pack()

def drawline(canvas,x1,y1,x2,y2,width,color):
    canvas.create_line(x1,y1,x2,y2,width=width,fill=color)

def drawcircle(canvas,x1,y1,r,width,outlinecolor,color):
    canvas.create_oval(x1,y1,x1+(2*r),y1+(2*r),fill=color,outline=outlinecolor,width=width)


