var slidingPuzzle = function (board) {
    const neighbor = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [3, 1, 5], [4, 2]];
    let start = new String();
    const target = '123450';
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            start += board[i][j].toString();
        }
    }

    let queue = [start];
    let visited = [start];
    let step = 0;

    while (queue) {
        const n = queue.length
        for (let i = 0; i < n; i++) {
            const cur = queue.pop(0);
            if (cur == target) {
                return step
            }
            const index = cur.indexOf('0');
            for (const near of neighbor[index]) {
                const news = swap(cur, index, near);
                if (!visited.includes(news)) {
                    queue.push(news)
                    visited.push(news)
                }
            }
        }
        step += 1
    }
    return -1

    function swap(cur, i, j) {
        if (i < j) {
            return cur.slice(0, i) + cur[j] + cur.slice(i + 1, j) + cur[i] + cur.slice(j + 1)
        } else {
            return cur.slice(0, j) + cur[i] + cur.slice(j + 1, i) + cur[j] + cur.slice(i + 1)
        }

    }
};
const a = slidingPuzzle([[1, 2, 3], [5, 4, 0]])
