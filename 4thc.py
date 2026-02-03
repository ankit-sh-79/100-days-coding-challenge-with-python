states_of_matter = ["delaware", "texas", "california", "new york"]

print(states_of_matter[0])

states_of_matter[1] = "florida"

# states_of_matter.append("pennsylvania")
states_of_matter.extend(["pennsylvania", "arizona", "alaska"])
states_of_matter.remove("california")                           
print(states_of_matter)
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
print("hiding your treasure X marks the spot.")
position = input() # where do you want to put the treasure?
#your code below
letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"

