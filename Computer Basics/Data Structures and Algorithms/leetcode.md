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
利用整除10^n删除n位以后数字（前序数字降位数），除10^n留余数保留n位及以后数字的数学特性

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

# 149.环形链表
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null
```python
def detectCycle(self, head: ListNode) -> ListNode:
    list1 = []
    per = head
    while True:
        if not(per and per.next):
            return 
        elif per in list1:
            return per
        list1.append(per)
        per = per.next 
```
## 双向链表
```python
def detectCycle(self, head: ListNode) -> ListNode:
    fast , slow = head , head
    while True:
        if not (fast and fast.next): return
        fast , slow = fast.next.next , slow.next
        if fast == slow: break
    fast = head
    while fast != slow:
        fast , slow = fast.next , slow.next
    return fast
```
双向链表，设链表共有a+b个节点，其中链表头部到链表入口有a个节点（不计链表入口节点），链表环有b个节点；设两指针分别走了f，s步，则有：
fast走的步数是slow步数的2倍，即f = 2s；
fast 比 slow多走了n个环的长度，即 f = s + nb；
以上两式相减得：f = 2nb，s = nb，即fast和slow 指针分别走了2n，n个环长
slow再走a = 入口；head走到入口 = a

# 21. 合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next , l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1 , l2.next)
            return l2
```
递归

# 416.分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
## 递归法
```python
def canPartition(self, nums: List[int]) -> bool:
    s = sum(nums)
    if s % 2 == 1:
        return False
    target = s // 2
    n = len(nums)
    def dfs(current , i):
        if current == target:
            return True
        if i>=n or current>target:
            return False
        return t(current+nums[i] , i+1) or t(current,i+1)
    return dfs(0,0)
```
## 动态规划法
状态转移方程：创建一个二维数组，包含n行target+1列，其中dp[i][j]表示从数组的[0 ,i]下标范围内选取若干个正整数，是否存在一种选取方案使得被选取的正整数的和等于j。初始时，dp中的全部元素都是false
这种二维数组的判定性质如下：
![状态转移方程.png](https://assets.leetcode-cn.com/solution-static/416/6.png)
第0行true证明i=0时可能出现的总数
从第1行起，true的判定是正上方状态和左num[i]位正上方的或门
最后dp[n−1][target] 即为答案
```python
def canPartition(nums):
    s = sum(nums)
    n = len(nums)
    if s % 2 == 1 or n<2 or max(nums)>s // 2:
        return False
    target = s // 2
    dp = [[0]*(target+1) for i in range(n)]
    dp[0][nums[0]] = 1
    for i in range(n):
        dp[i][0] = 1
    for i in range(1,n):
        for j in range(1,target+1):
            if j>=nums[i]:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1] == 1
```
## 动态规划优化
```python
def canPartition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    n = len(nums)
    if total_sum%2==1:
        return False 
    half_sum = total_sum//2
    dp = [0]*(half_sum+1)
    dp[0]=1
    if nums[0]<=half_sum:
        dp[nums[0]]=1
    for i in range(1,n):
        for j in range(half_sum,-1,-1):
            if nums[i]<=j:
                dp[j] = dp[j] or dp[j-nums[i]]
    return dp[-1]
```

# 26.删除排序数组中的重复项
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在原地修改输入数组 并在使用O(1)额外空间的条件下完成。
## 双指针法
```python
def removeDuplicates(self, nums: List[int]) -> int:
    i , j = 0 , 1
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
    return i+1
```
## 单指针法
```python
def removeDuplicates(self, nums: List[int]) -> int:
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del nums[i]
            i -= 1
        i += 1
    return i+1
```
# 530. 二叉搜索树的最小绝对差
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。
关键在二叉搜索树的性质上，左子树<根<右子树，中序历遍可以得到一个升序数列
```python
diff , per = 999, 999
def getMinimumDifference(self, root: TreeNode) -> int:
    def Search(root):
        if root == None:
            return
        
        Search(root.left)
        self.diff = min(self.diff , abs(self.per - root.val))
        self.per = root.val
        Search(root.right)
    
    Search(root)
    return self.diff
```

# 27.移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
## 单指针
更快但内存消耗多
```python
def removeElement(self, nums: List[int], val: int) -> int:
    i = 0
    while i <len(nums):
        if nums[i] == val:
            del nums[i]
            i -= 1
        i += 1
    return i
```
## 双指针
内存消耗少，但速度更慢
```python
def removeElement(self, nums: List[int], val: int) -> int:
    i ,j= 0, 0
    while j <len(nums):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i
```