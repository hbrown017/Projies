'''
Name: Harry Brown III
Program: Radio Button using Tkinter
Date:6/20/16
'''
from tkinter import *

win = Tk()

def show():
    lblsho = Label(win, text='You selected: ' + rbvalue.get())
    lblsho.pack()

rbvalue = StringVar()
rbvalue.set('Pizza')

lblhead = Label(win, text='Select a meal option:')
lblhead.pack()

rb1 = Radiobutton(win, text='Pizza', variable=rbvalue, value = 'Pizza')
rb2 = Radiobutton(win, text='Hotdog', variable=rbvalue, value = 'Hotdog')
rb3 = Radiobutton(win, text='Burger', variable=rbvalue, value = 'Burger')

rb1.pack()
rb2.pack()
rb3.pack()

btn = Button(win, text='OK', command=show)
btn.pack()

