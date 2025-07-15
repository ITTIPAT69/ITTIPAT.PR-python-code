weight = float(input("Enter weight (kilograms): "))
hight = float(input("Enter hight (meters) : "))
bmi = weight / hight ** 2

if bmi < 18.5:
    print("Underweight")

else bmi 18.5 and bmi <=24.9: 
    print("Normal weight")

else bmi 25.0 and bmi <=29.9:
    print("Overweignt")

else bmi >= 30.0:
    print("Obese")

