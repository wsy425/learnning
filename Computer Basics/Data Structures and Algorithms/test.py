def generate(numRows):
    total_list = []
    p = [1]
    j ,i= 0,0
    while j < numRows:
        total_list.append(p)
        size = len(p)
        p = []
        i = 0
        while i <= size:
            if i == 0:
                p.append(1)
            elif i == size:
                p.append(1)
            else:
                p.append(total_list[j][i-1]+total_list[j][i])
            i += 1
        j += 1
    return total_list
generate(5)