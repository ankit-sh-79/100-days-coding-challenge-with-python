name = name_string .(" , ")

import random

# get the total number of items in list
num_items = len(name)
# generate random number between 0 and the last index
random_choice = random.randint(0, num_items - 1)
#pick the random person from the list of names using the random number
person_who_will_pay = name[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
