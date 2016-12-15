'''
Name: Harry Brown III
Program: Fractal Design
Date: 6/28/16
'''

import turtle

def drawli(t, x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2,y2)
    t.up()


def fractal(t, x1, y1, x2, y2, level):
    if level == 0:
        drawli(t, x1, y1, x2, y2)
    else:
        newX = ((x1+x2)/2) + ((y2-y1)/2)
        newY = ((y1+y2)/2) - ((x2-x1)/2)
        level -= 1
        fractal(t, x1, y1, newX, newY, level)
        fractal(t, newX, newY, x2, y2, level)
        
def main():
    t = turtle.Turtle()
    t.pencolor('red')
    t.speed(0)
    level = 12
    fractal(t, -200, 0, 200, 0, level)

main()
