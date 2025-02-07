import math

number = float(input("Enter a number: "))

squareRoot = math.sqrt(number)
triple = number * 3
double = number * 2
toRaise = pow(number, 2)
Root = number ** (1/3)



print("The double of {} is {} ".format(number, double))
print("The triple of {} is {} ".format(number, triple))
print("The {} raise to 2 is {} ".format(number, toRaise))
print("The square root of {} is {:.2f} ".format(number, squareRoot))
print("The root of {} raise of 3 is {:.2f} ".format(number, Root))
print("The root of " + f"{number}" " raise of 3 is " + f"{Root:.2f}")
