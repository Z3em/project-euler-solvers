# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def IsPrime(number):
    upperBound = number
    for f in range(2, upperBound):
        if (number % f == 0):
            return False
        else:
            upperBound = number/f
    return True


primes = []
powers = []

for i in range(2, 21):
    if IsPrime(i):
        primes.append(i)
        powers.append(1)
    else:
        for p in range(0, len(primes)):
            while (i % (primes[p] ** (powers[p]+1)) == 0):
                powers[p] += 1

result = 1
for p in range(0, len(primes)):
    result = result * (primes[p] ** powers[p])
print(result)
