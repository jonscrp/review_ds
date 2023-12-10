
# Generating the binomial coefficient tree
def bin(n, k):
    if(k == 0 or n ==k):
        return 1
    else:
        return bin(n-1, k) + bin(n-1, k)


# Testing 



# This kills our stack 
# print(bin(9000,34))
# We need a better aproach 

# 3!/(2!(1!)) = 6/2 = 2

def binDyn(n, k):
    i = 0
    j = 0

    B[[] for ]
    for i in range(n):
        for j in range(min(i,k)):
            if(j == 0 or  j== i):
                B[]

