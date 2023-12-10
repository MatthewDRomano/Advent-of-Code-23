
text = open("Input.txt", "r")
lines = text.read().splitlines()

winning_nums = []
your_nums = []
total = 0

for i in range(0, len(lines)):
    winning_nums.append((lines[i][10:lines[i].find("|")]).split(" "))
    your_nums.append((lines[i][lines[i].find("|")+2:]).split(" "))

for line in range(0, len(your_nums)):
    points = 1
    for num in your_nums[line]:
        if num == "": continue
        if num in winning_nums[line]:
            points *= 2
    total += int(points/2)
print(total)

