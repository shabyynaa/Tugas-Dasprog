# Input x and y coordinates
coordinate_x = float(input("Enter the coordinates of point x: "))
coordinate_y = float(input("Enter the coordinates of point y: "))

# determine the location of the point
if coordinate_x == 0 and coordinate_y == 0:
    print("is at the origin")

elif coordinate_x == 0:
    print("is on the y axis")

elif coordinate_y == 0:
    print("is on the x axis")

elif coordinate_x > 0 and coordinate_y > 0:
    print("is in quadrant I")

elif coordinate_x < 0 and coordinate_y > 0:
    print("is in quadrant II")

elif coordinate_x < 0 and coordinate_y < 0:
    print("is in quadrant III")

elif coordinate_x > 0 and coordinate_y < 0:
    print("is in quadrant IV")