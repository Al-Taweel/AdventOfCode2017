# Given the input file input.txt containing a list of digits. Ge tthe Summary
# of all digits that match the next digit in the list. For example, the list '112'
# gives the sum of 1 because:
# - 1st digits matches the 2nd digit ==> sum = 1
# - 2nd digit doesn't match 3rd digit ==> sum = 1
# - 3rd digit doesn't match 1st digit ==> sum = 1


digits = ''
with open('input.txt') as f:
    digits = f.read()

total = 0
for i in range(len(digits)-1):
    if digits[i] == digits[i+1]:
        total += int(digits[i])
if digits[-1] == digits[0]:
    total += int(digits[0])
print(total)
