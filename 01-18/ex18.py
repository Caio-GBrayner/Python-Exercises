import math

angle = float(input("Enter the angle: "))
sine = math.sin(math.radians(angle))
print(f"The angle {angle:.2f} has the SINE of {sine:.2f}")
cosine = math.cos(math.radians(angle))
print(f"The angle {angle:.2f} has cosine of {cosine:.2f}")
tangent = math.tan(math.radians(angle))
print(f"The angle {angle:.2f} has the tangent of {tangent:.2f}")