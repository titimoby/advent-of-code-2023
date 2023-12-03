from tooling.file_access import get_content

avoid = "0123456789."


def day03part1(filename: str) -> int:
    schematic = get_content(filename)
    parts_sum = 0
    for line_index, line in enumerate(schematic):
        part_number = 0
        is_it_part = False
        for column_index, char in enumerate(line):
            # looking to get numbers
            if char.isdigit():
                part_number = part_number * 10 + int(char)
                for line_adjacent in [-1, 0, 1]:
                    for column_adjacent in [-1, 0, 1]:
                        try:
                            adjacent_char = schematic[line_index + line_adjacent][column_index + column_adjacent]
                            if adjacent_char not in avoid:
                                is_it_part = True
                        except IndexError:
                            # I know, sounds ugly, but it is a way to simply test adjacent cells anyway
                            continue
            if not char.isdigit() or column_index == len(line) - 1:
                if is_it_part:
                    parts_sum += part_number
                    is_it_part = False
                part_number = 0
    return parts_sum


if __name__ == "__main__":
    test_result = day03part1("input-files/day03part1.test")
    assert test_result == 4361
    print(test_result)
    test_result = day03part1("input-files/day03part1.input")
    assert test_result == 540131
    print(test_result)
