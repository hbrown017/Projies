'''
Name: Harry Brown III
Program: Multiplication Table using Turtle
Date: 6/29/16
'''

import turtle

def table(t, s):
    t.up()
    t.goto(s,70)
    t.down()
    t.forward(300) #horizontal line
    t.up()
    t.goto(s, 110)
    t.down()
    t.write('  ' + 'Multiplication Table', font=('Arial', 20, 'bold'))
    t.up()
    t.goto(s,70)
    t.down()
    t.right(90)
    t.forward(220) #vertical line

def multiplication(t, s):
    t.up()
    
    #print the top row
    x = s+10
    for j in range(10):

        t.goto(x, 80)
        t.write(str(j + 1), font=('Arial', 12))
        x += 30

    y, x = 50, s+10
    
    #print number columns
    for l in range(10):
        t.goto(s-20, y)
        t.write(str(l + 1), font=('Arial', 12))
        for j in range(10):
            t.goto(x, y)
            t.write(str((l + 1) * (j + 1)), font=('Arial', 12))
            x += 30
        y -= 22
        x = s+10

def main():
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    #call table function
    table(t, -150)
    
    #create multiplication table
    multiplication(t, -150)

#call main function
main()
