def main():
    totalWaysProduct = 1
    races = [(44, 277), (89, 1136), (96, 1890), (91, 1768)] #time, distance
    for race in races:
        totalWaysProduct *= possibleWays(race)
    print(totalWaysProduct)

def possibleWays(race):
    totalWays = 0

    for secondsHeld in range(1, race[0]):
        timetToMove = race[0] - secondsHeld
        speed = secondsHeld
        distance = speed * timetToMove
        if (distance > race[1]):
            totalWays += 1
            
    return totalWays

if __name__ == "__main__":
    main()