# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-16
# Assignment_02

#from numpy  import *
from math import *
from tkinter import *
import numpy as np
import math

class cl_world:
    def __init__(self, objects=[],canvases=[]):
        self.objects=objects
        self.canvases=canvases
    
    def add_canvas(self,canvas):
        self.canvases.append(canvas)
        canvas.world=self  
        
    def windowToViewPort(self):
        for key in transformedVertices:
            newPoints = []
            points = transformedVertices[key].split( )
            x = float(points[0])
            y = float(points[1])
            newX = vxmin + (sx * (x-wxmin))
            newY = vymin + (sy * (wymax-y))
            newPoints.append(format(newX,'.6f'))
            newPoints.append(format(newY,'.6f'))
            newVertices[key] = newPoints
    
    def plotPoints(self,canvas,cwidth,cheight):
        canvas.delete("all")
        self.objects.append(canvas.create_rectangle(cwidth*vxmin,cheight*vymin,cwidth*vxmax,cwidth*vymax))
        for key in faces:
            newPoints = []
            connection = key.split( )
            for face in connection:
                firstPoint = newVertices[int(face)]
                newPoints.append(cwidth*float(firstPoint[0]))
                newPoints.append(cheight*float(firstPoint[1]))
            self.objects.append(canvas.create_polygon(newPoints,fill="white", outline="black"))
        canvas.update()
          
    def updatePoints(self,canvas,cwidth,cheight):
        canvas.coords(1,cwidth*vxmin,cheight*vymin,cwidth*vxmax,cwidth*vymax)
        count = 2
        for key in faces:
            newPoints = []
            connection = key.split( )
            for face in connection:
                firstPoint = newVertices[int(face)]
                newPoints.append(cwidth*float(firstPoint[0]))
                newPoints.append(cheight*float(firstPoint[1]))
            canvas.coords(count,*newPoints)
            count = count + 1
            
    def load_image(self,canvas,fileName):
        f = open(fileName, 'r')
        
        global vertices
        vertices = {}
        
        global transformedVertices
        transformedVertices = {}
        
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
        global wxmin
        global wymin
        global wxmax
        global wymax
        global sx
        global sy
        
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
        
        sx = (vxmax - vxmin) / (wxmax - wxmin)
        sy = (vymax - vymin) / (wymax - wymin)         

        transformedVertices = vertices
        self.windowToViewPort();
        self.plotPoints(canvas,cwidth,cheight);
    
    def redisplay(self,canvas,event):
        
        cwidth = float(event.width)
        cheight = float(event.height)
        print(cwidth," ",cheight)
        self.plotPoints(canvas,cwidth,cheight); 
                
    def rotate_image(self,canvas,radioSelection,degree,steps):
        
        degree = float(degree)/float(steps)
        cos = math.cos(math.radians(degree))
        sin = math.sin(math.radians(degree))
        steps = int(steps)
        
        if radioSelection == 1:
            rotationMatrix = np.matrix( ((1,0,0,0),(0,cos,-sin,0),(0,sin,cos,0),(0,0,0,1)) )
        elif radioSelection == 2:
            rotationMatrix = np.matrix( ((cos,0,sin,0),(0,1,0,0),(-sin,0,cos,0),(0,0,0,1)) )
        elif radioSelection == 3:
            rotationMatrix = np.matrix( ((cos,-sin,0,0),(sin,cos,0,0),(0,0,1,0),(0,0,0,1)) )

        for i in range(1,steps+1):
            vertices = transformedVertices
            for key in vertices:
                points = vertices[key].split( )
                x = float(points[0])
                y = float(points[1]) 
                z = float(points[2]) 
                mat = np.matrix(((x,y,z,1)))
                result = rotationMatrix*np.transpose(mat)
                newX = float(result[0][0])
                newY = float(result[1][0])
                newZ = float(result[2][0])
                newPoint = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                transformedVertices[key] = newPoint
            
            cwidth = float(canvas.cget("width"))
            cheight = float(canvas.cget("height"))
            
            self.windowToViewPort();
            self.plotPoints(canvas,cwidth,cheight); 
            
    def scale_image(self,canvas,scalex,scaley,scalez,steps,point):
        
        scalex = float(scalex)
        scaley = float(scaley)
        scalez = float(scalez)
            
        if scalex > 1 or scaley > 1:
            
            p = point.split(",")
            steps = float(steps)
            
            if scalex > 1:
                scalex = 1 + (scalex - 1)/steps
            if scaley > 1:
                scaley = 1 + (scaley - 1)/steps
            if scalez > 1:
                scalez = 1 + (scalez - 1)/steps                
            
            tMatrix = np.matrix( ((1,0,0,-float(p[0])),(0,1,0,-float(p[1])),(0,0,1,-float(p[2])),(0,0,0,1)) )
            rotationMatrix = np.matrix( ((scalex,0,0,0),(0,scaley,0,0),(0,0,scalez,0),(0,0,0,1)) )
            t_Matrix = np.matrix( ((1,0,0,float(p[0])),(0,1,0,float(p[1])),(0,0,1,float(p[2])),(0,0,0,1)) )
            
            compositeMatrix = tMatrix * rotationMatrix * t_Matrix
            print(compositeMatrix)
            steps = int(steps)
    
            for i in range(1,steps+1):
                vertices = transformedVertices
                for key in vertices:
                    points = vertices[key].split( )
                    x = float(points[0])
                    y = float(points[1]) 
                    z = float(points[2]) 
                    mat = np.matrix(((x,y,z,1)))
                    result = compositeMatrix*np.transpose(mat)
                    newX = float(result[0][0])
                    newY = float(result[1][0])
                    newZ = float(result[2][0])
                    newPoint = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                    transformedVertices[key] = newPoint
                
                cwidth = float(canvas.cget("width"))
                cheight = float(canvas.cget("height"))
                
                self.windowToViewPort();
                self.plotPoints(canvas,cwidth,cheight);  
