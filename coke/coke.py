def main():
    price = int(50)
    while True:
        insert = int(input("Insert Coin: "))
        if insert == 25 or insert == 10 or insert == 5:
            price = price - insert
            if price > 0:
                print(f"Amount Due: {price}")
            elif price == 0:
                print(f"Change Owed: {price}")
                break
            elif price < 0:
                price = 0 - price
                print(f"Change Owed: {price}")
                break
        else:
            print(f"Amount Due: {price}")

main()
