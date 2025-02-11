name = str(input("Enter your name: "))

print(f"ToUppercase: {name.upper()}")
print(f"ToLowercase: {name.lower()}")
print(f"Your name have: {len(name)-name.count(' ')} letters")
firstName = name.split()
print(f"Your first name is {firstName} and has {len(firstName[0])} letters")