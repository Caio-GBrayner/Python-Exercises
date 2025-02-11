city = str(input("Enter the name of the city where you were born in: "))
cityWithoutSpaces = city.replace(" ", "").upper()

if "SANTO" == cityWithoutSpaces[3]:
    test = False
    print(test)
else:
    test = True
    print(test)

