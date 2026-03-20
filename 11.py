with open("data.txt", "r") as f:
    data = f.read()

with open("backup.txt", "w") as f:
    f.write(data)