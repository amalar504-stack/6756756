with open("data.txt", "r") as f:
    text = f.read()

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = ""

for ch in text:
    found = False

    for i in range(len(lower)):
        if ch == lower[i]:
            if i == 25:
                result += lower[0]
            else:
                result += lower[i + 1]
            found = True
            break

    if not found:
        for i in range(len(upper)):
            if ch == upper[i]:
                if i == 25:
                    result += upper[0]
                else:
                    result += upper[i + 1]
                found = True
                break

    if not found:
        result += ch

with open("encrypted.txt", "w") as f:
    f.write(result)