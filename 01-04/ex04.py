import string

a = input("Enter something: ")

print("O primitive type of this value is: ", type(a))
print("This primitive only has spaces? ", a.isspace())
print("Is it a number? ", a.isnumeric())
print("Is it alphabetic? ", a.isalpha())
print("Is it alphanumeric? ", a.isalnum())
print("Is it in uppercase? ", a.isupper())
print("Is it in lower? ", a.islower())
print("Is it capitalized? ", a.istitle())