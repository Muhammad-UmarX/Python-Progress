weight = float(input("Enter your weight(in kgs): "))
height_cm = float(input("Enter your height(in meters): "))

height_m = height_cm/100
bmi = weight/(height_m**2)

print("Your Body Mass Index (BMI) is", bmi)

if bmi > 40:
    print("You are obese")

elif bmi > 35:
    print("You are slightly obese")

elif bmi > 30:
    print("You are overweight")

elif bmi > 25:
    print("You are slightly overweight")

elif bmi > 22:
    print("You are healthier")

elif bmi > 18:
    print("You are healthy")

elif bmi <= 18:
    print("You are slightly underweight")

elif bmi <= 17:
    print("You are underweight")







