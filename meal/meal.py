def main():
    time = input("What time is it? ")
    output = convert(time)
    if 7.00 <= output <= 8.00:
        print("breakfast time")
    elif 12.00 <= output <= 13.00:
        print("lunch time")
    elif 18.00 <= output <= 19.00:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes) * 100/60
    minutes = int(minutes)

    output = f"{hours}.{minutes}"
    output = float(output)

    return output

if __name__ == "__main__":
    main()
