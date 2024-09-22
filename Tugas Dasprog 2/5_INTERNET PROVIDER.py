# Input data usage in GBs
data_usage = int(input("Enter the data usage in GBs: "))

# category charges
if data_usage > 0 and data_usage <= 1:
    charge = 250

elif data_usage > 1 and data_usage <= 2:
    charge = 500

elif data_usage > 2 and data_usage <= 5:
    charge = 1000

elif data_usage > 5 and data_usage <= 10:
    charge = 1500

elif data_usage > 10:
    charge = 2000

else:
    print("Bad data: Invalid input")

# print output
print("charge: ", charge)
