def translate(line: str) -> str:
    line = line.replace("one", "o1ne")
    line = line.replace("two", "t2wo")
    line = line.replace("three", "t3hree")
    line = line.replace("four", "f4our")
    line = line.replace("five", "f5ive")
    line = line.replace("six", "s6ix")
    line = line.replace("seven", "s7ven")
    line = line.replace("eight", "e8ight")
    line = line.replace("nine", "n9ine")
    return line


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
    print(day01("day 01/day01part2.test"))
    print(day01("day 01/day01part2.input"))
