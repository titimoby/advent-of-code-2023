import math 


def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.read().split('\n')
    return content


def day06part1(filename: str) -> int:
    data = get_content(filename)
    r = int(data[0].replace("Time:", "").strip().replace(" ", ""))
    d = int(data[1].replace("Distance:", "").strip().replace(" ", ""))

    solution = 1
    delta = math.sqrt(pow(r, 2) - 4 * d)
    c1 = math.ceil((r + delta)/2)
    c2 = math.floor((r - delta)/2)
    print(f"c1=${c1} c2=${c2}")
    solution = c1 - c2 - 1
    return solution

if __name__ == "__main__":
    test_result = day06part1("input-files/day06part1.test")
    print(test_result)
    assert test_result == 71503

    test_result = day06part1("input-files/day06part2.input")
    print(test_result)
    assert test_result == 27102791