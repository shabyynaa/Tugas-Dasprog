# read time
hour, minute = input("Enter hours and minute: ").split()
hour = int(hour)
minute = int(minute)
time = round(hour + minute/60, 1)
# gak usah ada round nya

print(time)

# calculate temperature
temperature = (4 * time**2)/(time + 2) - 20

# print output
print("Temperature", temperature)