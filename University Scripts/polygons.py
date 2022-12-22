## Nicolas Calafiore
## U94446501
## Retrieves 2 variables from input --> Initializes a new Polygon object with sides and length = 0 --> uses the setSides and setLength methods to update the objects variables --> uses the get functions to retrieve the data and print it

import math


class Polygon:
    def __init__(self):
        self.sides = 0
        self.length = 0

    def getPerimeter(self):
        return self.sides * self.length

    def getSides(self):
        return self.sides

    def setSides(self, sides):
        self.sides = sides

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getArea(self):
        return (self.sides * self.length ** 2) / (4 * math.tan(math.pi / self.sides))


def main():
    sides = int(input("Enter the number of sides (>=3): "))
    while (sides < 3):
        sides = int(input("Invalid entry. Re-enter the number of sides (>=3): "))

    length = float(input("Enter the length of each sides (>= 0.1): "))
    while (length < .1):
        length = float(input("Invalid entry. Re-enter the length of each sides (>= 0.1): "))

    shape = Polygon()
    shape.setSides(sides)
    shape.setLength(length)

    print("The polygon has", str(shape.getSides()),"sides .Each side is", shape.getLength(),"units in length.")
    print("The perimeter of the polygon is", "{:.3f}".format(shape.getPerimeter()),"units and its area is", "{:.3f}".format(shape.getArea()), "square units.")


if __name__ == "__main__":
    main()
