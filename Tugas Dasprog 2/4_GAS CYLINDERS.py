# Input cylinder’s color
Gas_Color = input("Enter the first letter of the cylinders color: ")

# Category of gas cylinders
if Gas_Color == "O" or Gas_Color == "o":
    category = "ammonia"

elif Gas_Color == "B" or Gas_Color == "b": 
    category = "carbon monoxide"

elif Gas_Color == "Y" or Gas_Color == "y": 
    category = "hydrogen"

elif Gas_Color == "G" or Gas_Color == "g":
    category = "oxygen"

else:
    category = "contents unknown"

# print output
print("the contents of the gas cylinder are: ", category)