camel = input("camelCase: ")

for i in camel:
    if i.isupper() == True:
        i = i.replace(i, f"_{i.lower()}")
    print(i, end="")
print()
