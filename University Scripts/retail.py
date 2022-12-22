## U94446501
## Nicolas Calafiore
## Gets 6 variables from input --> Creates two Retai_Item objects and assigns 3 variables each during initialization --> prints header --> calls the __str__ method for both objects which outputs the data using advance string formatting

class Retail_Item:
    def __init__(self, type, amount, price):
        self.type = type
        self.amount = amount
        self.price = price


    def __str__(self):
        print(f'{self.type:28} {self.amount:13} ${self.price:5}')




def main():
    type = str(input("Name of item 1: "))
    amount = str(input("Amount of item 1: "))
    price = str(input("Price of item 1: "))
    print()
    type2 = str(input("Name of item 2: "))
    amount2 = str(input("Amount of item 2: "))
    price2 = str(input("Price of item 2: "))
    print()
    item1 = Retail_Item(type, amount, price)
    item2 = Retail_Item(type2, amount2, price2)
    print()
    print("Here is a summary of the items you added:")
    print("Item                       Amount          Price")
    print("---------------------------------------------------")
    item1.__str__()
    item2.__str__()


if __name__ == "__main__":
    main()