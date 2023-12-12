# Generating the binomial coefficient recursively
def bin(n, k):
    if(k == 0 or n ==k):
        return 1
    else:
        return bin(n-1, k) + bin(n-1, k)


# Testing 
# This kills our stack 
# print(bin(9000,34))
# We need a better approach 

# 3!/(2!(1!)) = 6/2 = 2

# Using dynamic programming
def binDyn(n, k):
    b  = [([0]* n) for _ in range(n+1) ]   
    i = 0
    while i <= n:
        j = 0
        while(j <= min(i, k)):
            if(j == 0 or  j == i):
                b[i][j] = 1
            else:
                b[i][j] = b[i - 1][j - 1] + b[i - 1][j]
            j = j + 1
        i = i + 1
    return b[n][k]


# Testing 

print(binDyn(9000,4))

# Note to self: use while loops they are lot easier 