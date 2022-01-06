from tkinter import *
import Backend
def StartVideo():
    Backend.Capture()
def cl():
    window.destroy()
window = Tk()
window.title("Motion Detector")
window.geometry("1000x500")
b1 = Button(text="Start Motion Detection",command = StartVideo)
b1.grid(row = 1,column = 1,rowspan = 1,columnspan = 1,padx = 400,pady = 100)
b2 = Button(text = "Close",command = cl)
b2.grid(row = 2,column = 1,rowspan = 1,columnspan = 1,padx = 400)
window.mainloop()