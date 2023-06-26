import emoji


def main():
    text = input("Input: ")
    if text.rstrip("_") == True:
        print(emoji.emojize(f"Output: {text}"))
    else:
        print(emoji.emojize(f"Output: {text}", language = "alias"))


main()
