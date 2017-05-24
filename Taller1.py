from tkinter import *

def DanielCasagallo():
    print ('Daniel Casagallo')
tk = Tk()
btn = Button(tk, text = "Daniel", command = DanielCasagallo())
btn.pack()

def SebastianAlvarez():
    print 'Sebastian Alvarez  :v'

def JavierMaiza():
    print ('Jonathan Javier Maiza')

def BryanPerez():
    print('Bryan Perez')
    
def JoseAltamirano():
    print('Jose Altamirano')

tk=Tk()
btn= Button (tk, text='Javier', command= JavierMaiza())
btn.pack()

btn1=Button(tk, text='Daniel', command= DanielCasagallo())
btn1.pack()

btn2= Button(tk, text = "Bryan", command = BryanPerez())
btn2.pack()

btn3= Button(tk, text = "Jose Luis", command = JoseAltamirano())
btn3.pack()

btn4 = Button(tk1, text = 'Sebastian', command = SebastianAlvarez())
btn4.pack()
