def maxSubArray(nums):
    i, j = 0, 0
    maxi ,maxj ,temp= nums[0], nums[0], 0
    while i < len(nums):
        while j < len(nums):
            temp += nums[j]
            maxj = max(maxj , temp)
            j += 1
        maxi = max(maxi , maxj)
        i += 1
        j = i
        temp = 0
    return maxi
maxSubArray([-2,1,-3,4,-1,2,1,-5,4])