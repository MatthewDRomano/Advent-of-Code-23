file = open("Input.txt", "r")
charStrings = file.read().split(",")

boxMap = {int:[]}
for i in range(256):
    boxMap.update({i : []})
def main():
    for string in charStrings:
        boxIndex = 0
        if '-' in string:
            boxIndex = hash(string.split('-')[0])

            box = boxMap.get(boxIndex)
            if (box is None or len(box) == 0): continue
            for i in range(len(box)):
                print(box[i])
                if box[i].split(" ")[0] == string.split('-')[0]:
                    box.remove(box[i])
                    boxMap.update({boxIndex : box})#
                    break
        elif '=' in string:
            focalLength = string.split('=')[1]
            boxIndex = hash(string.split('=')[0])
            newLabel = string.split("=")[0] + " " + focalLength
            box = boxMap.get(boxIndex)

            inBox = False
            if (box is None):
                tempList = []
                tempList.append(newLabel)
                boxMap.update({boxIndex : tempList})
            else:
                for i in range(len(box)):
                    if string.split('=')[0] in box[i]:
                        inBox = True
                        box[i] = newLabel
                        boxMap.update({boxIndex : box})
                        break
                if not inBox:
                    box.append(newLabel)
    totalFocusPower = 0
    for boxNum in range(256):
        for slotNum in range(len(boxMap.get(boxNum))):
            totalFocusPower += ((1 + boxNum) * (1 + slotNum) * int(boxMap.get(boxNum)[slotNum].split(" ")[1]))
    print(totalFocusPower)


def hash(string):
    hashValue = 0
    for i in range(len(string)):
        hashValue += ord(string[i])
        hashValue *= 17
        hashValue %= 256
    return hashValue


if __name__ == "__main__":
    main()