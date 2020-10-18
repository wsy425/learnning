def plusOne(digits):
    j = 0
    for i in range(1,len(digits)+1):
        if digits[-i] != 9:
            digits[-i] += 1 
            break
        digits[-i] = 0
        j += 1
    if j == len(digits):
        digits.insert(0, 1)
    return digits
plusOne([1,9,9])