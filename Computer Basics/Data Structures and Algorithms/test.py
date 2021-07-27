def slidingPuzzle(board):
    neighbor = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
                3: [0, 4], 4: [3, 1, 5], 5: [4, 2]}
    start = ''
    target = '123450'
    for i in range(len(board)):
        for j in range(len(board[0])):
            start += str(board[i][j])

    queue = [start]
    visited = set()
    visited.add(start)
    step = 0
    while queue:
        for _ in range(len(queue)):
            cur = queue.pop(0)
            if cur == target:
                return step
            idx = cur.index('0')
            for near in neighbor[idx]:
                new = swap(cur, idx, near)
                if new not in visited:
                    queue.append(new)
                    visited.add(new)
        step += 1
    return -1


def swap(cur, i, j):
    cur_list = list(cur)
    cur_list[i], cur_list[j] = cur_list[j], cur_list[i]
    return "".join(cur_list)


slidingPuzzle([[1, 2, 3], [4, 0, 5]])
