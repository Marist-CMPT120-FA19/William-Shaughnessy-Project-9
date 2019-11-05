def main():
    x = int(input("What is the MAX number: "))
    numList = [0] * (x -1) 
    for i in range(x):
        numList[i-1] = i + 1
        
    while (len(numList) > 0):
        prime = numList[0]
        print(prime, "is prime")
        numList.remove(prime)
        
        for i in numList:
            if (i % prime == 0):
                numList.remove(i)
main()