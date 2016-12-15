'''
Name: Harry Brown III
Program: Sine and Cosine Graph System for Turtle
Date: 6/30/16
'''

import math
import turtle

def sinWave(t):
    t.pencolor('blue')
    t.up()
    for x in range(360, 0, -1):
        y = math.sin(math.radians(-x))
        t.goto(-x, y *80)
        t.down()
        
    for x in range(0, 360):
        y = math.sin(math.radians(x))
        t.goto(x, y *80)
        
def cosWave(t):
    t.pencolor('red')
    t.up()
    for x in range(360, 0, -1):
        y = math.cos(math.radians(-x))
        t.goto(-x, y * 80)
        t.down()
    
    for x in range(360):
        y = math.cos(math.radians(x))
        t.goto(x, y * 80)

def reset(t, x, y):
    t.up()
    t.goto(x, y)
    t.down()
        
def arrow(t):
    t.forward(20)
    t.backward(20)

def arrows(t, x, y):
    t.left(140)
    arrow(t)
    t.right(270)
    arrow(t)
    reset(t, x, y)

def drawGraph(t, txt, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.forward(380)
    txt.up()
    txt.goto(325, -20)
    txt.down()
    txt.write('2π', font=('Arial', 12))
    arrows(t, x, y)

    t.right(140)
    t.forward(300)
    arrows(t, x, y)

    t.left(220)
    t.forward(380)
    txt.up()
    txt.goto(-350, -20)
    txt.down()
    txt.write('-2π', font=('Arial', 12))
    arrows(t, x, y)


    t.left(220)
    t.forward(300)
    arrows(t, x, y)

def legend(txt):
    txt.up()
    txt.goto(200, -270)
    txt.down()
    txt.color('blue')
    txt.write('- Sine', font=('Arial', 25))
    txt.up()
    txt.goto(200, -300)
    txt.down()
    txt.color('red')
    txt.write('- Cosine', font=('Arial', 25))


def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(10)
    
    txt = turtle.Turtle()
    txt.hideturtle()

    x , y = 0, 0

    drawGraph(t, txt, x, y) #draw graph
    sinWave(t) #draw sine
    reset(t, x, y) #reset coordinates
    cosWave(t) #draw cosine

    legend(txt) #write legend

    
#call main function
main()



    
