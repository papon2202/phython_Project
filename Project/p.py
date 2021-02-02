from tkinter import *
from PIL import Image,ImageTk
root = Tk()



photo = ImageTk.PhotoImage(file= 'bg.jpg')
label = Label(image =photo)
label.pack()

root.mainloop()