from tooling.file_access import get_content


def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


def part1(line: str):
    number = ""
    number += get_first_digit(line)
    number += get_first_digit(line[::-1])
    return int(number)


def day01part1(filename: str) -> int:
    content = get_content(filename)
    result = 0
    for line in content:
        result += part1(line)
    return result


if __name__ == "__main__":
    test_result = day01part1("input-files/day01part1.test")
    assert (test_result == 142)
    print(test_result)
    input_result = day01part1("input-files/day01part1.input")
    assert input_result == 54968
    print(input_result)
