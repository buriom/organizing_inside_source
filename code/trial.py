from math import sqrt,pi
import turtle
import csv

def get_side_square(area):
  side = sqrt(area)
  return side

def get_side_equilateral(area):
  side = sqrt(4*area/sqrt(3))
  return side


def get_side_circle(area):
  radius = sqrt(area/pi)
  return radius


def get_side_golden(area):
  side =sqrt(area/1.618)
  return side

def draw_square (side,color,a,b):
	turtle.penup()
	turtle.setpos(a,b)
	turtle.pendown()
	turtle.color(color)
	turtle.begin_fill()
	turtle.forward(side)
	turtle.left(90)
	turtle.forward(side)
	turtle.left(90)
	turtle.forward(side)
	turtle.left(90)
	turtle.forward(side)
	turtle.left(90)
	turtle.end_fill()

def draw_equilateral (side,color,a,b):
	turtle.penup()
	turtle.setpos(a,b)
	turtle.pendown()
	turtle.color(color)
	turtle.begin_fill()
	turtle.forward(side)
	turtle.left(120)
	turtle.forward(side)
	turtle.left(120)
	turtle.forward(side)
	turtle.left(120)
	turtle.end_fill()

def draw_circle (side,color,a,b):
	turtle.penup()
	turtle.setpos(a,b)
	turtle.pendown()
	turtle.color(color)
	turtle.begin_fill()
    	turtle.circle(side)    # Draw a circle
	turtle.end_fill()

def draw_golden (side,color,a,b):
	turtle.penup()
	turtle.setpos(a,b)
	turtle.pendown()
	turtle.color(color)
	turtle.begin_fill()
	turtle.forward(side*1.618)
	turtle.left(90)
	turtle.forward(side)
	turtle.left(90)
	turtle.forward(side*1.618)
	turtle.left(90)
	turtle.forward(side)
	turtle.left(90)
	turtle.end_fill()
	
def genfun():
	area = input("Enter the area: ")
	color = raw_input('Enter the fill color: ')
	a = input('Enter the x coordinate of the origin: ')
	b = input('Enter the y coordinate of the origin: ')
	shape = raw_input('Enter the shape: ')
	if shape == "SQUARE":
		draw_square (get_side_square(area),color,a,b)
	elif shape == "TRIANGLE":
		draw_equilateral (get_side_equilateral(area),color,a,b)
	elif shape == "CIRCLE":
		draw_circle (get_side_circle(area),color,a,b)
	elif shape == "RECTANGLE":
		draw_golden (get_side_golden(area),color,a,b)
	else:
		print "wrong choice for shape"

def genfun1(shape,area,color,a,b):
	if shape == "SQUARE":
		draw_square (get_side_square(area),color,a,b)
	elif shape == "TRIANGLE":
		draw_equilateral (get_side_equilateral(area),color,a,b)
	elif shape == "CIRCLE":
		draw_circle (get_side_circle(area),color,a,b)
	elif shape == "RECTANGLE":
		draw_golden (get_side_golden(area),color,a,b)
	else:
		print "wrong choice for shape"
		
import csv

with open('day1.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
	shape = row[1]; area = float(row[0]); color = row[2]; a =float(row[3]); b= float(row[4])
	#print row[2]
	#genfun1("row[1]",row[0],"row[2]",row[3],row[4])            
	genfun1(shape,area,color,a,b)
