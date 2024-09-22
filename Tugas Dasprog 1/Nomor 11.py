# read variable  m
m = int(input("Masukkan nilai dari m: "))

# read variable n
n = int(input("Masukkan nilai dari n: "))

# calculate side 1
side_1 = m ** 2 - n ** 2

# calculate side 2
side_2 = 2 * m * n

# calculate hypotenuse
hypotenuse = (m ** 2) + (n ** 2)

# print output 
print("The values of the triple pythagorean triple are", side_1, side_2, hypotenuse)