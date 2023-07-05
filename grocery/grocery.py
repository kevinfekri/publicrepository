def main():
    my_list = {}
    while True:
        try:
            item = input("").upper()
            if item not in my_list:
                my_list[item] = 1
            elif item in my_list:
                my_list[item] += 1
        except KeyError:
            pass
        except EOFError:
            sorted_my_list = sorted(my_list.items())
            for key, value in sorted_my_list:
                print(value, key)
            break


main()
