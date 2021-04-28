from collections import defaultdict
def findWords(board, words):
    n, m = len(board), len(board[0])

    shot = defaultdict(list)
    for i in range(n):
        for j in range(m):
            shot[board[i][j]].append((i, j))

    road = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def go(w, index, x, y):
        if index == len(w):
            return True
        r[x][y] = 0
        for a, b in road:
            i, j = x + a, y + b
            if -1 < i < n and -1 < j < m and r[i][j] 
            and board[i][j] == w[index] and go(w, index + 1, i, j):
                return True
        r[x][y] = 1
        return False
    
    res = []
    for w in words:
        for x, y in shot[w[0]]:
            r = [[1] * m for _ in range(n)]
            if go(w, 1, x, y):
                res.append(w)
                break
    return res

findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])