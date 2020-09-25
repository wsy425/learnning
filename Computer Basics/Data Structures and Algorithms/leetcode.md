# 1.两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, n in enumerate(nums):
            c = target - n
            if c in dic:
                return [dic[c] , i]
            else:
                dic[n] = i  
```
整数数组是关键
应用哈希表，产生与给定整数数组检索内容相反的元组

# 7.整数反转
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
## 转换为str
```python
def reverse(self, x: int) -> int:
    x_str = str(x)
    if x_str[0] != '-':
        x = int(x_str[::-1])
    else:
        x = - int(x_str[:0:-1]) # a[开始截取位置:结束截取位置:步长] 包括开始截取位置字符，不包括结束截取位置字符。步长-1则代表反向截取
    return x if -2147483648 < x < 2147483647 else 0
```
注意理解x_str[ :0:-1 ]的含义
## int反转
```python
def reverse(self, x: int) -> int:
    y,res = abs(x),0
    boundary = (1<<31) - 1 if x>0 else 1<<31 #<<二进制像左移动，相当于*2
    while y != 0:
        res = res * 10 + y % 10 #%取余数
        if res > boundary:
            return 0
        y //= 10 #//取整除
    return res if x>0 else -res
```
一次构建反转整数的一位数字。

# 9.回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
## 转换为str
```python
def isPalindrome(self, x: int) -> bool:
    s = str(x)
    return s == s[::-1]
```
## 不转换为str
```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    elif x == 0:
        return True
    else:
        import math
        length = int(math.log(x,10)) + 1
        L = length -1
        for i in range(length // 2):
            if x // 10 ** L != x % 10:
                return False
            x = (x % 10 ** L) // 10
            L -= 2
        return True
```
利用整除10** n删除n位以后数字（前序数字降位数），除10**n留余数保留n位及以后数字的数学特性

# 13.罗马数字转整数
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内
```python
def romanToInt(self, s: str) -> int:
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
    num = 0
    for i , n in enumerate(s):
        if i < len(s)-1 and dic[s[i]] < dic[s[i + 1]]: 
            num -= dic[s[i]]
        else:
            num += dic[s[i]]
    return num
```
1. 使用哈希表存储数据
2. 在判定的时候要先判定i< len(s) -1
3. 相同意义下可以将代码简化
```python
def romanToInt(self, s: str) -> int:
    dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    return sum (-dic[s[i]] if i < len(s)-1 and dic[s[i]]<dic[s[i+1]] else dic[s[i]] for i, n in enumerate(s))
```

# 14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""
## 字符串拼接
```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    result = ""
    i = j = 0
    while j < len(strs[0]):
        cur = strs[0][j]
        while i < len(strs):
            if j > len(strs[i]) - 1 or strs[i][j] != cur:
                return result
            i += 1
        i = 0
        result += cur #字符串的拼接
        j += 1
    return result
```
## zip打包
```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    res = ''
    for c in zip(*strs): 
        if len(set(c)) == 1:
            res = res + c[0]
        else:
            break
    return res
```
zip(*):解压，返回每个数据的第一个值
set():不会存储相同元素

# 20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'[ '，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
```python
def isValid(self, s: str) -> bool:
    dic = {')':'(',']':'[','}':'{'}
    stack = []
    for i in s:
        if stack and i in dic: #这一步的判定没弄懂
            if stack[-1] == dic[i]: 
                stack.pop()
            else: return False
        else:
            stack.append(i)
    return not stack
```