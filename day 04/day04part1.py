from tooling.file_access import get_content


def day04part1(filename: str) -> int:
    pile_cards = get_content(filename)
    numbers_pairs = []
    worth = 0
    for line in pile_cards:
        # remove card name and index, then split winning and own numbers
        values_list = line.split(":")[1].split("|")
        # winning numbers, numbers you have
        winnings = [int(value) for value in values_list[0].split()]
        own = [int(value) for value in values_list[1].split()]
        numbers_pairs.append([winnings, own])
    for pair in numbers_pairs:
        matches = [value for value in pair[1] if value in pair[0]]
        if len(matches) > 0:
            worth += 2 ** (len(matches) - 1)
    return worth


if __name__ == "__main__":
    test_result = day04part1("input-files/day04part1.test")
    assert test_result == 13
    print(test_result)
    test_result = day04part1("input-files/day04part1.input")
    assert test_result == 26914
    print(test_result)
