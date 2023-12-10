def main():
    file = open("Input.txt", "r")
    sequenceArr = file.read().splitlines()

    sum1, sum2 = 0, 0
    for sequence in sequenceArr:
        numArr = (sequence.split(" "))
        sum1 += predict(numArr) #part 1
        sum2 += predict(numArr[::-1]) #part 2
    print(f"Part 1: {sum1}\nPart 2: {sum2}")

def sequenceNotFinished(sequence):
    for i in range(len(sequence)):
        if sequence[i] != 0:
            return True
    return False

def predict(sequence):
    finalCol = []  
    
    while sequenceNotFinished(sequence): 
        newSequence = []
        finalCol.append(sequence[len(sequence)-1])
        for num in range(len(sequence)-1):
            newSequence.append(int(sequence[num+1]) - int(sequence[num]))
        sequence = newSequence
    finalCol.append(0)

    predictCol = []
    predictCol.append(0)
    for i in range(len(finalCol)-1):
        predictCol.append(int(finalCol[len(finalCol)-2-i]) + int(predictCol[i]))
    
    return predictCol[len(predictCol)-1]

if __name__ == "__main__":
    main()