import inflect
import sys


def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except ValueError:
            pass
        except EOFError:
            mylist = p.join(names)
            print(f" Adieu, adieu, to {mylist}")
            break

main()
