o = [1,2,3,7,4,3,2]

def Merge(h,m, a,b,o ):
    idxa = 0  
    idxb = 0 
    idxo = 0
    while(idxa < h and idxb < m):
        if(a[idxa] < b[idxb]):
            o[idxo] = a[idxa]
            idxa = idxa + 1
        else:
            o[idxo] = b[idxb]
            idxb = idxb + 1
        idxo = idxo + 1
    idxo  = idxo -1

    if(idxa < h ):
        while(idxb < m):
            o[idxo] = a[idxb]
            idxa = idxa + 1
            idxo = idxo + 1
    else:
        while(idxa < h):
            o[idxo] = b[idxb]
            idxb  = idxb+ 1
            idxo = idxo + 1
    

def MergeSort(n, o):
    h = n//2   
 
    m = n-h 
  
    if(n > 1):
        a = [0]*h     
        b = [0]*m      
        for i in range(h):
            a[i] = o[i]

        for i in range(m):
            b[i] = o[h+i]

        MergeSort(h,a)
        MergeSort(m,b)
        Merge(h,m, a, b,o)


MergeSort(len(o), o)

for i in o:
    print(i)

