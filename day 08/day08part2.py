import time


def get_content(filename: str) -> (str, dict):
    with open(filename, "r") as file:
        data = file.read().split("\n\n")
    instructions = [0 if i == 'L' else 1 for i in data[0]]
    maps_data = data[1].replace('(', '').replace(')', '').split('\n')
    network = {line.split(' = ')[0]: line.split(' = ')[1].split(', ') for line in maps_data}
    return instructions, network


def all_nodes_to_Z(nodes) -> bool:
    finished = [value for value in nodes if value[-1] == 'Z']
    return len(finished) == len(nodes)


def how_many_steps(instructions, network, starting_nodes) -> int:
    step_counter = 0
    nodes = starting_nodes
    while not all_nodes_to_Z(nodes):
        which_instruction = step_counter % len(instructions)
        nodes = [network[node][instructions[which_instruction]] for node in nodes]
        step_counter += 1
    else:
        return step_counter


def day08part1(filename: str) -> int:
    instructions, network = get_content(filename)
    starting_nodes = [key for key in network.keys() if key[-1] == 'A']
    max_steps = how_many_steps(instructions, network, starting_nodes)
    return max_steps


if __name__ == "__main__":
    # test on the file parsing for test input
    parsing_test = get_content("input-files/day08part1.test")
    assert parsing_test == ([1, 0],
                            {'AAA': ['BBB', 'CCC'], 'BBB': ['DDD', 'EEE'], 'CCC': ['ZZZ', 'GGG'], 'DDD': ['DDD', 'DDD'],
                             'EEE': ['EEE', 'EEE'], 'GGG': ['GGG', 'GGG'], 'ZZZ': ['ZZZ', 'ZZZ']})

    test_result = day08part1("input-files/day08part2.test")
    print(test_result)
    assert test_result == 6

    time_start = time.perf_counter()
    test_result = day08part1("input-files/day08part2.input")
    print(test_result)
    # assert test_result == 18727
    print(f'Solved in {time.perf_counter() - time_start:.5f} Sec.')
