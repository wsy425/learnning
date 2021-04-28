def findWays(n,m,board, points):
    x_1,y_1,x_2,y_2 = points[0]-1,points[1]-1,points[2]-1,points[3]-1
    road = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    r = [[-1] * m for _ in range(n)]
    r[x_1][y_1] = 0

    def go(x2,y2,index,x1,y1):
        if x1==x2 and y1==y2:
            return True
        for a,b in road:
            i,j = x1+a,y1+b
            if -1 < i < n and -1 < j < m and board[i][j]>=board[x1][y1] and (r[i][j]!=index-2 or r[i][j]==-1):
                if r[i][j] == -1:
                    r[i][j] = index
                else:
                    r[i][j] = min(r[i][j],index)
                go(x2,y2, index + 1, i, j)
        return False
    
    go(x_2,y_2,1,x_1,y_1)
    return r[x_2][y_2]

findWays(5,3,[[4,4,3],[3,5,4],[6,5,6],[7,4,10],[8,9,9]], [1,1,5,3])