from tkinter import *
from modules.countdown.boundaries.B_GUI import B_GUI as CountdownGUI
from modules.countdown.const.CountdownStatus import CountdownStatus
from modules.countdown.control.C_Control import C_Control as CountdownControl
from modules.GUI import GUI
from modules.countdown.entities.E_CountdownWatch import E_CountdownWatch
from modules.countdown.entities.E_Input import E_Input
from modules.countdown.entities.E_Watch import E_Watch
from modules.countdown.services.S_Listener import S_Listener
from modules.countdown.services.S_Speaker import S_Speaker
from PIL import ImageTk,Image

root = Tk()

root.geometry('320x569')
root.title("Stopwatch")

#setting background
image=Image.open("stopwatch.jpg")
tkImage= ImageTk.PhotoImage(image)

Label(root,image=tkImage).place(x=-2,y=0)

frame=Frame(root,width=320, height=160,bg='#0e1013')
frame.pack(expand=True)
root.resizable(False, False)

eInput=E_Input()
eWatch=E_CountdownWatch(CountdownStatus.SILENCE)
sListener=S_Listener(eInput)
sSpeaker=S_Speaker()

countdownGUI = CountdownGUI(root,frame,eWatch)
mainGUI = GUI(root,countdownGUI)

countdownControl = CountdownControl(mainGUI,sListener,sSpeaker,eInput,eWatch)
countdownControl.process()

