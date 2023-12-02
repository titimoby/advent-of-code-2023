from tooling.file_access import get_content


def max_colors_of_set(game_set: str, max_colors: dict[str, int]) -> dict[str, int]:
    for cubes in game_set.split(','):
        number, color = cubes.strip().split(' ')
        if int(number) > max_colors[color]:
            max_colors[color] = int(number)
    return max_colors


def day02part2(filename: str) -> int:
    content = get_content(filename)
    power = 0
    for line in content:
        game_data, game_sets = line.split(':')
        max_colors = {'red': 0, 'blue': 0, 'green': 0}
        for game_set in game_sets.split(';'):
            max_colors = max_colors_of_set(game_set, max_colors)
        power_of_line = max_colors['red'] * max_colors['blue'] * max_colors['green']
        power += power_of_line
    return power


if __name__ == "__main__":
    test_result = day02part2("input-files/day02part1.test")
    assert (test_result == 2286)
    print(test_result)
    input_result = day02part2("input-files/day02part2.input")
#    assert input_result == 2285
    print(input_result)
