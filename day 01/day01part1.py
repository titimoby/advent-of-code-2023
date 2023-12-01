def get_first_digit(line: str) -> str:
    for char in line:
        if char.isdigit():
            return char


def day01(filename: str) -> str:
    result = 0
    with open(filename, "r") as file:
        content = file.readlines()
        for line in content:
            number = ""
            number += get_first_digit(line)
            number += get_first_digit(line[::-1])
            result += int(number)
    return result


if __name__ == "__main__":
    print(day01("day 01/day01part1.test"))
    print(day01("day 01/day01part1.input"))
