def generateMatrix(n):
    list1 = [[0 for _ in range(n)] for _ in range(n)]
    lrl,lll = -1,-1
    hrl,hll = n,n
    count = 1
    while count<n**2+1:
        for j in range(lll+1,hll):
            list1[lrl+1][j] = count
            count += 1
        lrl += 1
        for i in range(lrl+1,hrl):
            list1[i][hll-1] = count
            count += 1
        hll -= 1
        for j in range(hll-1,lll,-1):
            list1[hrl-1][j] = count
            count += 1
        hrl -= 1
        for i in range(hrl-1,lrl,-1):
            list1[i][lll+1] = count 
            count += 1
        lll += 1
    return list1
generateMatrix(3)