## Nicolas Calafiore
## U94446501
##
## Accepts 3 inputs that are used in calculations
## Variables are then assigned a final variable that is equal to its respective variable and its correct equation
## Print


import math
while True:
    firstDiagonal = float(input("Enter Diagonal #1: "));
    secondDiagonal = float(input("Enter Diagonal #2: "));
    radius = float(input("Enter Radius: "));

    kiteArea = float((firstDiagonal*secondDiagonal)/2);
    circleArea = float((math.pi) * (radius*radius));
    totalArea = kiteArea - circleArea;

    print("\nThe total area is ",round(totalArea,3), "square units.\n");

