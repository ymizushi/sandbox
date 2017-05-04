#!/usr/bin/env python3

def fizzbuzz(n):
    if (n % 3) == 0 and (n % 5) == 0:
        print("{}, fizzbuzz".format(n))
    elif (n % 3 == 0):
        print("{}, fizz".format(n))
    elif (n % 5 == 0):
        print("{}, buzz".format(n))
    else:
        pass

[fizzbuzz(i) for i in range(20)]
