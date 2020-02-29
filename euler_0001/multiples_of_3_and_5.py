# Find the sum of all the multiples of 3 or 5 below 1000.

mySum = currentNumber = 0
while currentNumber < 1000:
    mySum += currentNumber
    currentNumber += 3
currentNumber = 0
while currentNumber < 1000:
    if (currentNumber % 3 != 0):
        mySum += currentNumber
    currentNumber += 5
print(mySum)
