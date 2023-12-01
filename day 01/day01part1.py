def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


def part1(line: str):
    number = ""
    number += get_first_digit(line)
    number += get_first_digit(line[::-1])
    return int(number)


def day01(filename: str) -> str:
    with open(filename, "r") as file:
        content = file.readlines()
        result = 0
        for line in content:
            result += part1(line)
    return result


if __name__ == "__main__":
    test_result = day01("day 01/day01part1.test")
    assert (test_result == 142)
    print(test_result)
    input_result = day01("day 01/day01part1.input")
    assert input_result == 54968
    print(input_result)
