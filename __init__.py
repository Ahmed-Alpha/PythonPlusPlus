import tkinter
from tkinter import *
from tkinter import ttk
Tk=tkinter

# Basics
def write(data):
    """
    Show data in a specific location(e.g. terminal)
    """
    print(data)

def insert(data):
    """
    Query the user in front-end(e.g. terminal or finished version)
    """
    input(data)

#Graphical User Interface

def gui(data):
    """
    Creates a blank, 500x500 Graphical User Interface page
    This is a code method/ usage not a terminal method/ usage
    """
    import tkinter as tk
    root = tk.Tk()
    root.title(data)
    root.geometry("500x500")
    root.mainloop()

def gui_fullscreen(data):
    """
    Creates a blank, fullscreen Graphical User Interface page
    This is a code method/ usage not a terminal method/ usage
    """
    import tkinter as tk
    root = tk.Tk()
    root.title(data)
    width= root.winfo_screenwidth()
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))
    root.mainloop()

def messagebox_info_greeting(data):
    import tkinter as tk
    from tkinter import messagebox
    tkinter.messagebox.showinfo(title=data, message="Hello, World!")
    tkinter.mainloop()

def messagebox_qs_proceed(data):
    import tkinter as tk
    from tkinter import messagebox
    tkinter.messagebox.askquestion(title=data, message="Do you wish to proceed?")
    tkinter.mainloop()

def messagebox_warn_continue(data):
    import tkinter as tk
    from tkinter import messagebox
    tkinter.messagebox.showwarning(title=data, message="Do you want to continue?")
    tkinter.mainloop()

def messagebox_opps_error(data):
    import tkinter as tk
    from tkinter import messagebox
    tkinter.messagebox.showerror(title=data, message="Oops, error ocurred!")
    tkinter.mainloop()

