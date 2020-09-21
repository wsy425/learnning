import numpy as np
# 递归法
def LCS1(X,Y):
    if not X or not Y:
        return 0, ''
    if X[-1] == Y[-1]:
        length,s = LCS1(X[:-1], Y[:-1])
        return length + 1,s + X[-1]
    else:
        length1,s1 = LCS1(X[:-1], Y)
        length2,s2 = LCS1(X, Y[:-1])
        if length1 >= length2:
            return length1, s1
        else:
            return length2,s2

# 动态规划
def LCS2(X,Y):
    arr = np.zeros((len(X)+1, len(Y)+1))
    i = 0;j = 0
    s = ""
    if not X or not Y:
        return 0, ''
    else:
        while i in range(len(X)):
            while j in range(len(Y)):
                if X[i] == Y[j]:
                    arr[i+1,j+1] = arr[i,j] + 1
                    s += X[i]
                else :
                    arr[i+1,j+1] = max(arr[i,j+1] , arr[i+1,j])
                j += 1
            j = 0;i += 1
        return arr[-1,-1] , s 

X ="di"
Y ="das"
print(LCS2(X,Y))