def main():
    valid()


def valid():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            date = str(input("Date: ")).removeprefix('"').removesuffix('"').removeprefix(" ").removesuffix(" ")
            if "/" in date:
                month, days, year = date.split("/")
                if month.isdigit() == True and days.isdigit() == True and year.isdigit() == True:
                    month = int(month)
                    days = int(days)
                    year = int(year)
                    if 1 <= month <= 12 and 1 <= days <= 31:
                        print(f"{year}-{month:02}-{days:02}")
                        break
            elif "," in date:
                month, days, year = date.replace(",", "").split(" ")
                if month in months and days.isdigit() == True and year.isdigit() == True:
                    days = int(days)
                    year = int(year)
                    for i in range(len(months)):
                        if month == months[i]:
                            month = i + 1
                            month = int(month)
                    if 1 <= month <= 12 and 1 <= days <= 31:
                        print(f"{year}-{month:02}-{days:02}")
                        break
        except ValueError:
            pass


main()
