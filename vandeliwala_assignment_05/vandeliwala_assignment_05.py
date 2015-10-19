# Vandeliwala, Ismail
# 1000-990-475
# 2015-03-23
# Assignment_05

import sys
import math

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *

camera = {}
Angle = 0
rx = 0
ry = 0
rz = 0
Scale = 1
s = 0
      
def display():
    
    global Angle
    global rx
    global ry
    global rz
    global camera
    global Scale
    global s
      
    w=glutGet(GLUT_WINDOW_WIDTH)
    h=glutGet(GLUT_WINDOW_HEIGHT)
      
    glEnable(GL_SCISSOR_TEST)
    for i in camera:
        parameters = camera[i]
        window = parameters['w']
        viewport = parameters['s']
        eye = parameters['e']
        look = parameters['l']
        up = parameters['u']
        if parameters['t'] == 'perspective':
            glScissor(int(float(viewport[0])*w),int((1-float(viewport[3]))*h),int((float(viewport[2])-float(viewport[0]))*w),int((float(viewport[3])-float(viewport[1]))*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glFrustum(float(window[0]),float(window[1]),float(window[2]),float(window[3]),float(window[4]),float(window[5]))
            gluLookAt(float(eye[0]),float(eye[1]),float(eye[2]),float(look[0]),float(look[1]),float(look[2]),float(up[0]),float(up[1]),float(up[2]))
            glMatrixMode(GL_MODELVIEW)    
            glViewport(int(float(viewport[0])*w),int((1-float(viewport[3]))*h),int((float(viewport[2])-float(viewport[0]))*w),int((float(viewport[3])-float(viewport[1]))*h))
            glCallList(1) 
        else:
            glScissor(int(float(viewport[0])*w),int((1-float(viewport[3]))*h),int((float(viewport[2])-float(viewport[0]))*w),int((float(viewport[3])-float(viewport[1]))*h))
            glClearColor(0.4,0.4,0.6,0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(float(window[0]),float(window[1]),float(window[2]),float(window[3]),float(window[4]),float(window[5]))
            gluLookAt(float(eye[0]),float(eye[1]),float(eye[2]),float(look[0]),float(look[1]),float(look[2]),float(up[0]),float(up[1]),float(up[2]))
            glMatrixMode(GL_MODELVIEW)    
            glViewport(int(float(viewport[0])*w),int((1-float(viewport[3]))*h),int((float(viewport[2])-float(viewport[0]))*w),int((float(viewport[3])-float(viewport[1]))*h))
            glCallList(1) 
            
    glFlush()
    glutSwapBuffers()
    
    if rx == 1:
        glRotated(Angle,1,0,0)
    elif ry == 1:
        glRotated(Angle,0,1,0)
    elif rz == 1:
        glRotated(Angle,0,0,1)
     
    if s == 1:
        s = 0
        glScalef(Scale,Scale,Scale)
    
def cross(a, b):
    c = [float(a[1])*float(b[2]) - float(a[2])*float(b[1]),
         float(a[2])*float(b[0]) - float(a[0])*float(b[2]),
         float(a[0])*float(b[1]) - float(a[1])*float(b[0])]

    return c
    
def load():
    
    global Angle
    global rx
    global ry
    global rz
    global Scale
    global s
    
    Angle = 0
    rx = 0
    ry = 0
    rz = 0
    Scale = 1
    s = 0
    
    vertices = {}
    faces = []
    f = open(fileName, 'r')
    i = 0
    
    for line in f:
        firstLetter = line[:1]
        second = line[2:]
        if firstLetter == 'v':
            i = i+1
            vertices[i] = second.rstrip()
        elif firstLetter == 'f':
            faces.append(second.rstrip())
    f.close()
    
    glNewList(1,GL_COMPILE)
    glColor3f(0,1,0)
    for key in faces:
        connection = key.split( )
        glBegin(GL_LINE_LOOP)
        for face in connection:
            point = vertices[int(face)].split( )
            glVertex3f(float(point[0]),float(point[1]),float(point[2]))
        glEnd()   
    glEndList()
    
    global camera        
    camera = {}
    param = {}
    f = open("cameras_05.txt", 'r')        
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
        elif firstLetter == 'e':
            eye = second.rstrip().split( )
            param[firstLetter] = eye
        elif firstLetter == 'l':
            look = second.rstrip().split( )
            param[firstLetter] = look
        elif firstLetter == 'u':
            vup = second.rstrip().split( )
            param[firstLetter] = vup
        elif firstLetter == 'i':
            name = second.rstrip()
            param[firstLetter] = name
        elif firstLetter == 't':
            type1 = second.rstrip()
            param[firstLetter] = type1
    f.close()
    camera[name] = param
    
    for i in camera:
        parameters = camera[i]
        eye = parameters['e']
        look = parameters['l']
        up = parameters['u']
        vpn = []
        n1 = []
        u1 = []
        v1 = []
        
        d = math.sqrt((abs(float(eye[0]) - float(look[0])) ** 2) + (abs(float(eye[1]) - float(look[1])) ** 2) + (abs(float(eye[2]) - float(look[2])) ** 2))
        d1 = d * 0.05
        vpn.append(float(look[0]) - float(eye[0]))
        vpn.append(float(look[1]) - float(eye[1]))
        vpn.append(float(look[2]) - float(eye[2]))
        
        denom = math.sqrt(vpn[0] ** 2 + vpn[1] ** 2 + vpn[2] ** 2)
        n1.append(vpn[0]/denom)
        n1.append(vpn[1]/denom)
        n1.append(vpn[2]/denom)
        
        n1[0] = n1[0] * d1
        n1[1] = n1[1] * d1
        n1[2] = n1[2] * d1
        
        parameters['n1'] = n1
        camera[i] = parameters
        
        u = cross(vpn,up)
        
        denom = math.sqrt(u[0] ** 2 + u[1] ** 2 + u[2] ** 2)
        u1.append(u[0]/denom)
        u1.append(u[1]/denom)
        u1.append(u[2]/denom)
        
        u1[0] = u1[0] * d1
        u1[1] = u1[1] * d1
        u1[2] = u1[2] * d1
        
        parameters['u1'] = u1
        camera[i] = parameters
        
        v = cross(vpn,u)
        
        denom = math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)
        v1.append(v[0]/denom)
        v1.append(v[1]/denom)
        v1.append(v[2]/denom)
        
        v1[0] = v1[0] * d1
        v1[1] = v1[1] * d1
        v1[2] = v1[2] * d1
        
        parameters['v1'] = v1
        camera[i] = parameters
        
    
def keyHandler(Key, MouseX, MouseY):
    global Angle
    global rx
    global ry
    global rz
    global fileName
    global Scale
    global s
    if Key == b'n' or Key == b'N':
        fileName = input("Enter filename: ")
        load()
    elif Key == b'd' or Key == b'D':
        display()
    elif Key == b'x' or Key == b'X':
        rx = 1
        ry = 0
        rz = 0
        s = 0
        if Key == b'x':
            Angle = 5
        else:
            Angle = -5
        display()
    elif Key == b'y' or Key == b'Y':
        rx = 0
        ry = 1
        rz = 0
        s = 0
        if Key == b'y':
            Angle = 5
        else:
            Angle = -5
        display()
    elif Key == b'z' or Key == b'Z':
        rx = 0
        ry = 0
        rz = 1
        s = 0
        if Key == b'z':
            Angle = 5
        else:
            Angle = -5
        display()
    elif Key == b's' or Key == b'S':
        rx = 0
        ry = 0
        rz = 0
        if Key == b's':
            Scale = 1.05
        else:
            Scale = 0.95
        s = 1
        display()
    elif Key == b'f' or Key == b'b':
        rx = 0
        ry = 0
        rz = 0
        s = 0
            
        if Key == b'f':
            for i in camera:
                parameters = camera[i]
                eye = parameters['e']
                add = parameters['n1']
                newEye = []
                newEye.append(float(eye[0])+float(add[0]))
#                newEye.append(float(eye[1]))
#                newEye.append(float(eye[2]))
                newEye.append(float(eye[1])+float(add[1]))
                newEye.append(float(eye[2])+float(add[2]))
                parameters['e'] = newEye
        else:
            for i in camera:
                parameters = camera[i]
                eye = parameters['e']
                sub = parameters['n1']
                newEye = []
                newEye.append(float(eye[0])-float(sub[0]))
#                newEye.append(float(eye[1]))
#                newEye.append(float(eye[2]))
                newEye.append(float(eye[1])-float(sub[1]))
                newEye.append(float(eye[2])-float(sub[2]))
                parameters['e'] = newEye
        display()
    elif Key == b'p':
        rx = 0
        ry = 0
        rz = 0
        s = 0
            
        for i in camera:
            parameters = camera[i]
            if parameters['t'] == 'parallel':
                parameters['t'] = 'perspective'
            else:
                parameters['t'] = 'parallel'    
            
        display()
    elif Key == b'q' or Key == b'Q':
        print ("Bye")
        sys.exit()
        
def specialHandler(Key, MouseX, MouseY):
    
    global rx
    global ry
    global rz
    global s
    
    if Key == GLUT_KEY_UP or Key == GLUT_KEY_DOWN or Key == GLUT_KEY_LEFT or Key == GLUT_KEY_RIGHT:
        rx = 0
        ry = 0
        rz = 0
        s = 0
            
        if Key == GLUT_KEY_UP or Key == GLUT_KEY_LEFT:
            for i in camera:
                parameters = camera[i]
                eye = parameters['e']
                if Key == GLUT_KEY_UP:
                    add = parameters['u1']
                elif Key == GLUT_KEY_LEFT:
                    add = parameters['v1']
                newEye = []
                newEye.append(float(eye[0])+float(add[0]))
                newEye.append(float(eye[1])+float(add[1]))
                newEye.append(float(eye[2])+float(add[2]))
                parameters['e'] = newEye
        else:
            for i in camera:
                parameters = camera[i]
                eye = parameters['e']
                if Key == GLUT_KEY_DOWN:
                    sub = parameters['u1']
                elif Key == GLUT_KEY_RIGHT:
                    sub = parameters['v1']
                newEye = []
                newEye.append(float(eye[0])-float(sub[0]))
                newEye.append(float(eye[1])-float(sub[1]))
                newEye.append(float(eye[2])-float(sub[2]))
                parameters['e'] = newEye
        display()

def reshape(w, h):
    global rx
    global ry
    global rz
    global s
    rx = 0
    ry = 0
    rz = 0
    s = 0
    display()
                 
global fileName
fileName = 'pyramid_05.txt'

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
glutInitWindowSize(800, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"PyOpenGL Demo")
glClearColor(1,1,0,0)
glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
glEnable(GL_DEPTH_TEST)
glDepthFunc(GL_LESS);
glutDisplayFunc(display)
glutKeyboardFunc(keyHandler)
glutSpecialFunc(specialHandler)
glutReshapeFunc(reshape)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glMatrixMode(GL_MODELVIEW)
load()
glutMainLoop()


