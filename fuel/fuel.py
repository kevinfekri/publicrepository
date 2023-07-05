def main():
    fraction = valid()
    fuel(fraction)

def valid():
    while True:
        try:
            fraction = input("fraction: ")
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if x <= y and y != 0:
                return fraction
        except (ValueError, ZeroDivisionError):
            pass

def fuel(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if 99 <= x/y * 100 :
        print("F")
    elif x/y * 100 <= 1:
        print("E")
    else:
        print(f"{round(x/y * 100)}%")

main()
