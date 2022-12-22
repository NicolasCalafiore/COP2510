## Nicolas Calafiore
## U94446501
##
## Accepts 2 inputs (subtotal & tip amount %)
## Uses subtotal*tip/100 to find tip amount as cash
## Formats to 2 decimal places and rounds the subtotal, tip amount, and grand total
## prints

subtotal = float(input("Enter Subtotal: "))
tip = float(input("Enter Tip %: "));

newSubtotal = "%0.2f" % (round(subtotal,3),)  ## Credit: https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
tipAsCash = "%0.2f" % (round(subtotal*(tip/100),3),)
grandTotal = "%0.2f" % (round(float(newSubtotal) + float(tipAsCash),3),)

print("\n---Receipt---")
print("Subtotal: $", newSubtotal);
print("Tip: $", tipAsCash)
print("Total: $", grandTotal)
