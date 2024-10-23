# Ask the user for the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check if it's a valid triangle first
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    # Determine the type of triangle
    if side1 == side2 == side3:
        print("The triangle is Equilateral (all sides are equal).")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles (two sides are equal).")
    else:
        print("The triangle is Scalene (all sides are different).")
else:
    print("The lengths provided cannot form a valid triangle.")
