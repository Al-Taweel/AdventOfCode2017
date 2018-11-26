# Similar to first problem but instead of adding digits if they match the next
# digit, we now add a digit to sum only if it matches the digit (list length /2)
# away from it. The list is still circular


digits = ''
with open('input.txt') as f:
    digits = f.read()

total = 0
step =int(len(digits)/2)

for i in range(len(digits)-1):
    if i + step > len(digits)-1:
        if digits[i] == digits[(i+step)-len(digits)]:
            total += int(digits[i])
    else:
        if digits[i]==digits[i+step]:
            total += int(digits[i])

if digits[-1] == digits[step-1]:
    total += int(digits[-1])

print(total)
