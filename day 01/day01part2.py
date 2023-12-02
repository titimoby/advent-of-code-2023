from day01part1 import part1
from tooling.file_access import get_content


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


def day01part2(filename: str) -> str:
    content = get_content(filename)
    result = 0
    for line in content:
        result += part1(translate(line))
    return result


if __name__ == "__main__":
    test_result = day01part2("input-files/day01part2.test")
    assert (test_result == 281)
    print(test_result)
    input_result = day01part2("input-files/day01part2.input")
    assert input_result == 54094
    print(input_result)
