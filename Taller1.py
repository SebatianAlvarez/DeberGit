from tkinter import *

def DanielCasagallo():
    print 'Daniel Casagallo'
tk = Tk()
btn = Button(tk, text = "Daniel", command = DanielCasagallo())
btn.pack()

def JavierMaiza():
    print 'Jonathan Javier Maiza'

tk=Tk()
btn= Button (tk, text='Javier', command= JavierMaiza())
btn.pack()
btn1=Button(tk, text='Daniel', command= DanielCasagallo())
btn1.pack()


