# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-09
# Assignment_01

#from numpy  import *
from math import *
from tkinter import *


class cl_world:
    def __init__(self, objects=[],canvases=[]):
        self.objects=objects
        self.canvases=canvases
        
    def load_image(self,canvas,fileName):
        f = open(fileName, 'r')
        
        global vertices
        vertices = {}
        
        global faces
        faces = []
        
        window = []
        viewport = []
        
        global newVertices
        newVertices = {} 

        global vxmin
        global vymin
        global vxmax
        global vymax
        
        i = 0;
        for line in f:
            firstLetter = line[:1]
            second = line[2:]
            if firstLetter == 'v':
                i = i+1
                vertices[i] = second.rstrip()
            elif firstLetter == 'f':
                faces.append(second.rstrip())
            elif firstLetter == 'w':
                window = second.rstrip().split( )
            elif firstLetter == 's':
                viewport = second.rstrip().split( )
        f.close()
        
        wxmin = float(window[0])
        wymin = float(window[1])
        wxmax = float(window[2])
        wymax = float(window[3])
        
        vxmin = float(viewport[0])
        vymin = float(viewport[1])
        vxmax = float(viewport[2])
        vymax = float(viewport[3])
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
        self.objects.append(canvas.create_rectangle(cwidth*vxmin,cheight*vymin,cwidth*vxmax,cwidth*vymax))
        
        sx = (vxmax - vxmin) / (wxmax - wxmin)
        sy = (vymax - vymin) / (wymax - wymin)         

        for key in vertices:
            newPoints = []
            points = vertices[key].split( )
            x = float(points[0])
            y = float(points[1])
            newX = vxmin + (sx * (x-wxmin))
            newY = vymin + (sy * (wymax-y))
            newPoints.append(format(newX,'.6f'))
            newPoints.append(format(newY,'.6f'))
            newVertices[key] = newPoints
        
        for key in faces:
            connection = key.split( )
            i = 0
            for face in connection:
                if i == 0:
                    firstPoint = newVertices[int(face)]
                    lastPoint = newVertices[int(face)]
                else:
                    secondPoint = newVertices[int(face)]
                    self.objects.append(canvas.create_line(cwidth*float(firstPoint[0]),cheight*float(firstPoint[1]),cwidth*float(secondPoint[0]),cheight*float(secondPoint[1])))
                    firstPoint = secondPoint
                i = i + 1
                if i == len(connection):
                    self.objects.append(canvas.create_line(cwidth*float(firstPoint[0]),cheight*float(firstPoint[1]),cwidth*float(lastPoint[0]),cheight*float(lastPoint[1])))
                
        
#        print("vertices: ",vertices)
        print("new vertices: ",newVertices)
#        print(faces)
#        print("wxmin: ",wxmin," wymin: ",wymin," wxmax: ",wxmax," wymax: ",wymax)
#        print("vxmin: ",vxmin," vymin: ",vymin," vxmax: ",vxmax," vymax: ",vymax)
#        print("sx: ",sx," sy: ",sy)
#        print("cwidth: ",cwidth," cheight: ",cheight)
        
    def add_canvas(self,canvas):
        self.canvases.append(canvas)
        canvas.world=self
       
    def redisplay(self,canvas,event):
        
        canvas.delete("all")
        cwidth = float(event.width)
        cheight = float(event.height)
        self.objects.append(canvas.create_rectangle(cwidth*vxmin,cheight*vymin,cwidth*vxmax,cwidth*vymax))
        
        count = 1
        for key in faces:
            connection = key.split( )
            i = 0
            for face in connection:
                if i == 0:
                    firstPoint = newVertices[int(face)]
                    lastPoint = newVertices[int(face)]
                else:
                    secondPoint = newVertices[int(face)]
                    self.objects.append(canvas.create_line(cwidth*float(firstPoint[0]),cheight*float(firstPoint[1]),cwidth*float(secondPoint[0]),cheight*float(secondPoint[1])))                    
                    count = count + 1                    
                    firstPoint = secondPoint
                i = i + 1
                if i == len(connection):
                    self.objects.append(canvas.create_line(cwidth*float(firstPoint[0]),cheight*float(firstPoint[1]),cwidth*float(lastPoint[0]),cheight*float(lastPoint[1])))                    
                    count = count + 1
                
        
#        print("vertices: ",vertices)
#        print("new vertices: ",newVertices)
#        print(faces)
#        print("wxmin: ",wxmin," wymin: ",wymin," wxmax: ",wxmax," wymax: ",wymax)
#        print("vxmin: ",vxmin," vymin: ",vymin," vxmax: ",vxmax," vymax: ",vymax)
#        print("sx: ",sx," sy: ",sy)
#        print("cwidth: ",cwidth," cheight: ",cheight)       
