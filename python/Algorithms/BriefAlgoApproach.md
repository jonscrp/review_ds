## Algorithms 

> Goal of this..review for my csci323 exam lol

### Divide and conquer?


Steps 
    * Divide 
    * Conquer
    * Obtain (merge)


Divides a problem into "a" sub problems of size "n/b". 
    (aT(n) + f(x))

Until the smaller subproblem is solvable. Then we can combine this smaller subproblems upward until we have solved the original problem

Notes: 

top down approach 

the **sub problems are unrelated**

for example merge sort 

the left and right side need to be sorted indepently and the merged

**Example:**

Matrix Multiplication: 


#### SORT

Lower bound for sorting algorithms is OMEGA(nlogn)

[__Selection Sort__]()

Runtime: O(n^2)

In-place
used for small data sets ( < 1k)

[__Insertion Sort__]()
Runtime: O(n^2)
NOTES: 
in-place 
used for small data sets (< 1k>)

[__Heap Sort__]()
Runtime: O(nlogn)
in-place
used for large data sets (1k-1m)


***Divide and Conquer Examples** 

[__Merge Sort__](/python/Algorithms/MergeSort.py)
Run time : O(nlogn)
Height: O(logn)
NOTES:
sequential data access
used for huge datasets ( > 1m)

[__Quick Sort__]()
seudo linear time
NOTES:
in-place
randomized 
good for large inputs
Worse case occurs when the pivot is the unique minimum or maximum element
O(n^2)


#### Search 

[__Binary Search__](/python/Algorithms/MergeSort.py)
Run Time:
O(logn)
NOTES:


### Dynamic Programming


Steps: 
    * Establish a recursice property that solves the problem
    * Solve the problem in a bottom up approach that is solve the smaller problems first.

**The Binomial Coefficient**

We all know the binomial formula for nCr

n! / (r!(n-r)!)

as you can see this use factorials which we know tend to be really expensive computations if done recursively

what about a dynamic approach to solve this problem bottom up 

that is solve sub problems and store the results and used this results later if a **repeted computation** is necessary



**Floyd's Algorithm for Shortest Path**

Used to solve the shortest path problem which is an optimization problem

A silly approach would be to compute all pairs possible paths 
which will results in (n-2)! ... we want to stay away from factorials since they are expensice
[How?](https://youtu.be/aTvV27J3q3Y?si=JIrUceQUNuo6b0-i)


Let's try dinamic programming




**Review: **


[__Bellman Ford__]()


**Minimum Spanning Trees ** 

Cycle Property:
Replacing an edge will only happen if the edge being replaced by
has a smaller weight

Prevents cycles

Partition Property:
Adding or replacing an edge with simliar weigths will create a new MST

Assures the edge conneccting two sudsets of a MST are connected by the smallest edge

[__Djkstra__](0)

[__Kruskal__]()

__Matrix Multiplication__

[__Prim__]()

Algorithm 

```
 F  = None  // Wil contain our edges 

 Y  = [v1]  // Will contain vertex's visited

 while( the instance is not solved) //   ~ |Y| != |V|

    select a vertex V-Y  that is  // an adjacent vertex to any of the vertex's in Y 
    nearest to Y 
    
    add the vertex to Y
    add the edge to F

    if(Y == V)      // we have reached all vertex's
        the instance is solved
```



RunTime: Theta (n^2)




        





    


