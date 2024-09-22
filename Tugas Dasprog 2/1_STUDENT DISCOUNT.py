# Jumlah total pembeliaan
Total_Purchase = float(input("Masukkan total pembelian: $"))

# Student or No
Student = input("Apakah pembeli merupakan mahasiswa (yes/no): ")

# Discount and Tax
Students_Discount = 0.20
Sales_Tax = 0.05

# calculate
    # calculate for student
if Student == "yes":
    discount = round(Students_Discount * Total_Purchase, 2)
    Total_Discount = Total_Purchase - discount
    Tax = Sales_Tax * Total_Discount
    Final_Price = round(Total_Discount + Tax, 2)

    # print output for student
    print("Total Purchase: ", Total_Purchase)
    print("Student's Discount:", discount)
    print("Discount Total: ", Total_Discount)
    print("Sales Tax: ", Tax)
    print("Total: ", Final_Price)

else:
    # calculate for non student
    Tax = round(Sales_Tax * Total_Purchase, 2)
    Final_Price = round(Total_Purchase + Tax, 2)

    # print output for non student
    print("Total Purchase: ", Total_Purchase)
    print("Sales Tax (5%): ", Tax)
    print("Total: ", Final_Price)

