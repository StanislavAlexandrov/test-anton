import random
min = 1
max = 6

roll_again = "yes"


while roll_again == "yes" or roll_again == "y":
    result = random.randint(min, max)
    print("The result is..." + str(result))
    roll_again = input("Roll the dice again?")
