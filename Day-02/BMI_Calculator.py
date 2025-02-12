height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kgs: "))

BMI = weight/(height ** 2) * 10000

print("Your BMI value is:", BMI)

# If we want to print round value of float and two digits after float point
print(round(BMI,2))

# example output 34.56