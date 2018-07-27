#reflection 3D
# -*- coding: utf-8 -*-
from tkinter import *
from math import sqrt
from math import sin, cos, radians, pi

points = []
def conv3Dto2D(x,y,z):
	z = z/sqrt(2)
	x = ox+(x-z)
	y = oy-(y-z)
	return x,y

def cubedrawing(cubepoints,outline = 'black'):
	for i in range (len(cubepoints)):	
		points.insert(i,conv3Dto2D(cubepoints[i][0],cubepoints[i][1],cubepoints[i][2]))
		win.create_text(points[i],text=str(i),font="Times 10 bold")
	print (str(points)+"\n")
	win.create_rectangle(points[0],points[2],outline=outline)	
	win.create_rectangle(points[4],points[6],outline=outline)	
	win.create_line(points[0],points[4],fill=outline)
	win.create_line(points[1],points[5],fill=outline)
	win.create_line(points[2],points[6],fill=outline)
	win.create_line(points[3],points[7],fill=outline)	

def translation(x,y,z):
        
	T = 	[[1, 0, 0, tx],
		 [0, 1, 0, ty],
		 [0, 0, 1, tz],
		 [0, 0, 0, 1]]
	P =     [[x],
		[y],
		[z],
		[1]]

	result= [[0],
	  	 [0],
	   	 [0],
		 [0]]

	for i in range(len(T)):
		for j in range(len(P[0])):
			for k in range(len(P)):
				result[i][j] += T[i][k] * P[k][j]
	return result[0][0],result[1][0],result[2][0]

print("Enter the width,height and depth of cube")
w,h,d = map(int,input().split())
print ("enter the center coordinates xc yc")
xc,yc = map(int,input().split())
zc = 0
print("Enter translation factor tx, ty, tz")
tx,ty,tz = map(int,input().split())
master = Tk()
canvas_width = master.winfo_screenwidth()
canvas_height = master.winfo_screenheight()
win = Canvas(master,width = canvas_width,height = canvas_height)
win.pack()

#Origin
ox,oy = canvas_width/2,canvas_height/2

#Axes
win.create_line(ox,0,ox,oy)
win.create_line(ox,oy,ox*2,oy)
win.create_line(ox,oy,0,oy*2)

#Cube_points
cubepoints = [(0,0,0) , (w,0,0) , (w,h,0) , (0,h,0) , (0,0,d) , (w,0,d) , (w,h,d) , (0,h,d)]

#Displacing_cubes_by_(xc,yc)
cubepointsnew = []
for i in range(len(cubepoints)):
	cubepointsnew.insert(i,(cubepoints[i][0]+xc,cubepoints[i][1]+yc,cubepoints[i][2]+zc))
cubedrawing(cubepointsnew)
win.create_text(points[1],text="Original cube",font="Times 10 bold")

#Calculating_points_after_translation
pointsx = []
for i in range(len(points)):
	pointsx.insert(i,translation(cubepointsnew[i][0],cubepointsnew[i][1],cubepointsnew[i][2]))
print (pointsx)
cubedrawing(pointsx,'red')
win.create_text(points[1],text="Cube after translation",font="Times 10 bold")
mainloop()




     
