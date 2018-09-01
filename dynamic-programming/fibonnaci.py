max_number = 20
memo = [None]*max_number

def fib(n):
    if (n == 0 or n == 1):
        return n
    if (memo[n] == None):
        memo[n] = fib(n-2) + fib(n-1)
    
    return memo[n]

if __name__=="__main__":
    for i in range(max_number):
        print fib(i)