from tooling.file_access import get_content


def is_this_set_possible(game_set: str) -> bool:
    cubes_in_bag = {'red': 12, 'green': 13, 'blue': 14}
    set_is_possible = True
    for cubes in game_set.split(','):
        number, color = cubes.strip().split(' ')
        if int(number) > cubes_in_bag[color]:
            set_is_possible = False
            break
    return set_is_possible


def day02part1(filename: str) -> int:
    content = get_content(filename)
    id_sum = 0
    for line in content:
        game_data, game_sets = line.split(':')
        game_index = int(game_data.replace("Game ", ""))
        game_is_possible = True
        for game_set in game_sets.split(';'):
            game_is_possible = game_is_possible and is_this_set_possible(game_set)
        if game_is_possible:
            id_sum += game_index
    return id_sum


if __name__ == "__main__":
    test_result = day02part1("input-files/day02part1.test")
    assert (test_result == 8)
    print(test_result)
    input_result = day02part1("input-files/day02part1.input")
    assert input_result == 2285
    print(input_result)
