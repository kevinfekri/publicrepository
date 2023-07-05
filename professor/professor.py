import random
from cs50 import get_int

def main():
    level = get_level()
    score = 0
    i = 0
    while i < 10:
        for i in range(10):
            i = i + 1
            problem = generate_integer(level)
            X,Y = problem.replace("=", "").split("+")
            X, Y = int(X), int(Y)
            for j in range(3):
                answer = get_int("")
                if answer == X + Y:
                    score += 1
                    break
                else:
                    print("EEE")
                    if j == 2:
                        print(f"{X} + {Y} = {X + Y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            list = ["1", "2", "3"]
            for i in list:
                if level == i:
                    return level
        except:
            pass


def generate_integer(level):
    if level == "1":
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level == "2":
        X = random.randint(10, 99)
        Y = random.randint(10, 99)
    elif level == "3":
        X = random.randint(100, 999)
        Y = random.randint(100, 999)
    output = f"{X} + {Y} ="
    print(output)
    return output


if __name__ == "__main__":
    main()
