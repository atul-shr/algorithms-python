import math

tests = [{
    "input": {
        "cards": [13, 12, 11, 7, 6, 5, 3, 2, 1],
        "query": 7
    },
    "output": 3
}, {
    "input": {
        "cards": [],
        "query": 3
    },
    "output": -1
},
]


def locate_cards(cards, query):
    position = 0

    while position < len(cards):
        print(f"Looping for {position} times")
        if cards[position] == query:
            return position
        position += 1
    return -1


for test in tests:
    print(locate_cards(**test["input"]) == test["output"])
