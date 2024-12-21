print("----------This is the tip calculator----------")

bill = float(input("Enter total bill: "))
print("10% | 15% | 20%")
tip = float(input("How much tip would you like to give: "))
people = int(input("How many people will the bill be divided into: "))
div_bill = (bill + (tip/bill)*100)/people
div_bill = round(div_bill, 2)

print(f"Each person will pay {div_bill}$")