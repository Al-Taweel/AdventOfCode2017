import re


def find_parent(end_node, groups_dict):
    for parent, offspring in groups_dict.items():
        if end_node in offspring:
            return find_parent(parent, groups_dict)
    return end_node


def find_root():
    with open('input.txt') as f:
        programs_list = f.read().splitlines()

    # Build a dictionary with all parent nodes.
    groups_dict = {}
    for program in programs_list:
        stack = re.search('(\w+)(.*)->(.*)', program)
        if stack:
            key = stack.group(1).strip()
            value_list = [v.strip(' ,') for v in stack.group(3).split()]
            groups_dict[key] = value_list

    # find the first end node.
    end_node = ''
    for program in programs_list:
        match = re.search('(\w+) \(\d+\)$', program)
        if match:
            end_node = match.group(1)
            break
    # now find its parents recursively until no parent is found.
    root = find_parent(end_node, groups_dict)
    print(root)


if __name__ == '__main__':
    find_root()