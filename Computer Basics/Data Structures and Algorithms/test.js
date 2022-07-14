console.log(11111)
var imageSmoother = function (img) {
    let path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    let res = img
    for (let i = 0; i < img[0].length; i++) {
        for (let j = 0; j < img.length; j++) {
            let num = 0, account = 0
            for (let p of path) {
                if (i + p[1] > -1 && i + p[1] < img[0].length && j + p[0] > -1 && j + p[0] < img.length) {
                    num += 1
                    account += img[j][i]
                }
            }
            res[j][i] = Math.floor(account / num)
            console.log(res[j][i])
        }
    } return res
};
console.log(imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
