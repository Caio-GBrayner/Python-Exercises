name = str(input("Enter your name: "))
nameWithoutSpaces = name.replace(" ", "").upper()

if "SILVA" not in nameWithoutSpaces:
    test = False
    print(test)
else:
    test = True
    print(test)