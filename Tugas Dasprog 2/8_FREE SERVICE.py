# input menu
print("(1) First Free Service")
print("(2) Second Free Service")

# input service number
service_number = int(input("Enter the Free Service number: "))

# input miles
miles = float(input("Enter number of Miles: "))

# Determine the appropriate message
if service_number == 1:
    if miles > 1500 and miles <= 3000:
        print("Vehicle must be serviced")
    else:
        print("Vehicle does not require servicing yet")

elif service_number == 2:
    if miles > 3001 and miles <= 4500:
        print("Vehicle must be service")
    else:
        print("Vehicle does not require servicing yet")
else:
    print("Invalid service number")

