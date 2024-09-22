# read odometer
beginning_odometer = float(input('Enter beginning odometer: '))
ending_odometer = float(input('Enter ending odometer: '))

# calculate distance
distance = round(ending_odometer - beginning_odometer, 1)

# calculate fare
fare = round(distance * 1.50, 2)

#  print output
print("You traveled a distance of", distance, "miles. At $1.50 per mile, your fare is $", fare)