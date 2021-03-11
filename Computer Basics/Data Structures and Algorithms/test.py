def threeSumClosest(nums, target):
    nums.sort()
    res = nums[0] + nums[1] + nums[-1] - target
    for i in range(len(nums)-2):
        L = i + 1
        R = len(nums) - 1
        pre = nums[0] + nums[L] + nums[R] - target 
        while L < R:
            sums = nums[i] + nums[L] + nums[R] - target
            if sums == 0:
                return target
            if sums * pre < 0 and L != i+1:
                if abs(sums) < abs(pre):
                    pre = sums
                    break
                else:
                    break
            elif sums > 0:
                R -= 1
                pre = sums
            else:
                L += 1
                pre = sums 
        if abs(res) > abs(pre):
            res = pre
    return res + target
threeSumClosest([1,2,5,10,11],12)