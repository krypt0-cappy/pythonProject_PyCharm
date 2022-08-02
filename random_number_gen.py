import random
import string

from random import seed
from random import randint

for _ in range(1):
    my_number = randint(0,10)

user_number = int(input("Please pick a number between 1 and 10: "))
matches = my_number == user_number
if matches == True:
    print(f"You have chosen the correct number: {matches}.")
else:
    print("You have NOT chosen the correct number!")
    print(f"The correct number was {my_number}")


