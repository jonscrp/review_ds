c  =  [0,2,1,-6,3,2,4,-56,3,2,5,9,2,8, 0, -7, 78, 34,2,-108, 57,4]
d  = [0,1, -2, 3, 4, -5, 6, -7,]
g = [0,-14,  32, -30, 60 ,-360]



def maxSub(b):
    maxSum = [0]*len(b)
    i = 1
    maxSum = [0]*len(b)
    while(i < len(b) ):
        maxSum [i] = max( 0, (maxSum[i-1] + b[i]))
        i = i + 1


    print(maxSum)

    totalmax = 0
    for p in maxSum:
        if( p > totalmax):
            totalmax = p

    return totalmax


print(maxSub(g))

