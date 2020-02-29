# Find the largest palindrome made from the product of two 3-digit numbers.
import math


def IsPalindrome(number):
    for i in range(0, math.ceil(len(number)/2)):
        if (number[i] != number[len(number)-1-i]):
            return False
    return True


largestPalindrome = 0

for a in range(100, 999):
    for b in range(a, 999):
        number = a*b
        if (number > largestPalindrome and IsPalindrome(str(number))):
            largestPalindrome = number

print(largestPalindrome)
