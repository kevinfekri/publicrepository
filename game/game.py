import random
import sys
from cs50 import get_int


def main():
    n = number()
    while True:
        try:
            guess = get_int("Guess: ")
            if 0 < guess < n:
                print("Too small!")
            elif guess > n:
                print("Too large!")
            else:
                sys.exit("Just right!")
        except ValueError:
            pass


def number():
    while True:
        try:
            level = get_int("Level: ")
            if level > 1:
                n = random.randint(1, level)
                return n
                break
        except ValueError:
            pass


main()
