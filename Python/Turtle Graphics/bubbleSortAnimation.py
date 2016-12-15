'''
Name: Harry Brown III
Program: Bubble Sort using Turtle
Date: 6/20/16
'''

import turtle

def drawHistogram(t, list):
    t.speed(10) #0(fastest), 10(fast), 6(normal), 3 (slow)
    t.hideturtle()

    height = 100 #histogram height
    width = 400 #histogram width

    #draw bottom line for histogram
    t.up()
    t.goto(-width / 2, -height / 2)
    t.down()
    t.forward(width)

    #set bar width
    barWidth = width / len(list)

    #draw bars
    for i in range(len(list)):     
        h = list[i] * height / max(list)
        x = -width/2 + i * barWidth
        y = -height/2
        drawBar(t, list, i, x, y, barWidth, h)     

    #t.hideturtle()

def drawBar(t, list, i, x, y, barWidth, h):
    
    t.up()
    t.goto(x, y)
    t.setheading(90)
    t.down()

    t.forward(h)
    t.write(' ' + str(list[i]), align='left', font=('Arial', 18))
    t.right(90)
    t.forward(barWidth)
    t.right(90)
    t.forward(h)


def BubbleSort(t, n):
    count = 0
    listIt = 0
    t.hideturtle()
 
    for x in range(0, len(n)-3):
        for y in range(0, len(n)-1):
            if n[y] > n[y+1]:
                swap(t)
                drawHistogram(t, [(n[y]), (n[y+1])]) #display values to be swapped
                
                n[y], n[y+1] = n[y+1], n[y] #swap values

                swapping(t)
                drawHistogram(t, n)
                count += 1
            
        listIt += 1    
        #show list changes when swapped
        swapProcess(t, n, listIt)       
    return count

def unsorted(t):
    t.hideturtle()
    t.up()
    t.goto(0,200)
    t.write('Original list: ', align = 'center', font=('Arial', 30))
    
def swap(t):
    t.reset()
    t.hideturtle()
    t.color('red')
    t.up()
    t.goto(0,200)
    t.write('Needs Swapping: ', align = 'center', font=('Arial', 30))

def swapping(t):
    t.reset()
    t.hideturtle()
    t.color('red')
    t.up()
    t.goto(0,200)
    t.write('Swapping: ', align = 'center', font=('Arial', 30))

def sortedList(t):
    t.hideturtle()
    t.color('green')
    t.up()
    t.goto(0,200)
    t.write('Your list is now sorted: ', align = 'center', font=('Arial', 30))

def iterations(t, count):
    t.hideturtle()
    t.color('green')
    t.up()
    t.goto(0,-200)
    t.write('Total swaps performed: ' + str(count), align = 'center', font=('Arial', 30))

def swapProcess(t, n, it):
    t.reset()
    t.hideturtle()
    t.color('green')
    t.up()
    t.goto(0,-200)
    t.write('Full list iteration: #' + str(it), align = 'center', font=('Arial', 30))
    drawHistogram(t, n) #display swaped values
    t.reset()

def main():
    t = turtle.Turtle()
    
    #list = [32, 23, 45, 34, 4, 90, 23, 25] #create a list of numbers
    num = [1,8,-4,2,16,5,13,9,-2,12,6,17,7,19,4,10,3,2,11,14]

    unsorted(t)
    drawHistogram(t, num)
    t.reset()

    count = BubbleSort(t, num)

    sortedList(t)
    drawHistogram(t, num)
    iterations(t, count)

main()
