'''
Name: Harry Brown III
Program: Star with fillcolor
Date: 6/19/16
'''

import turtle

def draw(t, x, y, side):
    t.speed(10)
    t.pencolor('red')
    t.up()
    t.goto(x,y)
    
    t.left(36)
    t.down()
    t.pencolor('red')
    t.fillcolor('light blue')
    t.begin_fill()
    
    for i in range(36):
        t.forward(side)
        t.left(170)
    t.end_fill()

def main():
    t = turtle.Turtle()
    t.hideturtle()
    draw(t, 0,0, 200)

#call main
main()
