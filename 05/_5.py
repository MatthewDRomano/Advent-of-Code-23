import sys

file = open("Input.txt", "r")
lines = file.read().split("\n\n")
def main(): 
    seedMap = lines[0].split(": ")[1]

    locationNumber = sys.maxsize
    for seed in seedMap.split(" "):
        #iterate through each row of soilMap and if seed in range of (source, source+range) then  that seed corresponds to soil (destination + (seed-source))
        number = recursiveSearch(1, int(seed))
        if number is not None:
            locationNumber = min(locationNumber, number)
    print(locationNumber)

def recursiveSearch(mapIndex, num):
    if mapIndex == len(lines):
        return num
    mapRows = lines[mapIndex].split(":\n")[1].split("\n") #each row in desired map
    destination, source, range, = int(mapRows[0].split(" ")[0]), int(mapRows[0].split(" ")[1]), int(mapRows[0].split(" ")[2])
    for row in mapRows:
        destination, source, range, = int(row.split(" ")[0]), int(row.split(" ")[1]), int(row.split(" ")[2])
        if num >= source and num < source + range:
            return recursiveSearch(mapIndex+1, destination + (num - source))      

if __name__ == "__main__":
    main()