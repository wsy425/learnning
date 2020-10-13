# 朴素模式匹配算法
def Pattern_matching(str_1 , str_2):
    i = p = 0
    while i<len(str_1):
        i = p
        j = 0
        while j<len(str_2):
            if str_1[i] == str_2[j]:
                i += 1
                j += 1
            else:
                break
        if j == len(str_2):
            print(p)
            break
        p += 1
    return -1
Pattern_matching('aaaaa' , 'bba')
