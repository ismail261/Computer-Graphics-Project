# Vandeliwala, Ismail
# 1000-990-475
# 2015-03-06
# Assignment_04

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
        
    def windowToViewPort(self,points,vxmin,vymin,sx,sy):
        
        newPoints = []
        x = float(points[0])
        y = float(points[1])
        newX = vxmin + (sx * (x-0))
        newY = vymin + (sy * (1-y))
        newPoints.append(format(newX,'.6f'))
        newPoints.append(format(newY,'.6f'))
        
        return newPoints
        
    def windowToViewPortPers(self,points,vxmin,vymin,sx,sy):
        
        newPoints = []
        z = float(points[2])        
        x = float(points[0])/z
        y = float(points[1])/z
        
        newX = vxmin + (sx * (x+1))
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
        
    def persClip(self,fp,sp,zmin):
        
        newPoint = []
        x1 = float("{0:.2f}".format(float(fp[0])))
        y1 = float("{0:.2f}".format(float(fp[1])))
        z1 = float("{0:.2f}".format(float(fp[2])))
        x2 = float("{0:.2f}".format(float(sp[0])))
        y2 = float("{0:.2f}".format(float(sp[1])))
        z2 = float("{0:.2f}".format(float(sp[2])))
        zmin = float("{0:.2f}".format(float(zmin)))
        
        
        if abs(x1) < z1 and abs(y1) < z1 and z1 > zmin and z1 < 1 and abs(x2) < z2 and abs(y2) < z2 and z2 > zmin and z2 < 1:
            newPoint.append(str(x1) + ' ' + str(y1) + ' ' + str(z1))
            newPoint.append(str(x2) + ' ' + str(y2) + ' ' + str(z2))
        else:
            
            if abs(x1) < z1 and abs(y1) < z1 and z1 > zmin and z1 < 1:
                newPoint.append(str(x1) + ' ' + str(y1) + ' ' + str(z1))
            if abs(x2) < z2 and abs(y2) < z2 and z2 > zmin and z2 < 1:
                newPoint.append(str(x2) + ' ' + str(y2) + ' ' + str(z2))
                    
            if (x2-x1)-(z2-z1) != 0:
                # right plane
                t = -((x1 - z1)/((x2-x1)-(z2-z1)))
                if t>=0 and t<=1:
                    newX = ((x2-x1) * t) + x1
                    newY = ((y2-y1) * t) + y1
                    newZ = ((z2-z1) * t) + z1
                    if newZ >= zmin and newZ <= 1 and abs(newY) <= newZ:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)
            
            if (z2-z1)+(x2-x1) != 0:               
                # left plane
                t = -((x1 + z1)/((z2-z1)+(x2-x1)))
                if t>=0 and t<=1:
                    newX = ((x2-x1) * t) + x1
                    newY = ((y2-y1) * t) + y1
                    newZ = ((z2-z1) * t) + z1
                    if newZ >= zmin and newZ <= 1 and abs(newY) <= newZ:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)
            
            if (y2-y1)-(z2-z1) != 0:
                # top plane
                t = -((y1 - z1)/((y2-y1)-(z2-z1)))
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1            
                    newX = ((x2-x1) * t) + x1
                    newZ = ((z2-z1) * t) + z1
                    if newZ >= zmin and newZ <= 1 and abs(newX) <= newZ:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)
            
            if (y2-y1)+(z2-z1) != 0:
                # bottom plane
                t = -((y1 + z1)/((y2-y1)+(z2-z1))) 
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1            
                    newX = ((x2-x1) * t) + x1
                    newZ = ((z2-z1) * t) + z1
                    if newZ >= zmin and newZ <= 1 and abs(newX) <= newZ:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)
                        
            if z2-z1 != 0:
                # back plane
                t = -((z1-1)/(z2-z1))
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1
                    newX = ((x2-x1) * t) + x1
                    newZ = ((z2-z1) * t) + z1
                    if abs(newY) <= 1 and abs(newX) <= 1:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)
                            
                # front plane
                t = -((z1-zmin)/(z2-z1))
                if t>=0 and t<=1:
                    newY = ((y2-y1) * t) + y1
                    newX = ((x2-x1) * t) + x1
                    newZ = ((z2-z1) * t) + z1
                    if abs(newY) <= zmin and abs(newX) <= zmin:
                        a = str(newX) + ' ' + str(newY) + ' ' + str(newZ)
                        if a not in newPoint:
                            newPoint.append(a)               
        return newPoint
    
    def plotPoints(self,canvas,name,cwidth,cheight,viewport,transformedVertices):
        
        vxmin = float(viewport[0])
        vymin = float(viewport[1])
        vxmax = float(viewport[2])
        vymax = float(viewport[3])
        sx = (vxmax - vxmin)
        sy = (vymax - vymin)
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
                        fp = self.windowToViewPort(new[0].split( ),vxmin,vymin,sx,sy)
                        sp = self.windowToViewPort(new[1].split( ),vxmin,vymin,sx,sy)
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1]), tags = name))
                    firstPoint = secondPoint
                i = i + 1
                if i == len(connection):
                    new = self.clip(firstPoint,lastPoint)
                    if new:
                        fp = self.windowToViewPort(new[0].split( ),vxmin,vymin,sx,sy)
                        sp = self.windowToViewPort(new[1].split( ),vxmin,vymin,sx,sy)
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1]), tags = name))
        canvas.update()
        
    def plotPersPoints(self,canvas,name,cwidth,cheight,zmin,viewport,transformedVertices):
        
        vxmin = float(viewport[0])
        vymin = float(viewport[1])
        vxmax = float(viewport[2])
        vymax = float(viewport[3])
        sx = (vxmax - vxmin)/2
        sy = (vymax - vymin)/2
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
                    new = self.persClip(firstPoint,secondPoint,zmin)
                    if new and len(new) == 2:
                        fp = self.windowToViewPortPers(new[0].split( ),vxmin,vymin,sx,sy)
                        sp = self.windowToViewPortPers(new[1].split( ),vxmin,vymin,sx,sy)
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1]), tags = name))
                    firstPoint = secondPoint
                i = i + 1
                if i == len(connection):
                    new = self.persClip(firstPoint,lastPoint,zmin)
                    if new  and len(new) == 2:
                        fp = self.windowToViewPortPers(new[0].split( ),vxmin,vymin,sx,sy)
                        sp = self.windowToViewPortPers(new[1].split( ),vxmin,vymin,sx,sy)
                        self.objects.append(canvas.create_line(cwidth*float(fp[0]),cheight*float(fp[1]),cwidth*float(sp[0]),cheight*float(sp[1]), tags = name))
        canvas.update()
        
    def getCompositeMatrix(self,vrp,vpn,vup,prp,window):
        
        compositeMatrix = np.empty(shape=[0, 4])
        umin = float(window[0])
        umax = float(window[1])
        vmin = float(window[2])
        vmax = float(window[3])
        nmin = float(window[4])
        nmax = float(window[5])
        
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
        oldVup = np.matrix(((float(vup[0]),float(vup[1]),float(vup[2]),1)))
        newVpn = rx*np.transpose(oldVpn)
        newVup = rx*np.transpose(oldVup)
        
        a = float(newVpn[0][0])
        b = float(newVpn[1][0])
        c = float(newVpn[2][0])
        res = c/math.sqrt(a**2 + c**2)
        res1 = a/math.sqrt(a**2 + c**2) 
        ry = np.matrix( ((float(res),0,-float(res1),0),(0,1,0,0),(float(res1),0,float(res),0),(0,0,0,1)) )
        compositeMatrix = ry * compositeMatrix 
        oldVup = np.matrix(((float(newVup[0][0]),float(newVup[1][0]),float(newVup[2][0]),1)))
        newVup = ry*np.transpose(oldVup)
        
        a = float(newVup[0][0])
        b = float(newVup[1][0])
        c = float(newVup[2][0])
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
        
        if umax > umin:
            a = -umin
        else:
            a = -umax
        if vmax > vmin:
            b = -vmin
        else:
            b = -vmax
        if nmax > nmin:
            c = -nmin
        else:
            c = -nmax
        tcw = np.matrix( ((1,0,0,a),(0,1,0,b),(0,0,1,c),(0,0,0,1)) )
        compositeMatrix = tcw * compositeMatrix
        
        scx = float(1/(umax-umin))
        scy = float(1/(vmax-vmin))
        scz = float(1/(nmax-nmin))
        sm = np.matrix( ((float(scx),0,0,0),(0,float(scy),0,0),(0,0,float(scz),0),(0,0,0,1)) )
        compositeMatrix = sm * compositeMatrix
        
        return compositeMatrix
                
    def getPersCompositeMatrix(self,vrp,vpn,vup,prp,window):
        
        compositeMatrix = np.empty(shape=[0, 4])
        umin = float(window[0])
        umax = float(window[1])
        vmin = float(window[2])
        vmax = float(window[3])
        nmin = float(window[4])
        nmax = float(window[5])
        
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
        oldVup = np.matrix(((float(vup[0]),float(vup[1]),float(vup[2]),1)))
        newVpn = rx*np.transpose(oldVpn)
        newVup = rx*np.transpose(oldVup)
                
        a = float(newVpn[0][0])
        b = float(newVpn[1][0])
        c = float(newVpn[2][0])
        res = c/math.sqrt(a**2 + c**2)
        res1 = a/math.sqrt(a**2 + c**2) 
        ry = np.matrix( ((float(res),0,-float(res1),0),(0,1,0,0),(float(res1),0,float(res),0),(0,0,0,1)) )
        compositeMatrix = ry * compositeMatrix 
        oldVup = np.matrix(((float(newVup[0][0]),float(newVup[1][0]),float(newVup[2][0]),1)))
        newVup = ry*np.transpose(oldVup) 
        
        a = float(newVup[0][0])
        b = float(newVup[1][0])
        c = float(newVup[2][0])
        res = b/math.sqrt(b**2 + a**2)
        res1 = a/math.sqrt(b**2 + a**2)
        rz = np.matrix( ((float(res),-float(res1),0,0),(float(res1),float(res),0,0),(0,0,1,0),(0,0,0,1)) )
        compositeMatrix = rz * compositeMatrix
        
        a = float(prp[0])
        b = float(prp[1])
        c = float(prp[2])
        tcw = np.matrix( ((1,0,0,-a),(0,1,0,-b),(0,0,1,-c),(0,0,0,1)) )
        compositeMatrix = tcw * compositeMatrix
        
        res = (a-((umin+umax)/2))/c
        res1 = (b-((vmin+vmax)/2))/c
        sh = np.matrix( ((1,0,-float(res),0),(0,1,-float(res1),0),(0,0,1,0),(0,0,0,1)) )
        compositeMatrix = sh * compositeMatrix
        
        val = abs(-float(c)+nmax)
        val1 = abs(-float(c)+nmin)
        if val > val1:
            scx = (abs(-float(c)))/(((umax-umin)/2)*(-float(c)+nmax))
            scy = (abs(-float(c)))/(((vmax-vmin)/2)*(-float(c)+nmax))
            scz = 1/(-float(c)+nmax)
        else:
            scx = (abs(-float(c)))/(((umax-umin)/2)*(-float(c)+nmin))
            scy = (abs(-float(c)))/(((vmax-vmin)/2)*(-float(c)+nmin))
            scz = 1(-float(c)+nmin)
        sm = np.matrix( ((float(scx),0,0,0),(0,float(scy),0,0),(0,0,float(scz),0),(0,0,0,1)) )
        compositeMatrix = sm * compositeMatrix
        
        return compositeMatrix
        
    def getNewPoints(self,vertices1,compositeMatrix):
        
        transformedVertices = {}
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
        return transformedVertices
            
    def calculateZmin(self,window,prp):
        
        nmin = float(window[4])
        nmax = float(window[5])
        val = abs(-float(prp[2])+nmax)
        val1 = abs(-float(prp[2])+nmin)
        if val > val1:
            zmin = (-float(prp[2])+nmin)/(-float(prp[2])+nmax)
        else:
            zmin = (-float(prp[2])+nmax)/(-float(prp[2])+nmin)
        return zmin
    
    def drawBoundary(self,canvas,camera,cwidth,cheight):
        
        for i in camera:
            parameters = camera[i]
            label = parameters['i']
            viewport = parameters['s']
            vxmin = float(viewport[0])
            vymin = float(viewport[1])
            vxmax = float(viewport[2])
            vymax = float(viewport[3])
            self.objects.append(canvas.create_rectangle(cwidth*vxmin,cheight*vymin,cwidth*vxmax,cheight*vymax, tag='b'))
            self.objects.append(canvas.create_text(cwidth*vxmin,cheight*vymin,text=label, anchor=NW, tag='b'))
    
    def load_image(self,canvas,fileName):
        f = open(fileName, 'r')
        
        global vertices
        vertices = {}

        global cameraVertices
        cameraVertices = {}
        
        global faces
        faces = []
        
        window = []
        viewport = []
        
        vrp = []
        vpn = []
        vup = []
        prp = []
        
        i = 0;
        for line in f:
            firstLetter = line[:1]
            second = line[2:]
            if firstLetter == 'v':
                i = i+1
                vertices[i] = second.rstrip()
            elif firstLetter == 'f':
                faces.append(second.rstrip())
       
        f.close()
        
        global camera        
        camera = {}
        param = {}
        f = open("cameras_04.txt", 'r')        
        for line in f:
            firstLetter = line[:1]
            second = line[2:]
            if firstLetter == 'c':
                if param:
                    camera[name] = param
                param = {}
            if firstLetter == 'w':
                window = second.rstrip().split( )
                param[firstLetter] = window
            elif firstLetter == 's':
                viewport = second.rstrip().split( )
                param[firstLetter] = viewport
            elif firstLetter == 'r':
                vrp = second.rstrip().split( )
                param[firstLetter] = vrp
            elif firstLetter == 'n':
                vpn = second.rstrip().split( )
                param[firstLetter] = vpn
            elif firstLetter == 'u':
                vup = second.rstrip().split( )
                param[firstLetter] = vup
            elif firstLetter == 'p':
                prp = second.rstrip().split( )
                param[firstLetter] = prp
            elif firstLetter == 'i':
                name = second.rstrip()
                param[firstLetter] = name
            elif firstLetter == 't':
                type1 = second.rstrip()
                param[firstLetter] = type1
        f.close()
        camera[name] = param
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
        
        self.drawBoundary(canvas,camera,cwidth,cheight)
        
        for i in camera:
            parameters = camera[i]
            if parameters['t'] == 'perspective':
                compositeMatrix = self.getPersCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                vertices1 = vertices
                cameraVertices[i] = []
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                zmin = self.calculateZmin(parameters['w'],parameters['p'])
                self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
            else:
                compositeMatrix = self.getCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                vertices1 = vertices
                cameraVertices[i] = []                
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
        
    def redisplay(self,canvas,event):
        
        cwidth = float(event.width)
        cheight = float(event.height)
        canvas.delete('b')
        self.drawBoundary(canvas,camera,cwidth,cheight)
        for i in camera:
            canvas.delete(i);
            parameters = camera[i]
            if not cameraVertices[i]:
                vertices1 = vertices
            else:
                vertices1 = cameraVertices[i]
            if parameters['t'] == 'perspective':
                compositeMatrix = self.getPersCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                zmin = self.calculateZmin(parameters['w'],parameters['p'])
                self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
            else:
                compositeMatrix = self.getCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
                
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
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
            
        for j in range(1,steps+1):
            for i in camera:
                canvas.delete(i);
                transformedVertices1 = {}
                if not cameraVertices[i]:
                    transformedVertices = vertices
                else:
                    transformedVertices = cameraVertices[i]
                for key in transformedVertices:
                    points = transformedVertices[key].split( )
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
                parameters = camera[i]
                if parameters['t'] == 'perspective':
                    compositeMatrix = self.getPersCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                    cameraVertices[i] = transformedVertices1                    
                    transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                    zmin = self.calculateZmin(parameters['w'],parameters['p'])
                    self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
                else:
                    compositeMatrix = self.getCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                    cameraVertices[i] = transformedVertices1                    
                    transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                    self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
            
    def scale_image(self,canvas,scalex,scaley,scalez,steps,point):
        
        scalex = float(scalex)
        scaley = float(scaley)
        scalez = float(scalez)
        
        oscalex = scalex
        oscaley = scaley
            
        if scalex != 1 and scaley != 1:
            
            p = point.split(",")
            steps = float(steps)
            
            if scalex > 1:
                scalex = (scalex - 1)/steps
            elif scalex < 1:
                scalex = scalex/steps
            if scaley > 1:
                scaley = (scaley - 1)/steps
            elif scaley < 1:
                scaley = scaley/steps
            if scalez > 1:
                scalez = (scalez - 1)/steps
            elif scalez < 1:
                scalez = scalez/steps                
            
            steps = int(steps)
            
            cwidth = float(canvas.cget("width"))
            cheight = float(canvas.cget("height"))
        
            tMatrix = np.matrix( ((1,0,0,-float(p[0])),(0,1,0,-float(p[1])),(0,0,1,-float(p[2])),(0,0,0,1)) )
            t_Matrix = np.matrix( ((1,0,0,float(p[0])),(0,1,0,float(p[1])),(0,0,1,float(p[2])),(0,0,0,1)) )
                
            for j in range(1,steps+1):

                if oscalex > 1 and oscaley > 1:
                    sx = 1 + (scalex * j)
                    sy = 1 + (scaley * j)
                    sz = 1 + (scalez * j)
                elif oscalex < 1 and oscaley < 1:
                    sx = 1 - (scalex * j)
                    sy = 1 - (scaley * j)
                    sz = 1 - (scalez * j)
                
                scaleMatrix = np.matrix( ((sx,0,0,0),(0,sy,0,0),(0,0,sz,0),(0,0,0,1)) )
                
                compositeMatrixScale = tMatrix * scaleMatrix * t_Matrix
                for i in camera:
                    
                    canvas.delete(i);
                    transformedVertices1 = {}
                    if not cameraVertices[i]:
                        transformedVertices = vertices
                    else:
                        transformedVertices = cameraVertices[i]
                    for key in transformedVertices:
                        points = transformedVertices[key].split( )
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
                    
                    parameters = camera[i]
                    if parameters['t'] == 'perspective':
                        compositeMatrix = self.getPersCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                        if j == steps:                        
                            cameraVertices[i] = transformedVertices1                    
                        transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                        zmin = self.calculateZmin(parameters['w'],parameters['p'])
                        self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
                    else:
                        compositeMatrix = self.getCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                        if j == steps:                        
                            cameraVertices[i] = transformedVertices1                    
                        transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                        self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
                    
    def translate_image(self,canvas,translatex,translatey,translatez,steps):
        
        translatex = float(translatex)/float(steps)
        translatey = float(translatey)/float(steps)
        translatez = float(translatez)/float(steps)
        
        tMatrix = np.matrix( ((1,0,0,float(translatex)),(0,1,0,float(translatey)),(0,0,1,float(translatez)),(0,0,0,1)) )
        
        steps = int(steps)
    
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
    
        for i in range(1,steps+1):
            for i in camera:
                canvas.delete(i);
                transformedVertices1 = {}
                if not cameraVertices[i]:
                    transformedVertices = vertices
                else:
                    transformedVertices = cameraVertices[i]
                for key in transformedVertices:
                    points = transformedVertices[key].split( )
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
                
                parameters = camera[i]
                if parameters['t'] == 'perspective':
                    compositeMatrix = self.getPersCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                    cameraVertices[i] = transformedVertices1                    
                    transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                    zmin = self.calculateZmin(parameters['w'],parameters['p'])
                    self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
                else:
                    compositeMatrix = self.getCompositeMatrix(parameters['r'],parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                    cameraVertices[i] = transformedVertices1                    
                    transformedVertices = self.getNewPoints(transformedVertices1,compositeMatrix)
                    self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
            
    def fly_image(self,canvas,i,point,point1,steps):
        
        vrp = []
        
        cwidth = float(canvas.cget("width"))
        cheight = float(canvas.cget("height"))
            
        vrp = point.split(",")
        
        canvas.delete(i);
        parameters = camera[i]
        if not cameraVertices[i]:
            vertices1 = vertices
        else:
            vertices1 = cameraVertices[i]
        if parameters['t'] == 'perspective':
            compositeMatrix = self.getPersCompositeMatrix(vrp,parameters['n'],parameters['u'],parameters['p'],parameters['w'])
            transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
            zmin = self.calculateZmin(parameters['w'],parameters['p'])
            self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
        else:
            compositeMatrix = self.getCompositeMatrix(vrp,parameters['n'],parameters['u'],parameters['p'],parameters['w'])
            transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
            self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
                        
        p = point1.split(",")
        x = float(p[0])/float(steps)
        y = float(p[1])/float(steps)
        z = float(p[2])/float(steps)
        totalx = 0
        totaly = 0
        totalz = 0
        steps = int(steps)
        for j in range(1,steps+1):
            canvas.delete(i);
            vrp = []
            totalx = float(totalx) + float(x)
            totaly = float(totaly) + float(y)
            totalz = float(totalz) + float(z)
            vrp.append(float(totalx))        
            vrp.append(float(totaly))
            vrp.append(float(totalz))
            if parameters['t'] == 'perspective':
                compositeMatrix = self.getPersCompositeMatrix(vrp,parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                zmin = self.calculateZmin(parameters['w'],parameters['p'])
                self.plotPersPoints(canvas,i,cwidth,cheight,zmin,parameters['s'],transformedVertices)
            else:
                compositeMatrix = self.getCompositeMatrix(vrp,parameters['n'],parameters['u'],parameters['p'],parameters['w'])
                transformedVertices = self.getNewPoints(vertices1,compositeMatrix)
                self.plotPoints(canvas,i,cwidth,cheight,parameters['s'],transformedVertices)
        parameters['r'] = vrp
        camera[i] = parameters