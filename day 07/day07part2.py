from collections import defaultdict


def get_content(filename: str) -> list[str]:
    with open(filename, "r") as file:
        content = file.read().split("\n")
    return content


def index_value(card):
    return "J23456789TQKA".index(card)


def gives_score(hand):
    # by counting each card type, you can have a sort that exposes best combination
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    return sorted(counts.values(), reverse=True)


def score_with_jokers(hand):
    cards = "23456789TQKA"
    if "J" in hand:
        # evaluate every permutation of card when there are jokers
        return max([score_with_jokers(hand.replace("J", c, 1)) for c in cards])
    return gives_score(hand)


def score_with_tiebreak(hand):
    score = score_with_jokers(hand)
    # adding the value of all cards to figure out tie break in scores
    score.extend([index_value(x) for x in hand])
    return score


def day07part1(filename: str) -> int:
    card_order = "23456789TJQKA"
    data = get_content(filename)
    scores = []
    for line in data:
        hand, bid = line.split(" ")
        scores.append((score_with_tiebreak(hand), int(bid), hand))
    scores.sort()
    total = 0
    for rank, set_hand in enumerate(scores):
        bid = set_hand[1]
        total += (rank + 1) * bid
    return total


if __name__ == "__main__":
    test_result = day07part1("input-files/day07part1.test")
    print(test_result)
    assert test_result == 5905

    test_result = day07part1("input-files/day07part2.input")
    print(test_result)
    assert test_result == 246285222
