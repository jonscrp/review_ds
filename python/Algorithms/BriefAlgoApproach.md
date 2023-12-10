## Algorithms 

> Goal of this..review for my csci323 exam lol

### Divide and conquer?
    - Divides a problem in "a" sub problems of size "n/b".
    - Until the smaller subproblem is solvable. Then we can combine this smaller subproblems upward until we have solved the original problem


    Examples:

    Binary Search 

        Given a list of elements a = [1,2,3,4, 5, ... n-1, n]
        find k 

        Algorithm BinarySearch(low, high):

            mid = (low + high)//2
            if(low > high)
                return -1
            elif( k == a[mid]):
                return mid
            elif( k < a[mid] ):
                return BinarySearch(low, mid-1)
            else:
                return BinarySearch(mid+1, high)

        
        base case at some point will be 1 > 0 if k wans't in the array 

        for example 

        a  = [1]

        mid = 0
        low = 0 // index
        high = 0 // index
    
        suppose k < a[mid]

        our BinarySearch(low, mid -1) // recursive call

        will make 

        mid = 0 + (-1)
        low = 0
        high = -1

        thus 

        if(low > high) will be true if the k isn't in the list





    


