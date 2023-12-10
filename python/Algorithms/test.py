def Merge(h, m, a, b, o):
    idxa = 0
    idxb = 0
    idxo = 0
    while idxa < h and idxb < m:
        if a[idxa] < b[idxb]:
            o[idxo] = a[idxa]
            idxa += 1
        else:
            o[idxo] = b[idxb]
            idxb += 1
        idxo += 1

    idxo -= 1

    if idxa < h:
        while idxa < h:
            o[idxo] = a[idxa]
            idxa += 1
            idxo += 1
    else:
        while idxb < m:
            o[idxo] = b[idxb]
            idxb += 1
            idxo += 1


def MergeSort(n, o):
    h = n // 2
    m = n - h

    if n > 1:
        a = [0] * h
        b = [0] * m
        for i in range(h):
            a[i] = o[i]

        for i in range(m):
            b[i] = o[h + i]

        MergeSort(h, a)
        MergeSort(m, b)
        Merge(h, m, a, b, o)


o = [1, 2, 3, 7, 4, 3, 2]
MergeSort(len(o), o)

for i in o:
    print(i)
