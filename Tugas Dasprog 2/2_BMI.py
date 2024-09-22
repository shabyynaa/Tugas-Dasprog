# Input height and weight
Height = float(input("Enter your height (inches): ",))
Weight = float(input("Enter your weight (pounds): ",))

# Calculate BMI
BMI = round(703 * Weight / Height ** 2, 2)

# Category BMI
if BMI < 18.5:
    status = "Underweight"

elif 18.5 >= BMI >= 24.9:
    status = "Normal"

elif 24.9 >= BMI >= 29.9:
    status = "Overweight"

else:
    status = "Obsese" 

# print output 
print("Your BMI is: ", BMI)
print("Your weight status is: ", status)