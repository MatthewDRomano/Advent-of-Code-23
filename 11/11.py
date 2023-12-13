file = open("Input.txt", "r")
lines = file.read().splitlines()

def main():
  gravExpansion()

  sumOfPaths = 0

  galaxy = []
  for row in range(len(lines)):
    for col in range(len(lines[row])):
      if (lines[row][col] == "#"):
        galaxy.append((row, col))

  for i in range(len(galaxy)):  # doesnt check all pairs
    for j in range(i, len(galaxy)):
      sumOfPaths += (abs(galaxy[i][0] - galaxy[j][0])) + abs(
          (galaxy[i][1] - galaxy[j][1]))

  print(sumOfPaths)

def gravExpansion():
  r = 0
  while r < len(lines):  # row grav expansion
    if '#' not in lines[r]:
      lines.insert(r, str(lines[r]))
      r += 1
    r += 1

  c = 0
  while (c < len(
      lines[0])):  # col grav expansion (should work cant check at school)
    column = getColumn(c)
    if "#" not in column:
      for i in range(len(lines)):
        lines[i] = lines[i][:c] + '.' + lines[i][c:]
      c += 1
    c += 1

def getColumn(j):
  col = []
  for i in range(len(lines)):
    col.append(lines[i][j])
  return col

if __name__ == "__main__":
  main()