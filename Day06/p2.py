# Similar to previous puzzle, but now after reaching a pattern already seen, we
# need to find how many cycles it takes to reach that same state again.

NUMBER_OF_BLOCKS = 16


def redistribute_highest_cell(blocks_list, redistribution_cycle_counter):
    redistribution_cycle_counter += 1
    highest_value = max(blocks_list)
    max_block_index = blocks_list.index(highest_value)
    blocks_list[max_block_index] = 0
    current_block_index = max_block_index + 1
    for n in range(highest_value):
        if current_block_index >= NUMBER_OF_BLOCKS:
            current_block_index = 0
        blocks_list[current_block_index] += 1
        current_block_index += 1
    return redistribution_cycle_counter


def calc_number_of_cycles():
    with open('input.txt') as f:
        blocks = list(map(int, f.read().split('\t')))

    list_of_patterns = []
    redistribution_cycle = 0
    while blocks not in list_of_patterns:
        list_of_patterns.append(blocks[:])
        redistribution_cycle = redistribute_highest_cell(blocks, redistribution_cycle)

    # State already seen before has been reached
    list_of_patterns =[]
    redistribution_cycle = 0
    pattern_to_look_for = blocks[:]
    while pattern_to_look_for not in list_of_patterns:
        redistribution_cycle = redistribute_highest_cell(blocks, redistribution_cycle)
        list_of_patterns.append(blocks[:])

    print(redistribution_cycle)


if __name__ == '__main__':
    calc_number_of_cycles()