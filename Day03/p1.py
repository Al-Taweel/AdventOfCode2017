# Spiral memory:
# In a grid that starts in the middle with number 1 then spirals out  with
# every increment, find the "manhattan distance" to number '1' from a given
#  number in the grid. For example, in the following grid:
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# The distance from 23 to 1 is 2 (move up twice)
# The distance from 17 to 1 is 4 (move right twice then down twice)

import math

# The number to find the distance from
x = 265149


# Start by finding which square x is in.
sq_root_x = math.sqrt(x)
int_sq_root_x = int(sq_root_x)
# Squares sizes are 1x1, 3x3, 5x5, 7x7, etc.
# If sqrt of x is even, then adding one to it gives us the correct square.
# if sqrt of x is odd and not int then we need to add 2 to get the correct square.
# else sqrt of x is odd int. This is the actual square size.
if int_sq_root_x % 2 == 0:
    square = int_sq_root_x + 1
elif sq_root_x > int_sq_root_x:
    square = int_sq_root_x + 2
else:
    square = int_sq_root_x

# The square starts with ((square-2)^2)+1
square_begins = ((square-2)**2)+1
# The square ends with (square^2)
square_ends = square**2

# find the side x belongs to
if x < (square_begins-1+square-1):  # Right hand side.
    midpoint = square_begins - 1 + int(square/2)
    horizontal_distance = int(square/2)
    vertical_distance = abs(x-midpoint)
elif x < (square_begins-1+(2*(square-1))):    # Top side.
    midpoint = square_begins -1 + (square - 1) + int(square / 2)
    vertical_distance = int(square/2)
    horizontal_distance = abs(x-midpoint)
elif x < (square_begins-1+(3*(square-1))):    # Left side.
    midpoint = square_begins - 1 + (2*(square-1)) + int(square / 2)
    horizontal_distance = int(square/2)
    vertical_distance = abs(x-midpoint)
else:   # Bottom side
    midpoint = square_begins - 1 + (3*(square-1)) + int(square / 2)
    vertical_distance = int(square / 2)
    horizontal_distance = abs(x - midpoint)

distance = vertical_distance + horizontal_distance

print(distance)
