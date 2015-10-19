# Vandeliwala, Ismail
# 1000-990-475
# 2015-02-24
# Assignment_03

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
        
    def windowToViewPort(self,points):
        
        newPoints = []
        x = float(points[0])
        y = float(points[1])
        newX = vxmin + (sx * (x-0))
        newY = vymin + (sy * (1-y))
        newPoints.append(format(newX,'.6f'))
        newPoints.append(format(newY,'.6f'))
        
        return newPoints
            
    def clip(self,fp,sp):
        
        newPoint = []
        x1 = float(fp[0])
        y1 = float(fp[1])
        z1 = float(fp[2])
        x2 = float(sp[0])
        y2 = float(sp[1])
        z2 = float(sp[2])
        
        if x1 >= 0 and x1 <= 1 and y1 >= 0 and y1 <= 1 and z1 >= 0 and z1 <= 1 and x2 >= 0 and x2 <= 1 and y2 >= 0 and y2 <= 1 and z2 >= 0 and z2 <= 1:
            newPoint.append(str(x1) + ' ' + str(y1) + ' ' + str(z1))
            newPoint.append(str(x2) + ' ' + str(y2) + ' ' + str(z2))
        else:
            if x1 >= 0 and x1 <= 1 and y1 >= 0 and y1 <= 1 and z1 >= 0 and z1 <= 1:
                newPoint.append(str(x1) + ' ' + str(y1) + ' ' + str(z1))
            if x2 >= 0 and x2 <= 1 and y2 >= 0 and y2 <= 1 and z2 >= 0 and z2 <= 1:
                newPoint.append(str(x2) + ' ' + str(y2) + ' ' + str(z2))
            
            if x2-x1 != 0:
                # right plane
                t = (1 - x1)/(x2-x1)
                if t>=0 and t<=1:
                    newX = ((x2-x1) * t) + x1
                    newY = ((y2-y1) * t) + y1
                    if newY >=0 and newY <= 1:
                        newZ = ((z2-z1) * t) + z1
                        if newZ >=0 and newZ <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
                            
                # left plane
                t = (0 - x1)/(x2-x1)
                if t>=0 and t<=1:
                    newX = ((x2-x1) * t) + x1
                    newY = ((y2-y1) * t) + y1
                    if newY >=0 and newY <= 1:
                        newZ = ((z2-z1) * t) + z1
                        if newZ >=0 and newZ <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
            
            if y2-y1 != 0:
                # top plane
                t = (1 - y1)/(y2-y1)
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1            
                    newX = ((x2-x1) * t) + x1
                    if newX >=0 and newX <= 1:
                        newZ = ((z2-z1) * t) + z1
                        if newZ >=0 and newZ <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
                            
                # bottom plane
                t = (0 - y1)/(y2-y1)
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1            
                    newX = ((x2-x1) * t) + x1
                    if newX >=0 and newX <= 1:
                        newZ = ((z2-z1) * t) + z1
                        if newZ >=0 and newZ <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
                        
            if z2-z1 != 0:
                # back plane
                t = (1 - z1)/(z2-z1)
                if t>=0 and t<=1:
                    newZ = ((z2-z1) * t) + z1
                    newX = ((x2-x1) * t) + x1
                    if newX >=0 and newX <= 1:
                        newY = ((y2-y1) * t) + y1            
                        if newY >=0 and newY <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
                            
                # front plane
                t = (0 - z1)/(z2-z1)
                if t>=0 and t<=1:
                    newZ = ((z2-z1) * t) + z1
                    newX = ((x2-x1) * t) + x1
                    if newX >=0 and newX <= 1:
                        newY = ((y2-y1) * t) + y1            
                        if newY >=0 and newY <= 1:
                            a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                            if a not in newPoint:
                                newPoint.append(a)
                        
        return newPoint
    
    def plotPoints(self,canvas,cwidth,cheight):
        
        canvas.delete("all")
        self.objects.append(canvas.create_rectangle(cwidth*vxmin,cheight*vymin,cwidth*vxmax,cheight*vymax))
        transformedVertices2 = transformedVertices
        for key in faces:
            connection = key.split( )
            i = 0
            for face in connection:
                if i == 0:
                    firstPoint = transformedVertices2[int(face)].split( )
                    lastPoint = transformedVertices2[int(face)].split( )
                else:
                    secondPoint = transformedVertices2[int(face)].split( )
                    new = self.clip(firstPoint,secondPoint)
                    if new:
                        fp = self.windowToViewPort(new[0].split( ))
                        sp = self.windowToViewPort(new[1].split( ))
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1])))
                    firstPoint = secondPoint
                i = i + 1
                if i == len(connection):
                    new = self.clip(firstPoint,lastPoint)
                    if new:
                        fp = self.windowToViewPort(new[0].split( ))
                        sp = self.windowToViewPort(new[1].split( ))
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1])))
        canvas.update()
                    
    def getCompositeMatrix(self):
        
        t = np.matrix( ((1,0,0,-float(vrp[0])),(0,1,0,-float(vrp[1])),(0,0,1,-float(vrp[2])),(0,0,0,1)) )
        
        a = float(vpn[0])
        b = float(vpn[1])
        c = float(vpn[2])
        square = b**2 + c**2
        if square == 0:
            res = 1
            res1 = 0
        else:
            res = c/math.sqrt(float(square))
            res1 = b/math.sqrt(float(square))                        
        rx = np.matrix( ((1,0,0,0),(0,float(res),-float(res1),0),(0,float(res1),float(res),0),(0,0,0,1)) )
        compositeMatrix = rx * t
        oldVpn = np.matrix(((a,b,c,1)))    
        newVpn = rx*np.transpose(oldVpn)
        
        a = float(newVpn[0][0])
        b = float(newVpn[1][0])
        c = float(newVpn[2][0])
        res = c/math.sqrt(a**2 + c**2)
        res1 = a/math.sqrt(a**2 + c**2) 
        ry = np.matrix( ((float(res),0,-float(res1),0),(0,1,0,0),(float(res1),0,float(res),0),(0,0,0,1)) )
        compositeMatrix = ry * compositeMatrix 
        
        a = float(vup[0])
        b = float(vup[1])
        c = float(vup[2])
        res = b/math.sqrt(b**2 + a**2)
        res1 = a/math.sqrt(b**2 + a**2)
        rz = np.matrix( ((float(res),-float(res1),0,0),(float(res1),float(res),0,0),(0,0,1,0),(0,0,0,1)) )
        compositeMatrix = rz * compositeMatrix
        
        a = float(prp[0])
        b = float(prp[1])
        c = float(prp[2])
        res = (a-((umin+umax)/2))/c
        res1 = (b-((vmin+vmax)/2))/c
        sh = np.matrix( ((1,0,-float(res),0),(0,1,-float(res1),0),(0,0,1,0),(0,0,0,1)) )
        compositeMatrix = sh * compositeMatrix
        
        tcw = np.matrix( ((1,0,0,-umin),(0,1,0,-vmin),(0,0,1,-nmin),(0,0,0,1)) )
        compositeMatrix = tcw * compositeMatrix
        
        scx = float(1/(umax-umin))
        scy = float(1/(vmax-vmin))
        scz = float(1/(nmax-nmin))
        sm = np.matrix( ((float(scx),0,0,0),(0,float(scy),0,0),(0,0,float(scz),0),(0,0,0,1)) )
        compositeMatrix = sm * compositeMatrix
        
        return compositeMatrix
        
    def parallelNewPoint(self):
        
        for key in vertices1:
            points = vertices1[key].split( )
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
            
    def parallelNewPointOther(self):
        
        for key in transformedVertices1:
            points = transformedVertices1[key].split( )
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
    
    def load_image(self,canvas,fileName):
        f = open(fileName, 'r')
        
        global vertices
        vertices = {}

        global vertices1
        vertices1 = {}
        
        global transformedVertices
        transformedVertices = {}
        
        global transformedVertices1
        transformedVertices1 = {}
        
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
        global umin
        global umax
        global vmin
        global vmax
        global nmin
        global nmax
        global sx
        global sy
        global vrp
        global vpn
        global vup
        global prp
        global compositeMatrix
        
        vrp = []
        vpn = []
        vup = []
        prp = []
        compositeMatrix = np.empty(shape=[0, 4])
        
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
            elif firstLetter == 'r':
                vrp = second.rstrip().split( )
            elif firstLetter == 'n':
                vpn = second.rstrip().split( )
            elif firstLetter == 'u':
                vup = second.rstrip().split( )
            elif firstLetter == 'p':
                prp = second.rstrip().split( )
                
        f.close()
        
        umin = float(window[0])
        umax = float(window[1])
        vmin = float(window[2])
        vmax = float(window[3])
        nmin = float(window[4])
        nmax = float(window[5])
        
        vxmin = float(viewport[0])
        vymin = float(viewport[1])
        vxmax = float(viewport[2])
        vymax = float(viewport[3])
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
        
        compositeMatrix = self.getCompositeMatrix()
        vertices1 = vertices
        self.parallelNewPoint()
        sx = (vxmax - vxmin)
        sy = (vymax - vymin)
        self.plotPoints(canvas,cwidth,cheight)
        
    def redisplay(self,canvas,event):
        
        cwidth = float(event.width)
        cheight = float(event.height)
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
            if not transformedVertices1:
                vertices1 = vertices
            else:
                vertices1 = transformedVertices1
            for key in vertices1:
                points = vertices1[key].split( )
                x = float(points[0])
                y = float(points[1]) 
                z = float(points[2]) 
                mat = np.matrix(((x,y,z,1)))
                result = rotationMatrix*np.transpose(mat)
                newX = float(result[0][0])
                newY = float(result[1][0])
                newZ = float(result[2][0])
                newPoint = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                transformedVertices1[key] = newPoint
            
            cwidth = float(canvas.cget("width"))
            cheight = float(canvas.cget("height"))
            self.parallelNewPointOther()
            self.plotPoints(canvas,cwidth,cheight)
            
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
            scaleMatrix = np.matrix( ((scalex,0,0,0),(0,scaley,0,0),(0,0,scalez,0),(0,0,0,1)) )
            t_Matrix = np.matrix( ((1,0,0,float(p[0])),(0,1,0,float(p[1])),(0,0,1,float(p[2])),(0,0,0,1)) )
            
            compositeMatrixScale = tMatrix * scaleMatrix * t_Matrix
            steps = int(steps)
    
            for i in range(1,steps+1):
                if not transformedVertices1:
                    vertices1 = vertices
                else:
                    vertices1 = transformedVertices1
                for key in vertices1:
                    points = vertices1[key].split( )
                    x = float(points[0])
                    y = float(points[1]) 
                    z = float(points[2]) 
                    mat = np.matrix(((x,y,z,1)))
                    result = compositeMatrixScale*np.transpose(mat)
                    newX = float(result[0][0])
                    newY = float(result[1][0])
                    newZ = float(result[2][0])
                    newPoint = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                    transformedVertices1[key] = newPoint
                
                cwidth = float(canvas.cget("width"))
                cheight = float(canvas.cget("height"))
                self.parallelNewPointOther()
                self.plotPoints(canvas,cwidth,cheight)
                
    def translate_image(self,canvas,translatex,translatey,translatez,steps):
        
        translatex = float(translatex)/float(steps)
        translatey = float(translatey)/float(steps)
        translatez = float(translatez)/float(steps)
        
        tMatrix = np.matrix( ((1,0,0,float(translatex)),(0,1,0,float(translatey)),(0,0,1,float(translatez)),(0,0,0,1)) )
        
        steps = int(steps)
    
        for i in range(1,steps+1):
            if not transformedVertices1:
                vertices1 = vertices
            else:
                vertices1 = transformedVertices1
            for key in vertices:
                points = vertices1[key].split( )
                x = float(points[0])
                y = float(points[1]) 
                z = float(points[2]) 
                mat = np.matrix(((x,y,z,1)))
                result = tMatrix*np.transpose(mat)
                newX = float(result[0][0])
                newY = float(result[1][0])
                newZ = float(result[2][0])
                newPoint = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                transformedVertices1[key] = newPoint
            
            cwidth = float(canvas.cget("width"))
            cheight = float(canvas.cget("height"))
            self.parallelNewPointOther()
            self.plotPoints(canvas,cwidth,cheight)
            
    def fly_image(self,canvas,point,point1,steps):
        
        global compositeMatrix
        compositeMatrix = np.empty(shape=[0, 4])
        
        global vertices1
        vertices1 = vertices
        
        global vrp
        vrp = []
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
        
        vrp = point.split(",")
        compositeMatrix = self.getCompositeMatrix()
        self.parallelNewPointOther()
        self.clip1(canvas,cwidth,cheight)
        
        p = point1.split(",")
        x = float(p[0])/float(steps)
        y = float(p[1])/float(steps)
        z = float(p[1])/float(steps)
        totalx = 0
        totaly = 0
        totalz = 0
        steps = int(steps)
        for i in range(1,steps+1):
            vrp = []
            totalx = float(totalx) + float(x)
            totaly = float(totaly) + float(y)
            totalz = float(totalz) + float(z)
            vrp.append(float(totalx))        
            vrp.append(float(totaly))
            vrp.append(float(totalz))
            compositeMatrix = self.getCompositeMatrix()
            self.parallelNewPointOther()
            self.plotPoints(canvas,cwidth,cheight)