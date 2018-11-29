# An array of 16  blocks containing numbers needs to be redistributed. The
# block with the highest number in set to 0 and the number in it is
# redistributed to the other blocks (by adding 1 at a time to the other
# blocks), starting with the next block onwards and going round to the first
# block in a round robin way.
# The process continues until the numbers in all the blocks matches a pattern
# seen earlier (indicating an endless loop has been reached).
NUMBER_OF_BLOCKS = 16
with open('input.txt') as f:
    blocks = list(map(int, f.read().split('\t')))

list_of_patterns =[]
redistribution_cycle_counter = 0

while blocks not in list_of_patterns:
    redistribution_cycle_counter += 1
    list_of_patterns.append(blocks[:])
    highest_value = max(blocks)
    max_block_index = blocks.index(highest_value)
    blocks[max_block_index] = 0
    current_block_index = max_block_index + 1
    for n in range(highest_value):
        if current_block_index >= NUMBER_OF_BLOCKS:
            current_block_index = 0
        blocks[current_block_index] += 1
        current_block_index += 1


print(redistribution_cycle_counter)

