weight = float(input("Enter weight (kilograms): "))
hight = float(input("Enter hight (meters) : "))
bmi = weight / hight ** 2

if bmi < 18.5:
    print("Underweight")

if bmi >= 18.5 and bmi <=24.9: 
    print("Normal weight")

if bmi >= 25.0 and bmi <=29.9:
    print("Overweignt")

if bmi >= 30.0:
    print("Obese")

