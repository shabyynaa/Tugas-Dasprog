# read  volume
volume = int(input("volume to be infused => "))

# read Minutes
Minutes = int(input("Minutes over which to infuse => "))
hour = Minutes / 60

# calculate rate
debit = volume / hour

# print output
print("VTBI", volume, "ml")
print("rate", debit, "ml/hr")