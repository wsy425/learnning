def getRow(rowIndex):
    q = [1]
    i,j,size = 0,0,0
    while i < rowIndex:
        size += 1
        p = q
        q = []
        j = 0
        while j <=size:
            if j == 0:
                q.append(1)
            elif j == size:
                q.append(1)
            else:
                q.append(p[j-1]+p[j])
            j += 1
        i += 1
    return q
getRow(3)