import random
import string

# Create a list of approved departments for the random name generator
EC2_Department_Approved_List = ["Accounting", "Marketing", "FinOps"]
for i in range(len(EC2_Department_Approved_List)):
    EC2_Department_Approved_List[i] = EC2_Department_Approved_List[i].upper() #Convert the departments in the list to uppercase

# Create a list of Marvel related words/heroes/movies/etc to be used in the name generator
random_Marvel_list = ["Dr. Strange-", "Time Stone-" "Thor-", "Iron Patriot-", "Hawkeye-", "Black Widow-", "The Eternals-", "Nick Fury-", "I AM GROOT-", "Nebula-", "Iron Man-", "StarLord-", "Rocket-", "Captain America-", "Winter Soldier-", "Falcon-", "AntMan-", "SpiderMan-", "Thanos-", "Infinity Stones-", "Nidavellir-", "NoWhere-", "Vision-", "Hulk-", "She-Hulk-", "Captain Marvel-"]
print("Hello, welcome to the EC2 Name Generator\n")
name = input("Please tell me your name: ")
name = (name.upper())

# Get the number of EC2 Instances that need names
ec2_count = int(input("How many EC2 Instances do you want to create names for? "))
while ec2_count == 0: # If user keeps selecting 0 as the instance number, it prompts them to choosing any number higher than 0 until they do so
    print("Please choose a number higher than 0. ")
    ec2_count = (int(input("How many EC2 Instances do you want to create names for? \n")))
else:
    print(f"Great! Let's create names for your {ec2_count} instances\n")
    print("Because the Marvel Universe Rules, your EC2 names are going to be random names from the MCU. Enjoy!\n")

# Allows for 5 incorrect attempts of choosing the correct department
counter = 5

# Create a function to randomly generate characters and numbers at the end of our Marvel name list
def ec2_avengers_name():
    for choice in range(ec2_count):
        choice = random.choice(random_Marvel_list)
        d = random.choices(string.digits, k=4)
        l = random.choices(string.ascii_letters, k=5)
        together = d + l
        nums_chars_joined = ''.join(random.sample(together, len(together)))
        print(choice + nums_chars_joined)

department = input(f"What department do you work in, {name}?\n ").upper()

while department not in EC2_Department_Approved_List and counter >= 1:
    print(f"Since you don't work in Accounting, Marketing, or FinOps, you are not approved to do this\n")
    department = input(f"Let's try again shall we? What department do you work in, {name}?\n ").upper()
    counter -= 1
else:
    print(f"You work in the {department} department, which is approved to use the name generator!")
    print(f"Congratulations! You have successfully named {ec2_count} instances!\n")
    print("Those instance names are: ")
    ec2_avengers_name()

print("\nThanks for contributing to my love of the MCU. One day the DC Universe might catch up!")


