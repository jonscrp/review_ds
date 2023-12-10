
a = [1,2,3,4,5,6]
x = 9

def binarySearch(low, high):
    mid = 0
    if(low > high):
        return -1
    else:
        mid = (low + high)//2
        if(x == a[mid]):
            return mid
        elif(x < a[mid]):
            return binarySearch(low, mid-1)
        else:
            return binarySearch(mid + 1, high)
    

print(binarySearch(0,len(a)-1))
