from day01part1 import part1


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


def day01(filename: str) -> str:
    with open(filename, "r") as file:
        content = file.readlines()
        result = 0
        for line in content:
            result += part1(translate(line))
    return result


if __name__ == "__main__":
    test_result = day01("day 01/day01part2.test")
    assert (test_result == 281)
    print(test_result)
    input_result = day01("day 01/day01part2.input")
    assert input_result == 54094
    print(input_result)
