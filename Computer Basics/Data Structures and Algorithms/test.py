def lengthOfLastWord(s):
    #s = s.rstrip()
    s = s[::-1]
    s = s.split(' ',1)[0]
    return len(s)
lengthOfLastWord("b   acd    ")