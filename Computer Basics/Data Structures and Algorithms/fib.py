# 递归法
def fbi1(n):
    if n<2:
        return 1
    else:
        return fbi1(n-1) + fbi1(n-2)

# 动态规划
f = 0
g = 1
while (0 < n):
    g = g + f
    f = g - f
    return g