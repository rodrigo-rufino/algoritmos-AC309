from __future__ import print_function
import math

max_number = 20
memo = [[None for i in range(max_number)] for j in range(max_number)]

def bi_coef(n, k):
    if (k == 0 or k == n):
        return 1
    if (memo[n][k] == None):
        memo[n][k] = bi_coef(n-1, k-1) + bi_coef(n-1, k)
    return memo[n][k]

def bi_coef_slow(n, k):
    # c = (math.factorial(n))/(math.factorial(k)*(math.factorial(n-k)))
    if (k == 0 or k == n):
        return 1
    else:
        c = bi_coef_slow(n-1, k-1) + bi_coef_slow(n-1, k)
    return c

if __name__=="__main__":
    for n in range(max_number):
        for k in range(0, n+1):
            bi_coef(n, k)
            print(bi_coef(n, k), " ", end="")
        print("\n")

