def largestPerimeter(A):
    A.sort()
    for i in range(1,len(A)-1):
        if A[-i] < A[-i-1] + A[-i-2]:
            return A[-i]+A[-i-1]+A[-i-2]
    return 0
largestPerimeter([2,1,2])