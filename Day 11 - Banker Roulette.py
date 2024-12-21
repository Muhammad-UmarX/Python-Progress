names = input("Enter the names: ")
name_list = names.split(", ")

import random

list_size = len(name_list)
random_name = random.randint(1, list_size - 1)
person_paying = name_list[random_name]
print("The person to get their wallet empty is.....", person_paying)
