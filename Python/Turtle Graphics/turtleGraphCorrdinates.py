'''
Name: Harry Brown III
Program: Graph Coordinate System for Turtle
Date: 6/30/16
'''

import turtle

def drawChart(t):
    t.pensize(3)
    for x in range(4):
        t.forward(400)
        t.up()
        t.backward(400)
        t.down()
        t.left(90)

def drawX(t):
    t.up()
    t.pensize(1)
    for k in range(-400, 400, 40):
        t.goto(k, -10)
        t.down()
        t.left(90)
        t.forward(20)
        t.up()
        if k != 0:
            t.goto(k, -25)
            t.write(str(k), align='center', font=('Arial', 8))
        t.right(90)

def drawY(t):
    t.up()
    t.pensize(1)
    for k in range(400, -400, -40):
        t.goto(-10, k)
        t.down()
        t.forward(20)
        t.left(90)
        t.up()
        if k != 0:
            t.goto(15, k-5)
            t.write(str(k), font=('Arial', 8))
        t.right(90)

def plot(t):
    t.up()
    t.goto(-200, 60)
    t.down()
    t.dot()

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    
    drawChart(t)
    drawX(t)
    drawY(t)

#call main
main()
        
