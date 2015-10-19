# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-09
# Assignment_01

from tkinter import *
from math import *
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog

class cl_widgets:
    def __init__(self,ob_root_window,ob_world=[]):
        self.ob_root_window=ob_root_window
        self.ob_world=ob_world
        self.pannel_01 = cl_pannel_01(self)
        self.ob_canvas_frame=cl_canvas_frame(self)
        self.ob_world.add_canvas(self.ob_canvas_frame.canvas)

class cl_canvas_frame:
    
    def __init__(self, master):
        self.master=master
        self.canvas = Canvas(master.ob_root_window,width=640, height=640, bg="white")
        self.canvas.pack(expand=YES, fill=BOTH)
        
        self.canvas.bind('<Configure>', self.canvas_resized_callback) 
        self.canvas.bind("<ButtonPress-1>", self.left_mouse_click_callback)
        
    def left_mouse_click_callback(self,event):
        print ('Left mouse button was clicked')
        print ('x=',event.x, '   y=',event.y)
        self.x = event.x
        self.y = event.y  
        self.canvas.focus_set()
        
    def canvas_resized_callback(self,event):
        self.canvas.config(width=event.width-4,height=event.height-4)
        self.canvas.pack()
        print ('canvas width', self.canvas.cget("width"))
        print ('canvas height', self.canvas.cget("height"))
        self.master.ob_world.redisplay(self.master.ob_canvas_frame.canvas,event)
        
class cl_pannel_01:

    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var_filename = StringVar()
        self.var_filename.set('')
        
        self.e = Entry(frame, width=70)
        self.e.pack(side=LEFT)
        
        self.file_dialog_button = Button(frame, text="Open File Dialog", fg="blue", command=self.browse_file)
        self.file_dialog_button.pack(side=LEFT) 
        
        self.file_load_button = Button(frame, text="Load", fg="blue", command=self.load_file)
        self.file_load_button.pack(side=LEFT) 

    def browse_file(self):
        self.var_filename.set(filedialog.askopenfilename(filetypes=[("allfiles","*"),("pythonfiles","*.txt")]))
        filename = self.var_filename.get()
        self.e.delete(0,END)
        self.e.insert(0,filename)
        
    def load_file(self):
        self.master.ob_canvas_frame.canvas.delete("all")
        self.master.ob_world.load_image(self.master.ob_canvas_frame.canvas,self.e.get())

