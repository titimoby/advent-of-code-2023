def get_content(filename: str) -> (str, dict):
    with open(filename, "r") as file:
        data = file.read().split("\n\n")

    # map instruction as 0 for L and 1 for R
    instructions = [0 if i == 'L' else 1 for i in data[0]]

    maps_data = data[1].replace('(', '').replace(')', '').split('\n')
    # for my own education, I keep original code that created my dictionnary
    # network = {}
    # for line in maps_data:
    #     origin, move = line.split(' = ')
    #     network[origin] = move.split(', ')

    # and this is the version using dictionary comprehension
    network = {line.split(' = ')[0]: line.split(' = ')[1].split(', ') for line in maps_data}

    return instructions, network


def how_many_steps(instructions, network, starting_node) -> int:
    step_counter = 0
    node = starting_node
    while node[-1] != 'Z':
        which_instruction = step_counter % len(instructions)
        node = network[node][instructions[which_instruction]]
        step_counter += 1
    else:
        return step_counter


def day08part1(filename: str) -> int:
    instructions, network = get_content(filename)
    return how_many_steps(instructions, network, 'AAA')


if __name__ == "__main__":
    # test on the file parsing for test input
    parsing_test = get_content("input-files/day08part1.test")
    assert parsing_test == ([1, 0],
                            {'AAA': ['BBB', 'CCC'], 'BBB': ['DDD', 'EEE'], 'CCC': ['ZZZ', 'GGG'], 'DDD': ['DDD', 'DDD'],
                             'EEE': ['EEE', 'EEE'], 'GGG': ['GGG', 'GGG'], 'ZZZ': ['ZZZ', 'ZZZ']})

    test_result = day08part1("input-files/day08part1.test")
    print(test_result)
    assert test_result == 2

    test_result = day08part1("input-files/day08part1.test2")
    print(test_result)
    assert test_result == 6

    test_result = day08part1("input-files/day08part1.input")
    print(test_result)
    assert test_result == 18727