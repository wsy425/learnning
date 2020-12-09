# 1.两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标
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
        return t(current+nums[i] , i+1) or t(current , i+1)
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

# 24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
## python 同步赋值
```python
def swapPairs(self, head: ListNode) -> ListNode:
    h = temp = ListNode(next = head)
    if temp.next and temp.next.next:
        temp.next.next.next , temp.next.next , temp.next , temp = temp.next , temp.next.next.next , temp.next.next ,  temp.next
        #点2指向               点1指向          头指向       指针     点1              尾                   点2            点1
    return h.next
```
## 正常赋值
```python
def swapPairs(self, head: ListNode) -> ListNode:
    h = temp = ListNode(next = head)
    if temp.next and temp.next.next:
        node1 = temp.next
        node2 = temp.next.next

        temp.next = node2
        node1.next = node2.next
        node2.next = node1
        temp =node1
    return h.next
```
同步赋值所需的时间和内存都更小

# 28. 实现 strStr()
## python检索
```python
def strStr(self, haystack: str, needle: str) -> int:
    return haystack.index(needle) if needle in haystack else -1
```
## 滑动窗口比较
```python
def strStr(self, haystack: str, needle: str) -> int:
    L, n = len(needle), len(haystack)
    for start in range(n - L + 1):
        if haystack[start: start + L] == needle:
            return start
    return -1
```

# 1002.查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次
1. 哈希表，通过哈希表存储字符出现的次数
2. 对哈希表取交集得到字符出现的最低次数
3. 按最低次数输出字符
```python
def commonChars(self, A: List[str]) -> List[str]:
    res = None
    for a in A:
        c = Count(a)
        if res == None:
            res = c
        else:
            res &= c
    return list(res.elements())
```
1. Count()函数：一个数组内，遍历所有元素，将元素出现的次数记下来
2. &：求交集
3. .elements():

# 35. 搜索插入位置
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
## 顺序查找
```python
def searchInsert(self, nums: List[int], target: int) -> int:
    i = 0
    if target > max(nums):
        return len(nums)
    else:
        while i < len(nums):
            if target <= nums[i]
                return i
            i += 1
```
## 二分法
```python
def searchInsert(self, nums: List[int], target: int) -> int:
    left , right , ans = 0, len(nums)-1 , len(nums)
    while left <=right:
        middle = (right - left) // 2
        if target <= nums[middle]:
            ans = middle
            right = middle -1
        else:
            left = middle +1
    return ans
```
## python函数
```python
def searchInsert(self, nums: List[int], target: int) -> int:
    nums.append(target)
    nums.sort()
    return nums.index(target)
```
list.sort()函数直接对整个函数进行排序

# 116.填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL
## 指针法
```python
def connect(root):
    if not root:
        return None
    head = root
    while head:
        cur = head
        while cur and cur.left:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        head = head.left
    return root
```
## 层次历遍
```python
def connect(self, root: 'Node') -> 'Node':
    if not root:
        return root
    Q = collections.deque([root])
    while Q:
        for i in range(len(Q)):
            node = Q.popleft()
            if i < len(Q)-1:
                node.next = Q[0]
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
    return root
```
collections.deque:提供可以两边操作的列表

# 38.外观数列
给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
注意：整数序列中的每一项将表示为一个字符串。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
```python
def countAndSay(self, n: int) -> str:
    i ,j ,c , str1 , str2= 0, 0, 1, '1', ''
    while i < n-1:
        while j < len(str1):
            if j < len(str1)-1 and str1[j] == str1[j+1]:
                c += 1
            else:
                str2 = str2 + str(c) + str(str1[j])
                c = 1
            j += 1
        str1 = str2
        str2 = ''
        j = 0
        i += 1
    return str1
```

# 977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
## python自带函数法
```python
def sortedSquares(A):
    i = 0
    while i < len(A):
        A[i] = A[i] ** 2
        i += 1
    A.sort()
    return A
```
## 双指针法
```python
def sortedSquares(A):
    i, j ,cur = 0, len(A)-1, len(A)-1
    ans = [0] * len(A) 
    while i <= j:
        if abs(A[i]) > abs(A[j]):
            ans[cur] = A[i] ** 2
            i += 1
        else:
            ans[cur] = A[j] ** 2
            j -= 1
        cur -= 1
    return ans
```

# 53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
## 暴力法
```python
def maxSubArray(nums):
    temp = nums[0]
    max_ =temp
    for i in range(1,len(nums)):
        if temp > 0 :
            temp += nums[i]
        else:
            temp = nums[i]
        max_ = max(max_ , temp)
    return max_
```
## 递归
```python
def maxSubArray(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    else:
        max_left = self.maxSubArray(nums[0:len(nums) // 2])
        max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])
    max_l = nums[len(nums) // 2 - 1]
    tmp = 0
    for i in range(len(nums) // 2 - 1, -1, -1):
        tmp += nums[i]
        max_l = max(tmp, max_l)
    max_r = nums[len(nums) // 2]
    tmp = 0
    for i in range(len(nums) // 2, len(nums)):
        tmp += nums[i]
        max_r = max(tmp, max_r)
    return max(max_right,max_left,max_l+max_r)
```
## 动态规划
```python
def maxSubArray(nums):
    for i in range(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i] , nums[i])
    return mas(nums)
```

# N皇后 II
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给定一个整数 n，返回 n 皇后不同的解决方案的数量。
## 集合判断递归
```python
def totalNQueens(n):
    def backtrack(row: int) -> int:
        if row == n:
            return 1
        else:
            count = 0
            for i in range(n):
                if i in columns or row - i in diagonal1 or row + i in diagonal2:
                    continue
                columns.add(i)
                diagonal1.add(row - i)
                diagonal2.add(row + i)
                count += backtrack(row + 1)
                columns.remove(i)
                diagonal1.remove(row - i)
                diagonal2.remove(row + i)
            return count
                    
    columns = set()
    diagonal1 = set()
    diagonal2 = set()
    return backtrack(0)
```
## 位运算判断递归
```python
def totalNQueens(n):
    res=0
    def backtrack(i,col,pos,neg):
        nonlocal res
        if i==n:
            res+=1
            return 
        #其中1表示可以被选
        pre=((1<<n)-1)&(~(col | pos | neg))
          
        while pre:
            cur=pre & (-pre)
            backtrack(i+1,col | cur , (pos | cur)>>1,(neg | cur)<<1)
            pre &=pre-1
            
    backtrack(0,0,0,0)
    return res
```
| 位或运算
& 位与运算
x & (−x) 可以获得 x 的二进制表示中的最低位的 1 的位置；
x&(x-1)可以将 x 的二进制表示中的最低位的 1 置成 0。

# 58. 最后一个单词的长度
## split函数
```python
def lengthOfLastWord(s):
    s = s.rstrip()
    s = s[::-1]
    a = s.split(' ',1)
    p = a[0]
    return len(a[0])
```
要注意空字符串和空格在最后出现的情况
.rstrip()删除字符串末尾空格
.split(' ',1)以逗号前的字符从头分割字符串逗号后次数
## 反向历遍
```python
def lengthOfLastWord(s):
    i = len(s) - 1
    j = 0
    flag = False
    while i >= 0:
        if s[i] != ' ':
            flag = True
            j += 1
            i -= 1
            continue 
        elif flag:
            break
        i -= 1                     
    return j
```
要判断两次空格，通过flag指标与continue、break的配合实现算法

# 19.删除链表的倒数第N个节点
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    r = ListNode(0)
    r.next = head
    slownode = r
    fastnode = slownode
    for i in range(n):
        fastnode = fastnode.next
    while fastnode != None and fastnode.next!=None:
        slownode = slownode.next
        fastnode = fastnode.next
    slownode.next = slownode.next.next
    return r.next
```
1. 双指针：使快指针比慢指针快n，快指针触底时表示慢指针后一项删除
2. 创建空头链表，在空头链表上创建快慢指针，防止原链表第一个元素时删除出错
3. 考虑删除原链表第一个元素时，快指针已经超出链表范围，要对循环做更多限制

# 66.加一
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
```python
def plusOne(digits):
    j = 0
    for i in range(1,len(digits)+1):
        if digits[-i] != 9:
            digits[-i] += 1 
            break
        digits[-i] = 0
        j += 1
    if j == len(digits):
        digits.insert(0, 1)
    return digits
```

# 844. 比较含退格的字符串
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
注意：如果对空文本输入退格字符，文本继续为空。
```python
def backspaceCompare(S, T):
    i , j = len(S)-1 , len(T)-1
    count_i , count_j = 0 , 0
    while i>=0 or j>=0:
        if S[i] == '#'and i >=0:
            count_i += 1
            i -= 1
            continue
        if T[j] == '#' and j >=0:
            count_j += 1
            j -= 1
            continue
        elif count_i >0:
            i -= 1
            count_i -= 1
            continue
        elif count_j >0:
            j -= 1
            count_j -= 1
            continue
        elif  i<0 or j <0 or S[i] != T[j]:
            return False
        else:
            i -= 1
            j -= 1
    return i <0 and j <0
```
1. 双指针遍历两个字符串
2. 倒序遍历删除#前的字符
3. 不存在#删#的事件，所以计数不能直接减
4. 会出现字符串里只剩#的问题，且要与字符串可倒序检索一起考虑

# 67. 二进制求和
## python函数
```python
def addBinary(self, a: str, b: str) -> str:
    a = int(a,2)
    b = int(b,2)
    c = a + b
    return bin(c)[2:]
```
1. int():将括号里内容转换为一个整数
2. int(x,2/8/16):x为字符串，将2/8/16进制的字符串转化为10进制整数
3. bin(x):返回10进制x的2进制表达字符串，且前面带进制标识
4. python进制转换
![python进制转换.png](https://img-blog.csdn.net/20160720140605151)
## 补位后位运算
```python
def addBinary(a,b):
    a = a.zfill(max(len(a),len(b)))
    b = b.zfill(max(len(a) ,len(b)))
    count = 0
    c = ''
    for i in range(len(a)-1,-1,-1):
        if a[i] == '0' and b[i] == '0':
            c = str(count) + c
            count = 0
        elif a[i] == '0' or b[i] == '0':
            c = str(1^count) + c
            count = 1 & count
        else:
            c = c + str(count)
            count = 1
    if count == 1:
        c = '1' + c
    return c
```
1. .zfill (width)将字符串在左边补0达到width长度
2. 影响二进制计算的只有进的位和两个数该位本身，三者只可能是0、1，考虑位运算

# 143.重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
## 将链表存储到列表中
列表具有索引的功能，借助这一功能达到链表的索引
```python
def reorderList(self, head: ListNode) -> None:
    if not head:
        return
    node = head
    head_list = []
    while node:
        head_list.append(node)
        node = node.next
    i , j = 0 , len(head_list) - 1
    while i < j:
        head_list[i].next = head_list[j]
        head_list[j].next = head_list[i+1]
        i += 1
        j -= 1
    head_list[i].next = None
```
## 快慢指针找中点，右侧链表翻转后合并
```python
def reorderList(self, head: ListNode) -> None:
    if not head:
        return
    slow = fast = head
    left = head
    prv = None
    # 快慢指针找中点
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    # 分割成两个链表
    right = slow.next
    slow.next = None
    # 右侧链表翻转
    while right:
        right.next , right , prv = prv , right.next , right
    # 两链表合并
    while prv and left:
        left.next , prv.next , left , prv = prv , left.next , left.next , prv.next
```
1. 快慢指针找中点：边界条件中右侧可以从中位之后开始
2. 一定要分割成两个链表，否则成环
3. 链表翻转类似于栈

# 69. x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
```python
def mySqrt(self, x: int) -> int:
    if x <= 1:
        return x
    a = x
    while  a > x/a:
        a = (a + x/a) // 2
    return int(a)
```
1. 牛顿迭代法
2. 保持每次a都为整数，会使得收敛速度变快

# 925. 长按键入
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。
```python
def isLongPressedName(name,typed):
    i ,j = 0 , 0
    while i < len(name) and j <len(typed):
        if name[i] != typed[j] and j > 0:
            if typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        elif name[i] != typed[j]:
            return False
        else:
            i += 1
            j += 1
    return i = len(name) and len(set(typed[j-1:])) == 1
```
1. 双指针
2. 边界条件考虑

# 70. 爬楼梯
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
```python
def climbStairs(n)
    a = 0
    b = 1
    for i in range(n):
        a , b = b , b+a
    return b
```
就是求斐波那契数列

# 763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
## python函数
```python
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
```
## 哈希表
```python
def partitionLabels(S):
    char_pos ={}
    for i in range(len(S)):
        char_pos[S[i]] = i
    i , j = 0 , 0
    list_1 = []
    while i < len(S):
        per = S[i]
        z = 0
        while z < len(per):
            if per[z] in S[i+1:]:
                i = max(char_pos[per[z]] , i)
                per = ''.join(set(S[j:i]))
            else:
                z += 1
        i += 1
        list_1.append(i-j)
        j = i
    return list_1
```

# 83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
```python
def deleteDuplicates(head: ListNode):
    slow = head
    fast = head
    while fast:
        if slow.val != fast.val:
            slow = slow.next
        fast = fast.next
        slow.next = fast
    return head
```

# 234. 回文链表
请判断一个链表是否为回文链表
## 转换成列表
```python
def isPalindrome(head):
    head_list = []
    node = head
    if  not head:
        return True
    while node:
        head_list.append(node.val)
        node = node.next
    i , j = 0, len(head_list) - 1
    while i<j:
        if head_list[i] != head_list[j]:
            return False
        i += 1
        j -= 1
    return True
```
## 快慢指针找中点同时对左边链表反转
```python
def isPalindrome(head):
    slow = head
    fast = head
    pre = None
    count = 0
    if not head or not fast.next:
        return True
    while fast and fast.next:
        fast = fast.next.next
        temp = slow.next
        slow.next = pre
        pre = slow
        slow = temp
    if fast:
        slow =slow.next
    while pre:
        if pre.val != slow.val:
            return False
        pre = pre.next
        slow = slow.next
    return True
```

# 88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组
## python函数
```python
def merge(nums1,m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
```
## 倒序输入
```python
def merge(nums1, m, nums2, n):
    i = m+n-1
    a , b = m-1 , n-1 
    while i>=0:
        if a>=0 and b>=0 and nums1[a] > nums2[b]:
            nums1[i] = nums1[a]
            a -= 1
        elif a>=0 and b>=0:
            nums1[i] = nums2[b]
            b -= 1
        elif b>=0:
            nums1[i] = nums2[b]
            b -= 1
        i -= 1
```

# 1024. 视频拼接
你将会获得一系列视频片段，这些片段来自于一项持续时长为 T 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。
视频片段 clips[i] 都用区间进行表示：开始于 clips[i][0] 并于 clips[i][1] 结束。我们甚至可以对这些片段自由地再剪辑，例如片段 [0, 7] 可以剪切成 [0, 1] + [1, 3] + [3, 7] 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（[0, T]）。返回所需片段的最小数目，如果无法完成该任务，则返回 -1 。
## 贪心算法
```python
def videoStitching(clips, T):
    i, j, lastend , maxlength = 0 , 0 , 0 , 0
    count = 0
    clips = sorted(clips,key = lambda x:x[0])
    while i<len(clips):
        if lastend >= T:
            break
        while j<len(clips) and clips[j][0] <=lastend:
            maxlength = max(maxlength , clips[j][1])
            j += 1
        if i == j:
            return -1
        lastend = maxlength
        i = j
        count += 1
    return -1 if lastend<T else count
```
1. sorted(key = lambda x:x[ a])按照第a个数排列顺序
## 动态规划
```python
def videoStitching(clips, T):
    dp = [0] + [float("inf")] * T
    for i in range(1, T + 1):
        for aj, bj in clips:
            if aj < i <= bj:
                dp[i] = min(dp[i], dp[aj] + 1)
    return -1 if dp[T] == float("inf") else dp[T]
```
1. 用的dp[ i]存储到i需要的最少视频段

# 相同的树
给定两个二叉树，编写一个函数来检验它们是否相同。
如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
## 深度优先算法
```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
```
1. 递归思想
## 广度优先算法
```python
def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    if p is None and q is None: return True
    elif p is None and q is not None: return False
    elif p is not None and q is None: return False
    elif p.val != q.val: return False
    stack1, stack2 = [p], [q]
    while stack1:
        this_lv1, this_lv2= [], []
        for idx in range(len(stack1)):
            n1,n2 = stack1[idx], stack2[idx]
            if n1 is None and n2 is not None: return False
            elif n1 is not None and n2 is None: return False
            elif n1 is not None and n2 is not None and n1.val != n2.val: return False
            if n1 is not None: this_lv1.extend([n1.left, n1.right])
            if n2 is not None: this_lv2.extend([n2.left, n2.right])
        stack1, stack2 = this_lv1, this_lv2        
    return True
```
1. 不使用栈pop可以保证把整个列表遍历完

# 845. 数组中的最长山脉
我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”：
B.length >= 3
存在 0 < i < B.length - 1 使得 B[ 0] < B[ 1] < ... B[ i-1] < B[ i] > B[ i+1] > ... > B[B.length - 1]
（注意：B 可以是 A 的任意子数组，包括整个数组 A。）
给出一个整数数组 A，返回最长 “山脉” 的长度。
如果不含有 “山脉” 则返回 0
```python
def longestMountain(A):
    i , right ,left ,count=0,0,0,0
    while i <len(A) -1:
        if A[i] < A[i+1]:
            if right != 0:
                left = 0
                right = 0
            left += 1
        elif left != 0 and A[i] > A[i+1]:
            right += 1
            count = max(count,left+right+1)
        elif A[i] == A[i+1]:
            left = 0
        i += 1
    return count
```

# 101. 对称二叉树
给定一个二叉树，检查它是否是镜像对称的。
```python
def isSymmetric(self, root: TreeNode) -> bool:
    if not root:
        return True
    def is_mirror(l,r):
        if not(l or r):
            return True
        if not(l and r):
            return False
        if l.val != r.val:
            return False
        return is_mirror(l.left,r.right) and is_mirror(l.right,r.left)
    return is_mirror(root.left,root.right)
```
1. 递归

# 1365. 有多少小于当前数字的数字
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案
## python函数
```python
def smallerNumbersThanCurrent(nums):
    num1 = sorted(nums)
    count = []
    for num in nums:
        count.append(num1.index(num))
    return count
```
## 类哈希表
```python
def smallerNumbersThanCurrent(nums):
    place = [0]* (max(nums)+1)
    out = []
    for num in nums:
        place[num] += 1
    for i in range(1,len(place)):
        place[i] += place[i-1]
        i += 1
    for num in nums:
        if num ==0:
            out.append(0)
        else:
            out.append(place[num-1])
    return out
```
1. 考虑0的情况
2. 考虑同一个数反复出现的情况

# 104.  
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
## 递归
```python
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
```
## 广度优先算法
```python
def maxDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    q = deque([root])
    level = 0
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level
```

# 144. 二叉树的前序遍历
给定一个二叉树，返回它的前序遍历。
## 递归
```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    def preoder(root):
        if not root:
            return res
        res.append(root.val)
        preoder(root.left)
        preoder(root.right)
    return res 
```
## 迭代
```python
def preorderTraversal(self, root: TreeNode) -> List[int]:
    res = []
    stack = []
    if not root:
        return res
    node = root
    while node or stack:
        while node:
            res.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return res
```

# 107. 二叉树的层次遍历 II
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
```python
def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
    q = deque([root])
    p = []
    res = []
    if not root:
        return res
    while q:
        n = len(q)
        for i in range(n):
            node = q.popleft()
            p.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.insert(0,p)
        p = []
    return res
```

# 1207. 独一无二的出现次数
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
```python
def uniqueOccurrences(arr):
    dic = {}
    s = []
    for num in arr:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
    for i in dic:
        s.append(dic[i])
    return len(s) == len((set(s)))
```

# 108. 将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
```python
def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
    def BST(left,right):
        if left>right:
            return None
        mid = (left+right) // 2
        root = TreeNode(nums[mid])
        root.left = BST(left,mid-1)
        root.right = BST(mid+1,right)
        return root
    return BST(0,len(nums)-1)
```

# 129. 求根到叶子节点数字之和
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
例如，从根到叶子节点路径 1->2->3 代表数字 123。
计算从根到叶子节点生成的所有数字之和。
说明: 叶子节点是指没有子节点的节点。
## 广度优先算法
```python
def sumNumbers(self, root: TreeNode) -> int:
    if not root:
        return 0
    total = 0
    nodeQueue = collections.deque([root])
    numQueue = collections.deque([root.val])
    while nodeQueue:
        node = nodeQueue.popleft()
        num = numQueue.popleft()
        left, right = node.left, node.right
        if not left and not right:
            total += num
        else:
            if left:
                nodeQueue.append(left)
                numQueue.append(num * 10 + left.val)
            if right:
                nodeQueue.append(right)
                numQueue.append(num * 10 + right.val)
    return total
```
## 深度优先算法
```python
def sumNumbers(self, root: TreeNode) -> int:
    def dsf(root,pretotal):
        if not root:
            return 0
        total = pretotal * 10 + root.val
        if not root.left and not root.right:
            return total
        else:
            return dsf(root.left,total) + dsf(root.right,total)
    return dsf(root,0)
```

# 463. 岛屿的周长
给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。
```python
def islandPerimeter(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j]==0:
                    count += 1
                if  i == len(grid)-1 or grid[i+1][j]==0:
                    count += 1
                if j == 0 or grid[i][j-1]==0:
                    count += 1
                if j == len(grid[0])-1 or grid[i][j+1]==0:
                    count += 1
    return count
```
1. 周长加不加通过周围4个格子判定
2. 判断语句要把能通过的放在前面

# 381. O(1) 时间插入、删除和获取随机元素 - 允许重复
设计一个支持在平均 时间复杂度 O(1) 下， 执行以下操作的数据结构。
注意: 允许出现重复元素。
insert(val)：向集合中插入元素 val。
remove(val)：当 val 存在时，从集合中移除一个 val。
getRandom：从现有集合中随机获取一个元素。每个元素被返回的概率应该与其在集合中的数量呈线性相关。
```python
import random
class RandomizedCollection:
    def __init__(self):
       '''类存储定义'''
        self.nums = []
        self.num_loc = defaultdict(set)
        self._len = 0

    def insert(self, val: int) -> bool:
        """插入元素"""
        self.nums.append(val)
        self.num_loc[val].add(self._len)
        self._len += 1
        return len(self.num_loc[val]) == 1

    def remove(self, val: int) -> bool:
        """移除元素"""
        if not self.num_loc[val]:
            return False
        val_loc = self.num_loc[val].pop()
        self.nums[val_loc] = self.nums[-1]
        last_val = self.nums.pop()
        self.num_loc[last_val].add(val_loc)
        self.num_loc[last_val].discard(self._len-1)
        self._len -= 1
        return True

    def getRandom(self) -> int:
        """随机获取元素"""
        return random.choice(self.nums)
```
1. 集合set的内置函数add，discard
2. 列表与代替哈希表的字典混合运用
3. O(1)时间删除元素的关键在于用最后一个元素覆盖该元素，然后把最后一个元素删除

# 140. 单词拆分 II
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
说明：
分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词
```python
def wordBreak(s,wordDict):
    res = []
    memo = [1] * (len(s)+1)
    wordDict = set(wordDict)

    def dfs(wordDict,temp,pos):
        num = len(res)                  # 回溯前先记下答案中有多少个元素
        if pos == len(s):
            res.append(" ".join(temp))
            return
        for i in range(pos,len(s)+1):
            if memo[i] and s[pos:i] in wordDict: # 添加备忘录的判断条件
                temp.append(s[pos:i])
                dfs(wordDict,temp,i)
                temp.pop()
        # 答案中的元素没有增加，说明s[pos:]不能分割，修改备忘录        
        memo[pos] = 1 if len(res) > num else 0 
            
    dfs(wordDict,[],0)
    return res
```
1. 回溯算法：通过`if pos == len(s):`判定循环结束，并且return回到前一个循环，将最后一个值弹出，并添加弹出记忆
2. `.join()`函数返回通过前面指定字符连接括号中元素后生成的新字符串

# 110. 平衡二叉树
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
## 自顶向下递归
```python
def isBalanced(self, root: TreeNode) -> bool:
    def maxDepth(root):
        if not root:
            return 0
        else:
            return max(maxDepth(root.right),maxDepth(root.left))+1
    if not root:
        return True
    elif abs(maxDepth(root.left)-maxDepth(root.right))>1:
        return False
    else:
        return self.isBalanced(root.left) and self.isBalanced(root.right)
```
1. 深度优先算法
## 自底向上递归
```python
def isBalanced(self, root: TreeNode) -> bool:
        return self.recur(root) != -1

def recur(self, root):
    if not root:
        return 0
    left = self.recur(root.left)
    if left == -1:
        return -1
    right = self.recur(root.right)
    if right == -1:
        return -1
    if abs(left - right) < 2:
        return max(left, right) + 1 
    else:
        return -1
```
1. 提前剪枝
2. 不平衡则返回-1作为子树高度
3. 通过一次高度计算历遍解决问题

# 349. 两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。
## python集合函数
```python
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    set3 = set1.intersection(set2)
    num = []
    for  n in set3:
        num.append(n)
    return num
```
```python
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
```
1. `.intersection()`函数，返回前集合与后集合之间的交集
2. &直接求集合交集
## 哈希表
```python
def intersection(nums1, nums2):
    dic = {}
    num = []
    for i in range(len(nums1)):
        dic[nums1[i]] = 1
    for n in nums2:
        if dic.get(n) == 1:
            num.append(n)
            dic[n] = 0
    return num
```
1. `dict.get(key, default=None)`避免寻找字典中不存在的数字报错
## 排序双指针
```python
def intersection(nums1, nums2):
    nums1.sort()
    nums2.sort()
    num = []
    i,j = 0,0
    while i <len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            if not num or nums1[i] != num[-1]:
                num.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return num 
```

# 111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。
## 深度优先算法
```python
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    mindepth = 10**9
    if root.left:
        mindepth = min(self.minDepth(root.left),mindepth) 
    if root.right:
        mindepth = min(self.minDepth(root.right),mindepth) 
    return mindepth +1
```
1. 不能直接在mindepth上+1，这样会导致每次判断都+1，但不是每次判断都有效
## 广度优先算法
```python
def minDepth(self, root: TreeNode) -> int:
    if not root:
        return 0
    q = collections.deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        if not node.left and not node.right:
            return depth
        if node.left:
            q.append((node.left, depth + 1))
        if node.right:
            q.append((node.right, depth + 1))
    return 0
```
1. 在双向列表中一个元素传入两个量来表示深度

# 941. 有效的山脉数组
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
## 线性扫描
```python
def validMountainArray(A):
    sign = 0
    i = 0
    for i in range(len(A)-1):
        if A[i]<A[i+1] and sign == 0:
            continue
        elif A[i]>A[i+1] and sign == 0  and i != 0:
            sign = 1
        elif A[i]>A[i+1] and sign == 1:
            continue
        else:
            return False
    return sign == 1
```
## 双指针
```python
def validMountainArray(A):
    i,j = 0,len(A)-1
    while i+1<len(A) and A[i]<A[i+1]:
        i += 1
    while j-1>0 and A[j]<A[j-1]:
        j -= 1
    return i==j and i>0 and j<len(A)-1
```
1. 限制条件要考虑下一项的存在
2. 返回正确的条件要考虑只有一边的情况

# 112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
说明: 叶子节点是指没有子节点的节点。
## 深度优先算法+递归
```python
def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.right and not root.left:
        return root.val == sum
    return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
```
1. 要考虑到不能截取中间路径

# 57. 插入区间
给出一个无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    sign = 0
    i = 0
    if not intervals:
        return [newInterval]
    while i < len(intervals):
        if intervals[i][1] < newInterval[0] and i != len(intervals)-1:
            i += 1
            continue
        elif intervals[i][1] < newInterval[0]:
            intervals.append(newInterval)
        elif intervals[i][1] == newInterval[0]:
            intervals[i][1] = newInterval[1]
            sign = 1
        elif intervals[i][0] >newInterval[1] and sign == 0:
            intervals.insert(i,newInterval)
            sign = 1
            i += 1
        elif intervals[i][0] >newInterval[1] and sign == 1:
            i += 1
            continue
        elif intervals[i][0] > newInterval[0] and sign == 0:
            intervals[i][0] = newInterval[0]
            intervals[i][1] = max(newInterval[1] , intervals[i][1])
            sign = 1
        elif intervals[i][0] > newInterval[0] and sign == 1:
            intervals[i-1][1] = max(newInterval[1],intervals[i][1])
            del intervals[i]
            i -= 1
        elif intervals[i][0] <= newInterval[0]:
            intervals[i][1] = max(newInterval[1] , intervals[i][1])
                sign = 1
            i += 1
    return intervals
```
1. 通过插入区间和两个原区间的关系把边界条件考虑清楚

# 127. 单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
## 单向广度优先算法
```python
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    general_dic = {}
    q = collections.deque([(beginWord,1)])
    mark_dic = {beginWord:True}
    for w in wordList:
        for i in range(len(beginWord)):
            if w[:i]+"*"+w[i+1:] in general_dic:
                general_dic[w[:i]+"*"+w[i+1:]].append(w)
            else:
                general_dic[w[:i]+"*"+w[i+1:]] = [w]
    while q:
        node ,depth= q.popleft()
        for i in range(len(beginWord)):
            if node[:i]+"*"+node[i+1:] in general_dic:
                for w in general_dic[node[:i]+"*"+node[i+1:]]:
                    if w == endWord:
                        return depth+1
                    if w not in mark_dic:
                        mark_dic[w]=True
                        q.append((w,depth+1))
    return 0
```
1. 获得单词的关联单词方法
2. 标记已经走过的单词
3. 存在一个关联单词对应多个值，字典中套用列表
## 双向广度优先算法
```python
from collections import deque
def ladderLength(beginWord, endWord, wordList):
    general_dic = {}
    q = deque([beginWord])
    p = deque([endWord])
    mark_dic = {beginWord:True,endWord:True}
    step = 2
    length = len(q)
    if endWord not in wordList:
        return 0
    for w in wordList:
        for i in range(len(beginWord)):
            if w[:i]+"*"+w[i+1:] in general_dic:
                general_dic[w[:i]+"*"+w[i+1:]].append(w)
            else:
                general_dic[w[:i]+"*"+w[i+1:]] = [w]
    while q and p:
        length = len(q)
        step += 1
        for j in range(length):
            node = q.popleft()
            for i in range(len(beginWord)):
                if node[:i]+"*"+node[i+1:] in general_dic:
                    for w in general_dic[node[:i]+"*"+node[i+1:]]:
                        if w in p:
                            return step
                        if w not in mark_dic:
                            mark_dic[w]=True
                            q.append(w)
        if len(q) > len(p):
            q, p = p, q
    return 0
```
1. 从头和尾一起搜索，一直搜索少的那一个
2. 判断步数增加的方法要改变，方便判断两者相遇

# 118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。
```python
def generate(numRows):
    total_list = []
    p = [1]
    j ,i= 0,0
    while j < numRows:
        total_list.append(p)
        size = len(p)
        p = []
        i = 0
        while i <= size:
            if i == 0:
                p.append(1)
            elif i == size:
                p.append(1)
            else:
                p.append(total_list[j][i-1]+total_list[j][i])
            i += 1
        j += 1
    return total_list
```
1. 广度优先算法思维
2. 动态规划

# 1356. 根据数字二进制下 1 的数目排序
给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。
## 哈希表余数计数
```python
def sortByBits(arr):
    dic = {}
    count ,count_list= 0,[]
    arr1 = []
    arr.sort()
    for num in arr:
        n = num
        count = 0
        while n >0:
            count += n%2
            n = n // 2
        if count not in dic:
            dic[count] = [num]
            count_list.append(count)
        else:
            dic[count].append(num)
    count_list.sort()
    for count in count_list:
        if not arr1:
            arr1 = dic[count]
        else:
            arr1.extend(dic[count])
    return arr1
```
1. 为了控制最后输出按照顺序，需按序查找key，以及key对应的value按序排列
## 哈希表字符串计数
```python
def sortByBits(arr):
    dic = {}
    arr1 = []
    arr.sort()
    count_list = []
    for num in arr:
        count = 0
        for s in str(bin(num)):
            if s == '1':
                count += 1
        if count not in dic:
            dic[count] = [num]
            count_list.append(count)
        else:
            dic[count].append(num)
    count_list.sort()
    for count in count_list:
        if not arr1:
            arr1 = dic[count]
        else:
            arr1.append(dic[count])
    return arr1
```

# 119. 杨辉三角 II
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
## 动态规划
```python
def getRow(rowIndex):
    q = [1]
    i,j,size = 0,0,0
    while i < rowIndex:
        size += 1
        p = q
        q = []
        j = 0
        while j <=size:
            if j == 0:
                q.append(1)
            elif j == size:
                q.append(1)
            else:
                q.append(p[j-1]+p[j])
            j += 1
        i += 1
    return q
```

# 327. 区间和的个数
给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
## 暴力法
```python
def countRangeSum(nums, lower, upper):
    count = 0
    for i in range(len(nums)):
        total = 0
        for j in range(i,len(nums)):
            total += nums[j]
            if lower <= total <= upper:
                count += 1
    return count
```
## 区间和内求个数
```python
import bisect
def countRangeSum(nums, lower, upper):
    res = cur = 0
    s = [0]
    for v in nums:
        cur += v
        res += bisect.bisect_right(s, cur-lower) - bisect.bisect_left(s, cur-upper)
        bisect.insort_right(s, cur)
    return res
```
1. 对于指定右端点j，满足要求的左端点符合$ pre_sum[j] - upper <= pre_sum[i] <= pre_sum[j] - lower $
2. 对所有到pre_sum排序，获取上式的端点所以就能获得指定右端点j的满足条件的区间和个数
3. bisect板块，bisect.bisect返回如果插入的索引，bisect.insort添加元素，都在保证顺去的情况下

# 121. 买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。
## 双指针
```python
def maxProfit(prices):
    i,j,profit = 0,1,0
    while j < len(prices):
        if prices[j] > prices[i]:
            profit = max(profit,prices[j]-prices[i])
            j += 1
        else:
            i += 1
            j = i+1
    return profit
```
## 一次遍历
```python
def maxProfit(prices):
    inf = int(1e9)
    minprice = inf
    profit = 0
    for price in prices:
        profit = max(price - minprice, profit)
        minprice = min(price, minprice)
    return profit
```

# 122. 买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
## 双指针
```python
def maxProfit(prices):
    inf = int(1e9)
    minprice = inf
    profit ,j = 0,0
    sign = 0
    while j<len(prices)-1:
        if prices[j]<prices[j+1] :
            minprice = min(prices[j], minprice)
            sign = 1
        elif prices[j]>prices[j+1] and sign == 1:
            profit += prices[j] - minprice
            minprice = inf
            sign = 0
        j += 1
    if sign == 1:
        profit = profit + prices[-1] - minprice
    return profit
```
1. 使用标志指针
2. 一次确定山峰前的最小值
## 一次遍历
```python
def maxProfit(prices):
    profit = 0
    for i in range(1, len(prices)):
        tmp = prices[i] - prices[i - 1]
        if tmp > 0: profit += tmp
    return profit
```
1. 每次前一个小于现在就把差值加入，否则跳过

# 125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
## 记忆+双指针
```python
def isPalindrome(s):
    i,j = 0,len(s)-1
    me = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    while i < j:
        if s[i].capitalize() not in me:
            i += 1
        elif s[j].capitalize() not in me:
            j -= 1
        elif s[i].capitalize() != s[j].capitalize():
            return False
        else:
            i += 1
            j -= 1
    return True
```
## 优化
```python
def isPalindrome(s):
    s = s.lower()
    i,j = 0,len(s)-1
    me = 'abcdefghijklmnopqrstuvwxyz0123456789'
    while i < j:
        if s[i] not in me:
            i += 1
        elif s[j] not in me:
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    return True
```
1. 通过.low()函数将所有字母变为小写

# 973. 最接近原点的 K 个点
我们有一个由平面上的点组成的列表 points。需要从中找出 K 个距离原点 (0, 0) 最近的点。
你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。
## 新列表排序
```python
def kClosest(points, K):
    listlen = []
    out = []
    for i in range(len(points)):
        listlen.append([points[i][0]**2 + points[i][1]**2,i])
    listlen.sort(key = lambda x:x[0])
    for lenth in listlen[:K]:
        out.append(points[lenth[1]])
    return out
```
1. .sort()中key参数的赋值方式
## 排序优化
```python
def kClosest(points, K):
    points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
    return points[:K]
```
## 快速排序（不推荐）
```python
def kClosest(points, K):
    out = []
    lenlist = []
    j = 0
    for i in range(len(points)):
        if i<K:
            out.append(points[i])
            lenlist.append(points[i][0]**2 + points[i][1]**2)
        elif points[i][0]**2+points[i][1]**2 < max(lenlist):
            j = lenlist.index(max(lenlist))
            out[j] = points[i]
            lenlist[j] = points[i][0]**2+points[i][1]**2
    return out
```
## 堆排序
```python
from heapq import heappush, heappop 
def kClosest(points, K):
    queue = []
    distance = lambda x: points[x][0]**2 + points[x][1]**2
    length = len(points)
    for i in range(length):
        heappush(queue, (distance(i), points[i]))
    res = []
    for i in range(K):
        res.append(heappop(queue)[1])
    return res
```

# 136. 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
## 暴力判定
```python
def singleNumber(nums):
    for i in range(len(nums)-1):
        if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
            return nums[i]
    return nums[-1]
```
## 删除+暴力判定
```python
def singleNumber(nums):
    i = 0
    while i <len(nums)-1:
        a = nums[i]
        if a in nums[i+1:]:
            nums.remove(a)
            nums.remove(a)
            i -= 1
        else:
            return a
        i += 1
    return nums[-1]
```
## 删除+哈希表
```python
def singleNumber(nums):
    dic = {}
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            del dic[n]
    for key in dic.keys():
        return key
```

# 31. 下一个排列
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
# 反向遍历
```python
def nextPermutation(nums):
    for i in range(len(nums)-1,0,-1):
        if nums[i] > nums[i-1]:
            nums[i:] = sorted(nums[i:])
            for j in range(i,len(nums)):
                if nums[j] > nums[i-1]:
                    nums[j] , nums[i-1] = nums[i-1] , nums[j]
                    break
            return
    nums.sort()       
```

# 141. 环形链表
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
## 快慢指针
```python
def hasCycle(self, head: ListNode):
    i,j = head,head
    if not head:
        return False
    while j.next and j.next.next:
        i = i.next
        j = j.next.next
        if i.val == j.val:
            return True
    return False
```

# 514. 自由之路
电子游戏“辐射4”中，任务“通向自由”要求玩家到达名为“Freedom Trail Ring”的金属表盘，并使用表盘拼写特定关键词才能开门。
给定一个字符串 ring，表示刻在外环上的编码；给定另一个字符串 key，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的最少步数。
最初，ring 的第一个字符与12:00方向对齐。您需要顺时针或逆时针旋转 ring 以使 key 的一个字符在 12:00 方向对齐，然后按下中心按钮，以此逐个拼写完 key 中的所有字符。
旋转 ring 拼出 key 字符 key[ i] 的阶段中：
您可以将 ring 顺时针或逆时针旋转一个位置，计为1步。旋转的最终目的是将字符串 ring 的一个字符与 12:00 方向对齐，并且这个字符必须等于字符 key[ i] 。
如果字符 key[ i] 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 1 步。按完之后，您可以开始拼写 key 的下一个字符（下一阶段）, 直至完成所有拼写。
1. 不能使用贪心算法，存在非局部最优解的全局最优解
## 动态规划
```python
def findRotateSteps(ring, key):
        Choices = d()  # 把每个key对应的可选的ring的字母的index做成字典。
        for k in key:
            if k in Choices:
                continue
            else:
                Choices[k] = []
                for ri, r in enumerate(ring):
                    if r == k:
                        Choices[k].append(ri)
        counter = [{0 : 0}]
        Path = d()
        for keyi in range(len(key)): # 一共len(key)个格子。
            counter.append({})
            for choice in Choices[key[keyi]]:  # choice是个index，是表示对于在key上第keyi个字母来说，ring里有哪几个位置的字母可以选择。
                temp = []
                for start in counter[keyi].keys():  # start表示上一个格子里，有几种情况可以到达当前的choice。
                    previous_distance = counter[keyi][start]
                    s = str(start) + "-" + str(choice)
                    if s not in Path:
                        d1 = abs(choice - start)
                        d2 = abs(len(ring) - d1)
                        newc = min(d1, d2)
                        Path[s] = newc
                    temp.append(previous_distance + Path[s])
                counter[keyi + 1][choice] = min(temp) + 1  # 只需要保留最小值  再加1表示按下按钮。
        # print(Choices)
        final = min(counter[-1].values())
        return final
```

# 1122. 数组的相对排序
给你两个数组，arr1 和 arr2，
arr2 中的元素各不相同
arr2 中的每个元素都出现在 arr1 中
对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
## 暴力法
```python
def relativeSortArray(arr1, arr2):
    arr = []
    for i in range(len(arr2)):
        while arr2[i] in arr1:
            arr.append(arr2[i])
            arr1.remove(arr2[i])
    arr1.sort()
    return arr + arr1
```
## 计数排序
```python
def relativeSortArray(arr1, arr2):
    arr = []
    frequency = [0] * (max(arr1) + 1)
    for x in arr1:
        frequency[x] += 1
    for x in arr2:
        arr.extend([x] * frequency[x])
        frequency[x] = 0
    for x in range(len(frequency)):
        if frequency[x] != 0:
            arr.extend([x] * frequency[x])
    return arr
```

# 402. 移掉K位数字
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
注意:
num 的长度小于 10002 且 ≥ k。
num 不会包含任何前导零。
## 栈
```python
def removeKdigits(num, k):
    stack = []
    remain = len(num) - k
    for n in num:
        while k and stack and stack[-1]> n:
            stack.pop()
            k -= 1
        stack.append(n)
    return ''.join(stack[:remain]).lstrip('0') or '0'
```

# 452. 用最少数量的箭引爆气球
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。
给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。
## 贪心暴力法
```python
def findMinArrowShots(points):
    n = 0
    while points:
        x = points[0][0]
        j = 0
        max_count = 0
        while x <= points[0][1]:
            count = 0 
            for point in points:
                if x>= point[0] and x<= point[1]:
                    count += 1
            if max_count < count:
                j = x
                max_count = count
            x += 1
        i = 0
        while i <len(points):
            if j>= points[i][0] and j<= points[i][1]:
                del points[i]
                i -= 1
            i += 1
        n += 1
    return n
```
## 右边界排序贪心
```python
def findMinArrowShots(points):
    if not points:
        return 0
        
    points.sort(key=lambda balloon: balloon[1])
    pos = points[0][1]
    ans = 1
    for balloon in points:
        if balloon[0] > pos:
            pos = balloon[1]
            ans += 1
        
    return ans
```

# 454. 四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[ i] + B[ j] + C[ k] + D[ l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
## 哈希表计数法
```python
def fourSumCount(A, B, C, D):
    dic = {}
    count = 0
    for u in A:
        for v in B:
            if u+v not in dic:
                dic[u+v] = 1
            else:
                dic[u+v] += 1
    for u in C:
        for v in D:
            if -u-v in dic:
                count += dic[-u-v]
    return count
```

# 493. 翻转对
给定一个数组 nums ，如果 i < j 且 nums[ i] > 2*nums[ j] 我们就将 (i, j) 称作一个重要翻转对。
你需要返回给定数组中的重要翻转对的数量。
## 反向历遍+bisect模块
```python
def reversePairs(nums):
    tb, res = [], 0
    for n in reversed(nums) :
        res += bisect.bisect_left(tb, n)
        n2 = 2*n
        bisect.insort_right(tb, n2)
        return res
```
1. 反向历遍数组，将其两倍按顺序插入tb，累加下一项在tb的索引值

# 976. 三角形的最大周长
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。
## 贪心+排序
```python
def largestPerimeter(A):
    A.sort(reverse=True)
    for i in range(len(A)-2):
        if A[i]<A[i+1]+A[i+2]:
            return A[i]+A[i+1]+A[i+2]
    return 0
```

# 767. 重构字符串
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。
## 计数+贪心
```python
def reorganizeString(S):
    d, max_key, max_value = {}, 'a', 0
    for i in range(len(S)):
        if S[i] not in d:
            d[S[i]] = 1
        else:
            d[S[i]] += 1
        if d[S[i]] > max_value:
            max_key, max_value = S[i], d[S[i]]
    if max_value > 1 + (sum(d.values()) - max_value):
        return ''
    elif len(d) == 1:
        return S
    key_value, res = [list(item) for item in sorted(list(d.items()), key=lambda x: x[1])], ''
    sub_key, sub_value = key_value[len(key_value)-2][0], key_value[len(key_value)-2][1]
    for i in range(len(key_value)):
        while key_value[i][1]:
            for j in range(i, len(key_value)):
                res += key_value[j][0]
                key_value[j][1] -= 1
        if key_value[i][0] == sub_key:
            break
    left_value, index = max_value - sub_value, 0
    while left_value:
        if index == 0 or (res[index] != max_key and res[index-1] != max_key):
            res = res[:index] + max_key + res[index:]
            left_value -= 1
        index += 1
    return res
```

## 最大栈
```python
def reorganizeString(S):
    res = ""
    counter = collections.Counter(S)
    if max(counter.values()) > (len(S)+1) // 2:
        return res
    pq = []
    for key,val in counter.items():
        heapq.heappush(pq,(-val,key))
    prev = (0,None)
    while pq:
        v,k = heapq.heappop(pq)
        res += k
        if prev[0] < 0:
            heapq.heappush(pq,prev)
        prev = (v+1,k)
    return res
```