import collections

from tooling.file_access import get_content

avoid = "0123456789."


def day03part2(filename: str) -> int:
    schematic = get_content(filename)
    gear_ratio_sum = 0
    gears = collections.defaultdict(list)
    for line_index, line in enumerate(schematic):
        part_number = 0
        # believe it or not, I'm going to use this either as a boolean or a value
        # this is dedicated to my mate wilda
        gear = False
        for column_index, char in enumerate(line):
            # looking to get numbers
            if char.isdigit():
                part_number = part_number * 10 + int(char)
                for line_adjacent in [-1, 0, 1]:
                    for column_adjacent in [-1, 0, 1]:
                        try:
                            adjacent_char = schematic[line_index + line_adjacent][column_index + column_adjacent]
                            if adjacent_char == '*':
                                gear = (line_index + line_adjacent, column_index + column_adjacent)
                        except IndexError:
                            # I know, sounds ugly, but it is a way to simply test adjacent cells anyway
                            continue
            if not char.isdigit() or column_index == len(line) - 1:
                if gear:
                    gears[gear].append(part_number)
                    if len(gears[gear]) == 2:
                        gear_ratio_sum += part_number * gears[gear][0]
                    gear = False
                part_number = 0
    return gear_ratio_sum


if __name__ == "__main__":
    test_result = day03part2("input-files/day03part1.test")
    assert test_result == 467835
    print(test_result)
    test_result = day03part2("input-files/day03part2.input")
    # assert test_result == 540131
    print(test_result)
