def recurse(line):
    print(line)
    if sum(value != 0 for value in line) == 0:
        return 0
    steps = []
    for i in range(len(line) - 1):
        steps.append(line[i + 1] - line[i])
    return line[-1] + recurse(steps)


def get_content(filename: str) -> (str, dict):
    with open(filename, "r") as file:
        content = file.read().split("\n")
    data = [value.split() for value in content]
    return [[int(value) for value in line] for line in data]


def day09part2(filename: str) -> int:
    report = get_content(filename)
    # same as part1 but reverse the list
    return sum(recurse(line[::-1]) for line in report)


if __name__ == "__main__":
    test_result = day09part2("input-files/day09part1.test")
    print(test_result)
    assert test_result == 2

    test_result = day09part2("input-files/day09part2.input")
    print(test_result)
    assert test_result == 933
