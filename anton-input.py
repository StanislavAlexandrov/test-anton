
from random import randint
import time

x = input("what is your name? ")
y = input("what is the place? ")
z = input("what time is it? ")

print("Well, hello " + x)
time.sleep(1)
print("You are in " + y + ".")
time.sleep(1)
print("And it is " + z + ".")
time.sleep(1)


newThrow = input("Would you like to throw more? ")


def throwDice():
    result = randint(1, 6)
    print("Your result is... " + str(result) + ".")


while newThrow == "y":
    throwDice()
    newThrow = input("Would you like to throw more(y/n)?")
