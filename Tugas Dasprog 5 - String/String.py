# Create String
string0 = "Shabrina Sarayati"
string1 = "5054241009"
string2 = "JakTim"

# Print string
print("Nama saya adalah", string0)
print("NRP", string1)
print("Asal daerah " + string2)

# Access character in string
print("Inisial saya", string0[0] + string0[9])

# String slicing
print("Nama belakang saya" + string0[8:])
print("Nama panggilan saya" + string0[:4])

# Reverse String
print("Reverse dari NRP saya adalah " + string1[::-1])

# Update string
string3 = "Saya mahasiswa RKA"
# ubah menjadi "Saya bukan mahasiswa RPL"
# Cara 1 (Fasel)
string4 = string3.replace("mahasiswa RKA", "bukan mahasiswa RPL")
print(string4)

# Cara 2 (Raditya Akmal)
list3 = list(string3)
list3[4] = " bukan "
string4 = ''.join(list3)
string5 = string4[0:21] + "RPL"
print(string5)

# ----------
# Tugas implementasi
# 1 deleting a character dari kota asal
String1 = "Jakarta"
print("Initial String: ")
print(String1)

String2 = String1[0:3] + String1[4:]
print("\nDeleting character at 3nd Index: ")
print(String2)

# 2 Escape sequencing in python
string1 = """It's a "Sunny" day!"""
print("Initial String with use of Triple Quotes: ")
print(string1)

# Escaping Single Quote
String2 = 'You\'re a "Champion"'
print("\nEscaping Single Quote: ")
print(String2)

# Printing Paths with the
# use of Escape Sequences
String1 = "C:\\Users\\Shabrina\\Documents\\Semester 1\\Tugas Sem 1\\Dasar Pemrograman"
print("\nEscaping Backslashes: ")
print(String1)

# Printing Paths with the
# use of Tab
String1 = "Shabrina\tSarayati"
print("\nTab: ")
print(String1)

# Printing Paths with the
# use of New Line
String1 = "Belajar\nPython\nItu\nSeru\nBanget\nLoh"
print("\nNew Line: ")
print(String1)

# 3 python string formating 
# Python Program for
# Formatting of Strings

# Default order
String1 = "{} {} {}".format('Jaehyun', 'Ganteng', 'Banget')
print("Print String in default order: ")
print(String1)

# Positional Formatting
String1 = "{1} {0} {2}".format('Jaehyun', 'Ganteng', 'Banget')
print("\nPrint String in Positional order: ")
print(String1)

# Keyword Formatting
String1 = "{b} {g} {j}".format(j='Jaehyun', g='Ganteng', b='Banget')
print("\nPrint String in order of Keywords: ")
print(String1)

# Formatting of Integers
String1 = "{0:b}".format(2005)
print("\nBinary representation of 36 is ")
print(String1)

# Formatting of Floats
String1 = "{0:e}".format(306.2005)
print("\nExponent representation of 306.2005 is ")
print(String1)

# Rounding off Integers
String1 = "{0:.2f}".format(2005/1997)
print("\none-sixth is : ")
print(String1)

# String alignment
String1 = "|{:<3}|{:^6}|{:>9}|".format('Aku',
                                          'Suka', 
                                          'Pink')
print("\nLeft, center and right alignment with Formatting: ")
print(String1)

# To demonstrate aligning of spaces
String1 = "\n{0:^15} pink sejak {1:<10}!".format("Aku suka warna",
                                                    2010)
print(String1)

# Python Program for
# Old Style Formatting
# of Integers
Integer1 = 12.9876543
print("Formatting in 3.2f format: ")
print('The value of Integer1 is %3.2f' % Integer1)
print("\nFormatting in 3.4f format: ")
print('The value of Integer1 is %3.4f' % Integer1)