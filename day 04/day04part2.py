from tooling.file_access import get_content


def day04part2(filename: str) -> int:
    pile_cards = get_content(filename)
    cards = [1] * len(pile_cards)
    for card_index, line in enumerate(pile_cards):
        # remove card name and index, then split winning and own numbers
        values_list = line.split(":")[1].split("|")
        # winning numbers, numbers you have
        winnings = [int(value) for value in values_list[0].split()]
        own = [int(value) for value in values_list[1].split()]
        n = len(set(winnings) & set(own))
        for j in range(card_index + 1, min(card_index + 1 + n, len(pile_cards))):
            cards[j] += cards[card_index]
    return sum(cards)


if __name__ == "__main__":
    test_result = day04part2("input-files/day04part1.test")
    print(test_result)
    assert test_result == 30

    test_result = day04part2("input-files/day04part2.input")
    print(test_result)
    # assert test_result == 26914
