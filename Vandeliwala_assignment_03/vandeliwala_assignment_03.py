# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-24
# Assignment_03

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

import string
from vandeliwala_widgets_03 import *
from vandeliwala_graphics_03 import *

def close_window_callback(root):
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()


ob_root_window = Tk()
ob_root_window.protocol("WM_DELETE_WINDOW", lambda root_window=ob_root_window: close_window_callback(root_window))
ob_world=cl_world()
cl_widgets(ob_root_window,ob_world)
ob_root_window.mainloop()    
    
