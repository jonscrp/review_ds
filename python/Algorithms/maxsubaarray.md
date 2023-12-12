# Overview


a = [0, 1, -2, 3, 4, -5, 6, -7]



maxSum_0  = 0 

maxSum_1 = max(0, maxSum_0 + a[t]) = 1

maxSum_2 = max(0, maxSum_1 + a[t]) = 0  // all subarrays ending at t can be ignored

maxSum_3 = max(0, maxSum_2 + a[t]) = 3

maxSum_4 = max(0, maxSum_3 + a[t]) = 7

maxSum_5 = max(0, maxSum_4 + a[t]) = 2

maxSum_6 = max(0, maxSum_5 + a[t]) = 8

maxSum_7 = max(0, maxSum_6 + a[t]) = 1
