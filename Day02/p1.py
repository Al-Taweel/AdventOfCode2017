# Given the input file input.txt containing a list of digits in rows, find
# the difference between the largest and the smallest numbers in each row and
# add that to a checksum.


checksum = 0
with open('input.txt') as f:
	rows = f.readlines()

for row in rows:
	largest_number = None
	smallest_number = None
	for n in row.split('\t'):
		number = int(n)
		if largest_number is None:
			largest_number = int(number)
			smallest_number = int(number)
		if number > largest_number:
			largest_number = number
		if number < smallest_number:
			smallest_number = number
	checksum += largest_number - smallest_number

print(checksum)
