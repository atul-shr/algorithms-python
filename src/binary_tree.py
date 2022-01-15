import math

test = {
    "input": {
        "cards": [13, 12, 11, 7, 6, 5, 3, 2, 1],
        "query": 7
    },
    "output": 3
}


def locate_cards(cards, query):
    position = 0

    while True:
        if cards[position] == query:
            return position

        if position == len(cards):
            return -1

        position += 1


print(locate_cards(**test["input"]) == test["output"])

