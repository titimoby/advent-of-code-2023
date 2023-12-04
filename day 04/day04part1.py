from tooling.file_access import get_content


def day04part1(filename: str) -> int:
    pile_cards = get_content(filename)
    worth = 0
    for card in pile_cards:
        winnings, own = map(str.split, card.split('|'))
        matches = set(winnings) & set(own)
        worth += 2 ** (len(matches) - 1) if matches else 0
    return worth


if __name__ == "__main__":
    test_result = day04part1("input-files/day04part1.test")
    assert test_result == 13
    print(test_result)
    test_result = day04part1("input-files/day04part1.input")
    assert test_result == 26914
    print(test_result)
