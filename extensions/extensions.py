name = input("File name: ").strip().casefold()

if name.endswith((".gif", ".png")) == True:
    name = name.rsplit(".")
    print(f"image/{name[-1]}")
elif name.endswith((".jpg", ".jpeg")) == True:
    print("image/jpeg")
elif name.endswith((".pdf", ".zip")) == True:
    name = name.rsplit(".")
    print(f"application/{name[-1]}")
elif name.endswith(".txt") == True:
    name = name.split(".")
    print(f"text/{name[0]}")
else:
    print("application/octet-stream")
