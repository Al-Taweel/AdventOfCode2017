# No anagrams Passphrases:
# Check a phrase of words for anagram words.
# a phrase with no anagrams is valid, otherwise invalid.
# anagrams are words that can be rearranged to form each other
# For example:
# "aa bb cc" is valid
# "ab ba " is invalid
# "adf dfa asg" is invalid.
# Count the number of valid phrases in an input file.


def valid(p):
    # sort letters in words for easier comparison.
    word_list = list(map(sorted, p.split(' ')))
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
