def reorganizeString(S):
    dic = {}
    max_value = 0
    max_key = 'a'
    T = ''
    j = 1
    for n in S:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
        if max_value < dic[n]:
            max_key , max_value = n , dic[n]
    if max_value > len(S) - max_value +1 :
        return ""
    else:
        T = max_key * max_value
        while j <len(S):
            for key,value in dic.items():
                if key != max_key:
                    for i in range(value):
                        T = T[:j] + key + T[j:]
                        j += 2
        return T
reorganizeString("eqmeyggvp")