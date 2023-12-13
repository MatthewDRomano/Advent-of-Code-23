file = open("Input.txt", "r")
lines = file.read().splitlines()

def main():
    
    galaxy = []
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if (lines[row][col] == "#"):
                galaxy.append((row, col))

    sumOfPaths = 0

    for i in range(len(galaxy)):
        for j in range(i + 1, len(galaxy)):
            rowDistance = 0
            for y in range(min(galaxy[i][0], galaxy[j][0]), max(galaxy[i][0], galaxy[j][0])):
                if '#' not in lines[y]:
                    rowDistance += 1000000
                else: rowDistance += 1
            sumOfPaths += rowDistance

            colDistance = 0
            for x in range(min(galaxy[i][1], galaxy[j][1]), max(galaxy[i][1], galaxy[j][1])):
                column = getColumn(x)
                if '#' not in column:
                    colDistance += 1000000
                else: colDistance += 1
              
            sumOfPaths += colDistance
    
    print(sumOfPaths)

def getColumn(j):
  col = []
  for i in range(len(lines)):
    col.append(lines[i][j])
  return col


if __name__ == "__main__":
  main()