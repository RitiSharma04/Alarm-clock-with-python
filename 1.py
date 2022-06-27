# import tkinter


# top = tkinter.Tk()

# def helloCallBack():
#    tkinter.tkMessageBox.showinfo( "Hello Python", "Hello World")

# B = tkinter.Button(top, text ="Hello", command = helloCallBack)

# B.pack()
# top.mainloop()
# from tkinter import *
# import tkinter   
      
# top = Tk()  
      
# top.geometry("200x100")  
      
# def fun():  
#     tkinter.tkMessageBox.showinfo("Hello", "Red Button clicked")  
      
      
# b1 = Button(top,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)  
      
# b2 = Button(top, text = "Blue",activeforeground = "blue",activebackground = "pink",pady=10)  
      
# b3 = Button(top, text = "Green",activeforeground = "green",activebackground = "pink",pady = 10)  
      
# b4 = Button(top, text = "Yellow",activeforeground = "yellow",activebackground = "pink",pady = 10)  
      
# b1.pack(side = LEFT)  
      
# b2.pack(side = RIGHT)  
      
# b3.pack(side = TOP)  
      
# b4.pack(side = BOTTOM)  
      
# top.mainloop()  

# from statistics import geometric_mean
# from tkinter import*
# top=Tk()
# b=Button(top,text="hlo",width=20,height=10,relief="sunken",activebackground="DarkGray",activeforeground="black",bg="PaleTurquoise")
# b.pack(side=BOTTOM)
# top.mainloop()
from tkinter import *
import tkinter

top = tkinter.Tk()

B1 = tkinter.Button(top, text ="circle", relief=RAISED,\
                         cursor="circle")
B2 = tkinter.Button(top, text ="plus", relief=RAISED,\
                         cursor="plus")
B1.pack()
B2.pack()
top.mainloop()