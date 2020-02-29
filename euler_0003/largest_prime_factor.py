def IsPrime(number):
    upperBound = number
    factor = 2
    while (factor <= upperBound):
        if (number % factor == 0):
            return False
        else:
            factor += 1
            upperBound = number/factor
    return True


bigNumber = 600851475143
upperBound = bigNumber
currentNumber = 2
factors = []
result = 0

while (currentNumber <= upperBound):
    if (bigNumber % currentNumber == 0):
        factors.append(currentNumber)
    upperBound = bigNumber/currentNumber
    currentNumber += 1

factors.reverse()
index = 0

for f in factors:
    if (IsPrime(f)):
        print(f)
        break
