# source: https://www.youtube.com/watch?v=xoeCIx4uOLo
import tkinter as Tk
from tkinter import *
from PIL import ImageTk,Image

w=Tk()
w.geometry('320x569')
w.title("Stopwatch")

#setting background
img1=Image.open("Stopwatch_bgd_resize.jpg")
img2= ImageTk.PhotoImage(img1)

Label(w,image=img2).place(x=-2,y=0)

f1=Frame(w,width=320, height=160,bg='#0e1013')
f1.pack(expand=True)
w.resizable(False, False)

#Mechenism
def time(hour, minute, second):
    l1=Label(f1, font=('Century Gothic',40),bg='#0e1013',fg='#7f7f7f',text=hour)
    l1.place(x=25 ,y=35)

    l2=Label(f1, font=('Century Gothic',40),bg='#0e1013',fg='#7f7f7f',text=':')
    l2.place(x=95 ,y=35)

    l3=Label(f1, font=('Century Gothic',40),bg='#0e1013',fg='#7f7f7f',text=minute)
    l3.place(x=125 ,y=35)

    l4=Label(f1, font=('Century Gothic',40),bg='#0e1013',fg='#7f7f7f',text=":")
    l4.place(x=200 ,y=35)

    l5=Label(f1, font=('Century Gothic',40),bg='#0e1013',fg='#7f7f7f',text=second)
    l5.place(x=225 ,y=35)

#Required labels (260)
def labels():
    l6=Label(f1, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='HOURS')
    l6.place(x=(320-260)/2 + 5 ,y=110)

    l7=Label(f1, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='MINUTES')
    l7.place(x=(320-260)/2 + 100,y=110)

    l8=Label(f1, font=('Century Gothic',10),bg='#0e1013',fg='#7f7f7f',text='SECONDS')
    l8.place(x=(320-260)/2 + 200 - 5,y=110)

Checkbutton(w, font=('Century Gothic',10), bg='#0e1013', fg='#7f7f7f', text='Speak outloud', onvalue=1, offvalue=0).place(x = 100 , y = 400 ) #,variable=ifcheck, command=speak()

time('00', '00', '30')
labels()

w.mainloop()
