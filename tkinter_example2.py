from tkinter import *
from tkinter import filedialog


def openFile():
        
    
    tf = filedialog.askopenfilename(
        initialdir="C:\Anton\VS\.git", 
        title="Open Text file", 
        filetypes=(("text","*.txt"),("All files", "*.*"))
        )
    pathh.insert(END, tf)
    tf = open(tf)  # or tf = open(tf, 'r')
    data = tf.read()
    txtarea.insert(END, data)
    tf.close()


ws = Tk()
ws.title("Test_open_file")
ws.geometry("400x450")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


ws.mainloop()