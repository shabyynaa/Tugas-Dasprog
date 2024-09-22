# Input day, month, and year
day = int(input("Enter the day (1-31): "))
month = int(input("Enter the month (1-12): "))
year = int(input("Enter the year: "))

# tahun kabisat
if (year % 400 == 0): 
    leap_year = True

else:
    leap_year = False

# Jumlah hari dalam setiap bulan untuk tahun yang bukan kabisat
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# tahun kabisat
if leap_year:
    days_in_month[1] = 29 

# Calculate the day number
day_number = sum(days_in_month[0:month - 1]) + day

# print output
print(day, "/", month, "/", year, "is day number", day_number, "of the year")
