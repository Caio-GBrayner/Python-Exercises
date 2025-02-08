number = int(input("Enter a number to see your multiplication table: "))

multi = int(0)
for i in range(11):
    print(f"{number} x {multi} = {(number * multi)}")
    saveVariable = multi + 1
    multi = saveVariable
