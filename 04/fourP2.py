def main():
    text = open("Input.txt", "r")
    lines = text.read().splitlines()

    winning_nums = []
    your_nums = []
    totalCards = 0

    numOfEachCard = []
    for n in range(206):
        numOfEachCard.append(1)

    for i in range(0, len(lines)):
        winning_nums.append((lines[i][10:lines[i].find("|")]).split(" "))
        your_nums.append((lines[i][lines[i].find("|")+2:]).split(" "))

    for line in range(0, len(your_nums)):
        winners = 0
        for copy in range(numOfEachCard[line]):
            totalCards += 1
            for num in your_nums[line]:
                if num == "": continue
                if num in winning_nums[line]:
                    winners += 1
            for x in range(1, winners+1):
                numOfEachCard[line+x] += 1
    print(totalCards)


if __name__ == "__main__":
    main()