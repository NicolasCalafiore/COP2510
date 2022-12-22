# Nicolas Calafiore
# U94446501

# Program asks for two inputs (sides and length)
# For the amount of sides the program loops, draws one side, turns at the predetermined angle using the formula given, and repeats until all sides have been accounted for

import turtle

sides = int(input("Enter the number of sides between 3 and 12 (inclusive):"))
while sides <= 2 or sides > 12:
    sides = int(input("Invalid number of sides. Enter a number between 3 and 12 (inclusive):"))

length = int(input("Enter the length of each side (> 50)"))
while length <= 50:
    length = int(input("Please enter a larger length of each side:"))

angle = ((sides - 2) * 180) / sides

turtle = turtle.Turtle()
# turtle.shape('turtle')

currentSide = 0

while(currentSide < sides):
    turtle.forward(length)
    turtle.right(180 - angle)
    currentSide += 1

shapeType = ''

if sides == 1:
    shapeType = 'Monogon'
elif sides == 2:
    shapeType = 'Digon'
elif sides == 3:
    shapeType = 'Triangle'
elif sides == 4:
    shapeType = 'Quadrilateral'
elif sides == 5:
    shapeType = 'Pentagon'
elif sides == 6:
    shapeType = 'Hexagon'
elif sides == 7:
    shapeType = 'Heptagon'
elif sides == 8:
    shapeType = 'Octogon'
elif sides == 9:
    shapeType = 'nonagon'
elif sides == 10:
    shapeType = 'Decagon'
elif sides == 11:
    shapeType = 'Hendecagon'
elif sides == 12:
    shapeType = 'Dodecagon'
else:
    shapeType = 'Error'

turtle.write(shapeType)



