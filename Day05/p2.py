# A Maze of Twisty Trampolines, All Alike
# The input is a list of numbers. Each number represents a jump to the next
# location. After a jump, the number causing the jump increases by 1 if it was
# less than 3 and decreases by 1 otherwise.
# Find the number of jumps needed to exit from the list.

with open('input.txt') as f:
    list_of_numbers = f.readlines()

current_location = 0
number_of_jumps = 0
while current_location < len(list_of_numbers):
    jump = int(list_of_numbers[current_location])
    next_location = current_location + jump
    if jump < 3:
        list_of_numbers[current_location] = jump + 1
    else:
        list_of_numbers[current_location] = jump - 1
    current_location = next_location
    number_of_jumps += 1

print(number_of_jumps)
