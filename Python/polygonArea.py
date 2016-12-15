'''
Name: Harry Brown III
Program: Polygon Area
Date: 6/6/16
'''

import math

#get user input for polygon
sides = int(input('Enter the number of sides: '))
length = eval(input('Enter the side length: '))

#calculate area
s = length ** 2
area = float((sides * s)/(4 *(math.tan(math.pi/sides))))

#concatinate strings
out = '\n\nThe number of sides is: ' + str(sides) + '\n' + \
      'The length of each side is: ' + str(length) + '\n' + \
      '\n\nThe area of the polygon is: ' + str(format(area, '.2f'))

#display output
print(out)
      
      
