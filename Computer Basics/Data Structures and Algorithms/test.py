def partitionLabels(S):
    i , j = 0 , 0
    list_1 = []
    while i <len(S):
        per = S[i]
        z = 0
        while z < len(per):
            if per[z] in S[i+1:]:
                i =max(i , len(S) - S[::-1].index(per[z]) -1)
                per = ''.join(set(S[j:i]))
            else:
                z += 1
        i += 1
        list_1.append(i-j)
        j = i
    return list_1
partitionLabels("mlullbhiuiujgvwvurcdvhzdk")