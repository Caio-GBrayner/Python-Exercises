width = float(input("Enter width value: "))
height = float(input("Enter height value: "))



print(f"Its wall is the size of {width} x {height} and its area is {(width * height)}m².")

paint = (width * height)/ 2

print(f"To paint this wall, you will need {paint:.3f}l paint")