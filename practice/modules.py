import math
import random
from pathlib import Path


def roll():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print(a, b)


def generate():
    coin = random.choice(["head", "tail"])
    print(coin)


def card():
    cards = ["King", "Queen", "Jack"]
    random.shuffle(cards)  # shaffle the original list
    print(cards)


def pa_th():
    members = ["a", "b", "c", "d"]
    x = math.floor(random.randint(25, 26))
    y = random.choice(members)

    path = Path()
    for file in path.glob("*.py"):
        print(file)







