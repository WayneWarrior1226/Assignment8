#Created by Veronica Dean on 3/10/2022
from tkinter import *
import os
import turtle
import random

#Declare random variables

#Create Display Window
window = Tk()
window.geometry('400x500')
window.title('Mad Gen')
Label(window, text= 'TKINTER APP' , font = 'Helvetica 20 bold').pack()
Label(window, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)


#MadLib game

def madlib1():
	animal=input('enter an animal name : ')
	profession = input('enter a profession name: ')
	cloth = input('enter a piece of cloth name: ')
	things = input('enter a thing name: ')
	name = input('enter a name: ')
	place = input('enter a place name: ')
	verb = input('enter a verb in ing form: ')
	food = input('food name: ')
	print('say ' + food + ', the photographer said as the camera flashed! ' + name + ' and I had gone to ' + place +' to get our photos taken on my birthday. The first photo we really wanted was a picture of us dressed as ' + animal + ' pretending to be a ' + profession + '. when we saw the second photo, it was exactly what I wanted. We both looked like ' + things + ' wearing ' + cloth + ' and ' + verb + ' --exactly what I had in mind')

#Random Polygon
	
def randompoly():
        tr = turtle.Turtle()
        for i in range(9):
                tr.forward(100)
                tr.right(40)
        tr.end()
                                 

def polygon(sides, length):
        sides = int(input("How many sides do you want? Use digits: "))
        length = int(input("Length of the sides of polygon?"))
        colorname = input("Color of the polygon?" )
        fcolor = input("Fill color of polygon?" )

        tr.color = (colorname)
        tr.fillcolor = (fcolor)
    
        for x in range(int(sides)):
                tr.forward(int(length))
                tr.left(int(360/sides))
        tr.end()

def quit_program():
	exit()

#Add and Place buttons

Button(window, text = 'Madlibs game', font = 'arial 15', command = madlib1, bg = 'ghost white').place(x=60, y=120)
Button(window, text = 'Draw a random polygon', font = 'arial 15', command = randompoly, bg = 'ghost white').place(x=70, y=180)
Button(window, text = 'Draw a specific polygon', font ='arial 15', command = polygon, bg = 'ghost white').place(x=80, y=240)
Button(window, text="QUIT", font = ('Helvetica 13 bold'), foreground = "Green", background = "Yellow", command=quit_program).place(x=80, y=280)



window.mainloop()
