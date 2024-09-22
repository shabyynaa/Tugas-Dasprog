# read Gallon
Galon_Per_Barrel = 42 

# BTU per Barrel
BTU_Per_Barrel = 5800000 

# calculate BTU per gallon of oil
BTU = BTU_Per_Barrel / Galon_Per_Barrel 

# read jumlah
gallons = int(input("gallons of oil: "))

# read efisiensi
efisiensi = float(input("Masukkan efisiensi: "))

# calculate
BTU_total = gallons / 42 * 58000000 * efisiensi / 100

# print output
print("BTU_total", BTU_total)

