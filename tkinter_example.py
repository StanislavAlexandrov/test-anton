
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
gui = Tk()
gui.geometry("100x100")



def getFolderPath():
   print(filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)))

btnFind = ttk.Button(gui, text="Open Folder",command=getFolderPath)
btnFind.grid(row=0,column=2)
from tkinter import filedialog


gui.mainloop()