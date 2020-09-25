def isValid(s):
    dic = {')':'(',']':'[','}':'{'}
    stack = []
    for i in s:
        if stack and i in dic:
            if stack[-1] == dic[i]: 
                stack.pop()
            else: return False
        else:
            stack.append(i)
    return not stack

print(isValid("{[]}"))
'''
# 朴素模式匹配算法
def Pattern_matching(str_1 , str_2):
    while i<len(str_1):
        while j<len(str_2):
            if str_1[i] == str_2[j]:
                i += 1
                j += 1
            else:
'''                