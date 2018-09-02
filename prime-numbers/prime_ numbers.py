# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time, math

def isPrimeOddOnly(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, n):
        if (n%i == 0):
            return False
    return True

    
def isPrimeOddOnlyUntilHalf(n):
    if n == 2:
        return True
    if n%2 == 0 or n == 0 or n == 1:
        return False
    for i in range(3, n/2):
        if (n%i == 0):
            return False
    return True   


def isPrimeOddOnlyUntilSqrt(n):
    if n == 2:
        return True
    if n%2 == 0 or n == 0 or n == 1:
        return False
    for i in range(3, int(math.floor(math.sqrt(n)))):
        if (n%i == 0):
            return False
    return True     


def detectPrime():
    n = 179426549
    t = time.time()
    print n, "is prime?", isPrimeOddOnly(n)
    print "Execution time:", time.time() - t
    
    t = time.time()
    print n, "is prime?", isPrimeOddOnlyUntilHalf(n)
    print "Execution time:",time.time() - t
    
    t = time.time()
    print n, "is prime?", isPrimeOddOnlyUntilSqrt(n)
    print "Execution time:",time.time() - t
    
    
def generatePrime(n):
    a = range(2, n+1)
    for i in a:
        for j in a[i:]:
            if j%i == 0:
                a.remove(j)
    return a
    
    
if __name__=='__main__':
    #detectPrime()
    n = 1000
    t = time.time()
    print "Numeros primos até", n, ":", generatePrime(n)
    print "Execution time:",time.time() - t