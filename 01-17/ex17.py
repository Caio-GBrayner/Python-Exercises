import math

a = float(input("Enter the opposite side"))
b = float(input("Enter the adjacent side"))
c = math.sqrt((pow(a,2) + pow(b,2)))
d = (pow(a,2) + pow(b,2))**0.5

print(f"The hypotenuse: {c:.2f}")
print(f"The hypotenuse: {d:.2f}")

