import sys
import os


def is_palindrome(x):
    temp = x
    new = 0
    while temp > 0:
        new = new * 10 + temp % 10
        temp = temp // 10
    return new == x


list1 = [48, 2984, 292, 930, 17641, 19731, 2456542]
for item in list1:
    print(is_palindrome(item))
