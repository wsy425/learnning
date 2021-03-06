def lengthOfLongestSubstring(s):
    n = 0
    j = 0
    dick = set()
    for i in range(len(s)):
        if i != 0:
            dick.remove(s[i-1])
        while j<len(s) and s[j] not in dick:
            dick.add(s[j])
            j += 1
        n = max(n,j-i)
    return n
lengthOfLongestSubstring("pwwkew")