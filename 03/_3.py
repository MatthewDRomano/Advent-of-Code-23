file = open("Input.txt", "r")
lines = file.read().splitlines()
class partOne:
    def main():
        total = 0
        for y in range(len(lines)):
            i = 0
            while i < len(lines[y]):
                if (isInt(lines[y][i])):
                    num = int(getNum(lines[y], i))
                    if isPartNumber(y, i, num):
                        total += int(num)
                    i += len(str(num)) - 1

                i += 1
        print(total)

def isPartNumber(row, col, num):
    x, y = col - 1, row - 1 #top left (for loop right)
    for i in range(x, x + len(str(num) + "") + 2):
       if (inBounds(i, y)):
               if (not isInt(lines[y][i]) and ord(lines[y][i]) != 46):            
                   return True
       
    x, y = col - 1, row + 1 #bottom left (for loop right)
    for i in range(x, x + len(str(num)) + 2):
        if (inBounds(i, y)):
            if (not isInt(lines[y][i]) and ord(lines[y][i]) != 46):
                  return True
          
    x, y = col - 1, row #middle left
    if (inBounds(x, y) and not isInt(lines[y][x]) and ord(lines[y][x]) != 46):
        return True

    x, y = col + len(str(num)), row #middle right 
    if (inBounds(x, y) and not isInt(lines[y][x]) and ord(lines[y][x]) != 46):
        return True
    
    return False

def inBounds(x, y):
    if (x < 0 or x >= len(lines[0])):
        return False
    if (y < 0 or y >= len(lines)):
        return False
    return True

def getNum(line, startIndex):
    newIndex = startIndex
    while newIndex <= len(line)-1 and isInt(line[newIndex]):
        newIndex += 1
    if (newIndex == startIndex):
        newIndex += 1
    return int(line[startIndex:newIndex])

def isInt(c):
    return ord(c) > 47 and ord(c) < 58

if __name__ ==  "__main__":
    partOne.main()  