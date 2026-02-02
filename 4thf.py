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

# don't change the code above 👆
#Write your code below this row 👇

#write your code above this row 👆
#don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")