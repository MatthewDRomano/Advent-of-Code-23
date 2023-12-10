def main():
    raceTime = 44899691
    raceDistance = 277113618901768

    totalWays = 0
    for secondsHeld in range(1, raceTime):
        timeToMove = raceTime - secondsHeld
        speed = secondsHeld
        distance = speed * timeToMove
        if (distance > raceDistance):
            totalWays += 1
    print(totalWays)

if __name__ == "__main__":
    main()