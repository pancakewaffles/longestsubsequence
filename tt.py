a = []
with open('hard.txt','r') as r:
    for line in r:
        a.append(int(line))

# Python program to find 
# length of longest 
# increasing subsequence 
# in O(n Log n) time 
  
# Binary search (note 
# boundaries in the caller) 
# A[] is ceilIndex 
# in the caller 
def CeilIndex(A, l, r, key): 
  
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 
   
def LongestIncreasingSubsequenceLength(A, size): 
  
    # Add boundary case, 
    # when array size is one 
   
    tailTable = [0 for i in range(size + 1)] 
    len1 = 0 # always points empty slot 
   
    tailTable[0] = A[0] 
    len1 = 1
    for i in range(1, size): 
      
        if (A[i] < tailTable[0]): 
  
            # new smallest value 
            tailTable[0] = A[i] 
   
        elif (A[i] > tailTable[len1-1]): 
  
            # A[i] wants to extend 
            # largest subsequence 
            tailTable[len1] = A[i] 
            len1+= 1
   
        else: 
            # A[i] wants to be current 
            # end candidate of an existing 
            # subsequence. It will replace 
            # ceil value in tailTable 
            tailTable[CeilIndex(tailTable, -1, len1-1, A[i])] = A[i] 
          
   
    return len1

print(LongestIncreasingSubsequenceLength(a,len(a)))
