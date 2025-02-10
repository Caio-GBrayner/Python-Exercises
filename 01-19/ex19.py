import random
name1 = str(input("Enter the  1st "))
name3 = str(input("Enter the  3st "))
name2 = str(input("Enter the  2st "))
name4 = str(input("Enter the  4st "))

listName = [name1, name2, name3, name4]

chosenOne = random.choice(listName)

print(f"The chosen one is {chosenOne}")
