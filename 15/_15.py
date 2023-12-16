file = open("Input.txt", "r")
charStrings = file.readline().split(",")

total = 0
for string in charStrings:
    currentValue = 0
    for i in range(len(string)):
        currentValue += ord(string[i])
        currentValue *= 17
        currentValue %= 256
    total += currentValue
print(total)