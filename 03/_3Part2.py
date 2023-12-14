file = open("Input.txt", "r")
lines = file.read().splitlines()

def main():
    gearRatioSum = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (lines[i][j] == "*"):
                nums = surroundingNumbers(i, j)
                if (len(nums) == 2):
                    gearRatioSum += (nums[0] * nums[1])
    print(gearRatioSum)

def surroundingNumbers(i, j): # row, col THIS METHOD IS HARD CODED
    nums = []
    if isInt(lines[i][j-1]) and isInt(lines[i][j+1]): #left and right
        nums.append(getNumber(i,j-1))
        nums.append(getNumber(i,j+1))
        return nums
    elif isInt(lines[i-1][j]) and isInt(lines[i+1][j]): #top and bottom
        nums.append(getNumber(i-1,j))
        nums.append(getNumber(i+1,j))
        return nums
    elif isInt(lines[i-1][j-1]) and isInt(lines[i+1][j+1]): #topLeft and bottomRight
        nums.append(getNumber(i-1,j-1))
        nums.append(getNumber(i+1,j+1))
        return nums
    elif isInt(lines[i-1][j+1]) and isInt(lines[i+1][j-1]): #topRight and bottomLeft
        nums.append(getNumber(i-1,j+1))
        nums.append(getNumber(i+1,j-1))
        return nums
    
    elif (isInt(lines[i-1][j-1]) and isInt(lines[i-1][j+1]) and not isInt(lines[i-1][j])): #top left and top right
        nums.append(getNumber(i-1, j-1))
        nums.append(getNumber(i-1, j+1))
        return nums

    elif (isInt(lines[i+1][j-1]) and isInt(lines[i+1][j+1]) and not isInt(lines[i+1][j])): #top left and top right
        nums.append(getNumber(i+1, j-1))
        nums.append(getNumber(i+1, j+1))
        return nums
    
    elif (isInt(lines[i][j+1]) and isInt(lines[i+1][j])): #Right middle and bottom middle
        nums.append(getNumber(i, j+1))
        nums.append(getNumber(i+1, j))
        return nums
    elif (isInt(lines[i][j+1]) and isInt(lines[i+1][j-1])):#Right middl;e and Bottom Left
        nums.append(getNumber(i, j+1))
        nums.append(getNumber(i+1, j-1))
        return nums
    elif (isInt(lines[i][j+1]) and isInt(lines[i-1][j])): #Right middle and Top middle
        nums.append(getNumber(i, j+1))
        nums.append(getNumber(i-1, j))
        return nums
    elif (isInt(lines[i][j+1]) and isInt(lines[i-1][j-1])):#Right middle and Top Left
        nums.append(getNumber(i, j+1))
        nums.append(getNumber(i-1, j-1))
        return nums

    elif (isInt(lines[i][j-1]) and isInt(lines[i+1][j])): #Left middle and Bottom Middle
        nums.append(getNumber(i, j-1))
        nums.append(getNumber(i+1, j))
        return nums
    elif (isInt(lines[i][j-1]) and isInt(lines[i+1][j+1])): #Left middle andBottom Right
        nums.append(getNumber(i, j-1))
        nums.append(getNumber(i+1, j+1))
        return nums
    elif (isInt(lines[i][j-1]) and isInt(lines[i-1][j])): #Left middle and Top Middle
        nums.append(getNumber(i, j-1))
        nums.append(getNumber(i-1, j))
        return nums
    elif (isInt(lines[i][j-1]) and isInt(lines[i-1][j+1])): #Left middle andTop Right
        nums.append(getNumber(i, j-1))
        nums.append(getNumber(i-1, j+1))
        return nums
    
    elif (isInt(lines[i-1][j+1]) and isInt(lines[i+1][j+1])):#Top/Bottom Rights
        nums.append(getNumber(i-1, j+1))
        nums.append(getNumber(i+1, j+1))
        return nums
    elif (isInt(lines[i-1][j-1]) and isInt(lines[i+1][j-1])):#Top / Bottom Lefts
        nums.append(getNumber(i-1, j-1))
        nums.append(getNumber(i+1, j-1))
        return nums
  
    return nums

def getNumber(i, j):
    num = [lines[i][j]]

    if inBounds(i, j-1) and isInt(lines[i][j-1]):
        num.insert(0, lines[i][j-1])
        if inBounds(i, j-2) and isInt(lines[i][j-2]):
            num.insert(0, lines[i][j-2])

    if (inBounds(i, j+1) and isInt(lines[i][j+1])):
        num.append(lines[i][j+1])
        if (inBounds(i, j+2) and isInt(lines[i][j+2])):
            num.append(lines[i][j+2])

    print(''.join(num))        
    return int(''.join(num))


def inBounds(r, c):
    if (c < 0 or c >= len(lines[0])):
        return False
    if (r < 0 or r >= len(lines)):
        return False
    return True

def isInt(c):
    return ord(c) > 47 and ord(c) < 58

if __name__ == "__main__":
    main()