'''
Name: Harry Brown III
Program: Line Graph
Date: 6/22/16
'''

import turtle

#draw line graph
def startPoint(t, list):
    i = 0
    t.up()
    t.goto(-120, -30)
    t.up()
    t.goto(-120, list[1])
    t.down()
    t.dot()
    t.goto(-120+60, list[2])
    t.write(list[0], align='center', font=('Arial', 12))
    i += 60
    return i

def main():

    t = turtle.Turtle()
    text = turtle.Turtle()
    t.hideturtle()
    text.hideturtle()

    text.color('blue')

    goals = ['Freshman Life Goals (% of students commited to goal)',
             1978, 1988, 1998, 2008]

    finance = ['Well off financially', 59, 74, 73, 77]
    life = ['Meaningful philosophy of life', 60, 43, 44, 51]

    #set up x axis
    t.up()
    t.goto(-180, -50)
    t.down()

    #draw x axis
    for i in range(5):
        t.forward(60)
        t.left(90)
        t.forward(10)
        t.backward(10)
        t.right(90)

    #draw x axis values
    x = -180
    for i in range(1, 5):
        x += 60
        text.up()
        text.goto(x, -70)
        text.down()
        text.write(goals[i], align='center', font=('Arial', 12))

    #draw text under x axis
    text.up()
    text.goto(0, -95)
    text.down
    text.write(goals[0], align='center', font=('Arial', 12))

    #set up y axis
    t.up()
    t.goto(-180, -50)
    t.down()

    #draw y axis
    t.left(90)
    for i in range(3):
        t.forward(80)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(90)

    #set up y axis values
    y = -50
    for i in range(2, 0, -1):
        y += 75
        text.up()
        text.goto(-190, y)
        text.down()
        text.write(life[i], align='center', font=('Arial', 12))

    #plot points on graph
    i = startPoint(t, finance)
    for x in range(2, 5):
        t.goto(-120+i, finance[x])
        t.dot()
        i += 60

    #i = startPoint(t, life)
    i = 0
    t.up()
    t.goto(-120, -30)
    t.up()
    t.goto(-120, life[1])
    t.down()
    t.dot()
    i += 60
    t.down()
    for x in range(2, 5):
        t.goto(-120+i, life[x])
        t.dot()
        i += 60

    t.up()
    t.goto(-120+90, 20)
    t.write(life[0], align='center', font=('Arial', 12))

main()
