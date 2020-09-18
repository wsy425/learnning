# 基础操作
ndarray：存储高维数组的对象
## 创建数组
```python
import numpy as np
arr = np.zeros((10, 10)) #创建数组，10*10全是0的数组
np.arange(10) #从0开始的10个自然数
np.arange(1, 5, 0.5) #生成等差数列,1到5间隔0.5的等差数列
np.ones #生成全是1的数组
np.eye #生成单位矩阵
```
## 读取维度
`arr.ndim #`
## 读取各维度大小
`arr.shape`
## 读取元素类型
`arr.dtype` 
## 与list的互相转换
```python
arr.tolist() #变换成python原生list
arr=np.array() #python原生list变换成ndarray
```
## 改变数据类型
```python
ex1 = np.arange(10)
ex1.astype(np.float64) #调用astype方法更改ndarray中所有变量的类型
ex1 = np.arange(10, dtype=np.float32) #创建时通过dtype参数来设置数据类型
```
numpy 支持的数据类型：int（带符号和不带符号的8、32、64、128）、float（16、32、64、128）、complex（64、128、256）、string_、object、unicode_
# 计算
## 一般计算
基本的四则运算和逻辑运算都可以实现
Numpy中四则运算符直接映射到对应的元素中
逻辑运算返回False、True
可以通过np的api进行常见数学计算公式：log、exp、pow等，与math中一致
```
arr = np.array([[1,2,3],[2,2,3]])
```
![直接四则运算](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603182016223.png)
![api运算](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603182102031.png)
![数组比较](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603182134119.png)
## 广播计算
### 单数字广播
```python
arr + 3 #数组中所有数字全加3
arr ** 2 #数字全平方
```
### 行向量或列向量广播
将行向量或列向量与原数组的各行或各列作运算
# 切片
## 切片操作
我们用上下标加上冒号来表示我们想要切片的范围， 和Python一样，这是一个左闭右开的区间。
```python
arr[4:10] #取4到10位
arr[::-1] #反向切片
```
## 拷贝操作
Numpy中的切片代表原数组一段区间的引用，而不是拷贝。也就是说我们修改切片中的内容是会影响原数组的
为了不影响原数组需要拷贝是需要调用copy方法
```python
arr[3:10].copy() #复制数组
```
# 索引
## 普通索引
支持和python一样的多个方括号锁定元素位置；也支持python原生数组不支持的逗号分隔查询
```python
arr[2][3] #python原生支持
arr[0,1,1] #python原生不支持
```
拿3维数组举例，如果我们访问的时候只用一个下标，那么我们获得的是一个二维数组。如果使用两个下标，则获得的是一个一维数组。对于更高的维度也是同样。
## 切片索引
![](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603183514329.png)
![](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603183528121.png)
## bool索引
![](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603183706776.png)
![](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603183721134.png)
## 花式索引
![](C:%5CUsers%5CWIN10%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images%5Cimage-20200603183757165.png)
以次去3、2、1、1、3行的arr组成新的数组