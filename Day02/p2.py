# Similar to the first problem but instead of finding the largest and the
# smallest in each row, we need to find the two numbers evenly divisible
# by each others. The sum of the divisions makes the checksum for this task.


checksum = 0
with open('input.txt') as f:
	rows = f.readlines()

for row in rows:
	row_division_result = None
	for n1 in row.split('\t'):
		number1 = int(n1)
		for n2 in row.split('\t'):
			number2 = int(n2)
			if (number1 != number2) and ((number1 % number2) == 0):
				row_division_result = number1 / number2
				break
		if row_division_result is not None:
			checksum += row_division_result
			break

print(int(checksum))
