from pyfiglet import Figlet
from random import choice
import sys


def main():
    figlet = Figlet()
    list = figlet.getFonts()
    if len(sys.argv) == 1:
        text = input("Input: ")
        figlet.setFont(font=random.choice(list))
        print(f"Output: \n{figlet.renderText(text)}")
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        i = sys.argv[2]
        if i in list:
            text = input("Input: ")
            figlet.setFont(font=i)
            print(f"Output: \n{figlet.renderText(text)}")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


main()
