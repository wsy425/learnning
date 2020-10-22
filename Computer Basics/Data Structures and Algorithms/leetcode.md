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