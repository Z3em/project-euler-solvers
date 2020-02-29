# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

previous = 0
current = 1
mySum = 0
while (current < 4000000):
    if (current % 2 == 0):
        mySum += current
    temp = current
    current += previous
    previous = temp
print(mySum)
