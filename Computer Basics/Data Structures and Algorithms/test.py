def smallerNumbersThanCurrent(nums):
    place = [0]* (max(nums)+1)
    out = []
    for num in nums:
        place[num] += 1
    for i in range(1,len(place)):
        place[i] += place[i-1]
        i += 1
    for num in nums:
        out.append(place[num-1])
    return out
smallerNumbersThanCurrent([5,0,10,0,10,6])