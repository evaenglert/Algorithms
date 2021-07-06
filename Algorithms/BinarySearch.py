# This is a Python script for Binary search implementation
import math

def binarySearch(numberToLook, arrayOfIntegers):
    arrayOfIntegers.sort()
    startOfArray = 0
    endOfArray = len(arrayOfIntegers) - 1
    numberOfSearches = 0

    while startOfArray <= endOfArray:
        numberOfSearches = numberOfSearches + 1
        indexToLookUp = math.floor((startOfArray + endOfArray)/2)
        print(f'Checking at index {indexToLookUp}')
        if arrayOfIntegers[indexToLookUp] == numberToLook:
            pintReturn = indexToLookUp
            print(f'Number of tries: {numberOfSearches}, index is {indexToLookUp}')
            break
        elif arrayOfIntegers[indexToLookUp] > numberToLook:
            endOfArray = indexToLookUp - 1
            print(f'At index {indexToLookUp} we have {arrayOfIntegers[indexToLookUp]}, this is larger than {numberToLook}. Interval starts at {startOfArray} and ends at {endOfArray}')
        else:
            startOfArray = indexToLookUp + 1
            print(f'At index {indexToLookUp} we have {arrayOfIntegers[indexToLookUp]}, this is smaller than {numberToLook}. Interval starts at {startOfArray} and ends at {endOfArray}')



