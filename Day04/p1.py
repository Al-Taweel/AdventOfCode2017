# High-Entropy Passphrases:
# Check a phrase of words for repeated words.
# a phrase with no repeat is valid, otherwise invalid.
# For example:
# "aa bb cc" is valid
# "aa bb aa" is invalid
# "aaa aa" is valid.
# Count the number of valid phrases in an input file.


def valid(p):
    word_list = p.split(' ')
    while word_list:
        word = word_list.pop()
        if word in word_list:
            return False
    return True


valid_count = 0
with open('input.txt') as f:
    phrases = f.readlines()
for phrase in phrases:
    if valid(phrase.rstrip()):
        valid_count += 1

print(valid_count)