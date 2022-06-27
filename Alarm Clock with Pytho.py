import imp
import sys
import time
import datetime
from  tkinter import*
from  tkinter  import messagebox
from playsound import playsound
from PIL import ImageTk,  Image


def times():    
    time=input("enter the AM or PM:-")
    hour=int(input("enter the hour:-"))
    min=int(input("enter min:-"))
    sec=int(input("enter the sec:-"))     
    if time=="pm":
        hour=hour+12
        print("a")
    while True :   
            if hour==datetime.datetime.now().hour and min==datetime.datetime.now().minute and sec==datetime.datetime.now().second:  
                print("play")  
                playsound("https://zigtone.com/download/?id=2658&post=2657")
                break
   

times()
# root.mainloop()





