print("S | M | L")
pizza_size = input("Please choose your pizza size: ")
total_bill = 0

if pizza_size == "S":
    add_pepperoni = input("Do you want to add pepperoni?")
    total_bill += 15
    if add_pepperoni == "Y":
        total_bill += 2
    add_cheese = input("Do you want to add extra cheese?")
    if add_cheese == "Y":
        total_bill += 1
    print("That will be", total_bill, "$")

elif pizza_size == "M":
    total_bill += 20
    add_pepperoni = input("Do you want to add pepperoni?")
    if add_pepperoni == "Y":
        total_bill += 3
    add_cheese = input("Do you want to add extra cheese?")
    if add_cheese == "Y":
        total_bill += 1
    print("That will be", total_bill, "$")

elif pizza_size == "L":
    total_bill += 25
    add_pepperoni = input("Do you want to add pepperoni?")
    if add_pepperoni == "Y":
        total_bill += 2
    add_cheese = input("Do you want to add extra cheese?")
    if add_cheese == "Y":
        total_bill += 1
    print("That will be", total_bill, "$")