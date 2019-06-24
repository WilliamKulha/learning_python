from tkinter import *
import tkinter.scrolledtext as ScrolledText

#Root for main window
root = Tk(className = " Text Editor")

textArea = ScrolledText.ScrolledText(root, width=500, height=500)
textArea.configure(background="black", foreground="white")
textArea.pack()

#Menu Options
menu = Menu(root)
root.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New File")
#Keep window open
root.mainloop()
