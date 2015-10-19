# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-24
# Assignment_03

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
        self.pannel_02 = cl_pannel_02(self)
        self.pannel_03 = cl_pannel_03(self)
        self.pannel_04 = cl_pannel_04(self)
        self.pannel_05 = cl_pannel_05(self)
        self.ob_canvas_frame=cl_canvas_frame(self)
        self.ob_world.add_canvas(self.ob_canvas_frame.canvas)

class cl_canvas_frame:
    
    def __init__(self, master):
        self.master=master
        self.canvas = Canvas(master.ob_root_window,width=600, height=480, bg="white")
        self.canvas.pack(expand = YES, fill = BOTH)
        
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
        
class cl_pannel_02:

    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var = StringVar()
        self.label = Label(frame,textvariable = self.var )
        self.var.set("Rotation Axis: ")
        self.label.pack(side=LEFT)
               
        self.v = IntVar()

        self.r1 = Radiobutton(frame, text="X", variable=self.v, value=1)
        self.r1.pack(side=LEFT)
        self.r2 = Radiobutton(frame, text="Y", variable=self.v, value=2)
        self.r2.pack(side=LEFT)
        self.r3 = Radiobutton(frame, text="Z", variable=self.v, value=3)
        self.r3.pack(side=LEFT)

        self.var1 = StringVar()
        self.label1 = Label(frame,textvariable = self.var1 )
        self.var1.set("Degress: ")
        self.label1.pack(side=LEFT)        
        
        self.listbox = Listbox(frame, height = 1)
        self.listbox.pack(side=LEFT)
        
        for item in range(1,361):
            self.listbox.insert(END, item)
        self.listbox.select_set(0)
        
        self.var2 = StringVar()
        self.label2 = Label(frame,textvariable = self.var2 )
        self.var2.set("Steps: ")
        self.label2.pack(side=LEFT)
        
        self.steps = Entry(frame, width=5)
        self.steps.pack(side=LEFT)
        self.steps.insert(INSERT,"1")
        
        self.button = Button(frame, text="Rotate", fg="blue", command=self.rotate_callback)
        self.button.pack(side=LEFT)
        

    def rotate_callback(self):
        self.current = self.listbox.curselection()
        if not self.current:
            self.listbox.select_set(self.newSelection)
        else:
            self.newSelection = self.current[0]
        print(self.newSelection)
        self.selected = self.listbox.get(self.listbox.curselection())
        self.master.ob_world.rotate_image(self.master.ob_canvas_frame.canvas,self.v.get(),self.selected,self.steps.get())
        
class cl_pannel_03:

    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var = StringVar()
        self.label = Label(frame,textvariable = self.var )
        self.var.set("Scale X: ")
        self.label.pack(side=LEFT)
            
        self.scalex = Entry(frame, width=5)
        self.scalex.pack(side=LEFT)
        
        self.var1 = StringVar()
        self.label1 = Label(frame,textvariable = self.var1 )
        self.var1.set("Scale Y: ")
        self.label1.pack(side=LEFT)
        
        self.scaley = Entry(frame, width=5)
        self.scaley.pack(side=LEFT)
        
        self.var2 = StringVar()
        self.label2 = Label(frame,textvariable = self.var2 )
        self.var2.set("Scale Z: ")
        self.label2.pack(side=LEFT)
        
        self.scalez = Entry(frame, width=5)
        self.scalez.pack(side=LEFT)
        
        self.var3 = StringVar()
        self.label3 = Label(frame,textvariable = self.var3 )
        self.var3.set("A: ")
        self.label3.pack(side=LEFT)
        
        self.point = Entry(frame, width=10)
        self.point.pack(side=LEFT)
        self.point.insert(INSERT,"0,0,0")
        
        self.var4 = StringVar()
        self.label4 = Label(frame,textvariable = self.var4 )
        self.var4.set("Steps: ")
        self.label4.pack(side=LEFT)
        
        self.steps = Entry(frame, width=5)
        self.steps.pack(side=LEFT)
        self.steps.insert(INSERT,"1")
        
        self.button = Button(frame, text="Scale", fg="blue", command=self.scale_callback)
        self.button.pack(side=LEFT)
        

    def scale_callback(self):
        
        self.master.ob_world.scale_image(self.master.ob_canvas_frame.canvas,self.scalex.get(),self.scaley.get(),self.scalez.get(),self.steps.get(),self.point.get())
        
class cl_pannel_04:

    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var = StringVar()
        self.label = Label(frame,textvariable = self.var )
        self.var.set("Translate X: ")
        self.label.pack(side=LEFT)
            
        self.translatex = Entry(frame, width=5)
        self.translatex.pack(side=LEFT)
        
        self.var1 = StringVar()
        self.label1 = Label(frame,textvariable = self.var1 )
        self.var1.set("Translate Y: ")
        self.label1.pack(side=LEFT)
        
        self.translatey = Entry(frame, width=5)
        self.translatey.pack(side=LEFT)
        
        self.var2 = StringVar()
        self.label2 = Label(frame,textvariable = self.var2 )
        self.var2.set("Translate Z: ")
        self.label2.pack(side=LEFT)
        
        self.translatez = Entry(frame, width=5)
        self.translatez.pack(side=LEFT)
        
        self.var4 = StringVar()
        self.label4 = Label(frame,textvariable = self.var4 )
        self.var4.set("Steps: ")
        self.label4.pack(side=LEFT)
        
        self.steps = Entry(frame, width=5)
        self.steps.pack(side=LEFT)
        self.steps.insert(INSERT,"1")
        
        self.button = Button(frame, text="Translate", fg="blue", command=self.translate_callback)
        self.button.pack(side=LEFT)
        

    def translate_callback(self):
        
        self.master.ob_world.translate_image(self.master.ob_canvas_frame.canvas,self.translatex.get(),self.translatey.get(),self.translatez.get(),self.steps.get())

class cl_pannel_05:

    def __init__(self, master):

        self.master=master
        frame = Frame(master.ob_root_window)
        frame.pack()
        
        self.var3 = StringVar()
        self.label3 = Label(frame,textvariable = self.var3 )
        self.var3.set("VRP1: ")
        self.label3.pack(side=LEFT)
        
        self.point = Entry(frame, width=10)
        self.point.pack(side=LEFT)
        self.point.insert(INSERT,"0,0,0")
        
        self.var4 = StringVar()
        self.label4 = Label(frame,textvariable = self.var4 )
        self.var4.set("VRP2: ")
        self.label4.pack(side=LEFT)
        
        self.point1 = Entry(frame, width=10)
        self.point1.pack(side=LEFT)
        self.point1.insert(INSERT,"0,0,0")
        
        self.var5 = StringVar()
        self.label5 = Label(frame,textvariable = self.var5 )
        self.var5.set("Steps: ")
        self.label5.pack(side=LEFT)
        
        self.steps = Entry(frame, width=5)
        self.steps.pack(side=LEFT)
        self.steps.insert(INSERT,"1")
        
        self.button = Button(frame, text="Fly", fg="blue", command=self.fly_callback)
        self.button.pack(side=LEFT)
        

    def fly_callback(self):
        
        self.master.ob_world.fly_image(self.master.ob_canvas_frame.canvas,self.point.get(),self.point1.get(),self.steps.get())