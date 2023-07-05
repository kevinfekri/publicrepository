input = input("Expression: ")

x, y, z = input.split(" ")

x = int(x)
z = int(z)

if y == "+":
    output = x + z
    print(f"{output:.1f}")
elif y == "-":
    output = x - z
    print(f"{output:.1f}")
elif y == "/" and z != 0:
    output = x / z
    print(f"{output:.1f}")
elif y == "*":
    output = x * z
    print(f"{output:.1f}")
elif y == "/" and z == 0:
    print("Cannot divide by 0")
