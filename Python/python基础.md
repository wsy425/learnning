# 变量与简单数据类型
## 变量
1. 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头
2. 变量名不能包含空格，但可使用下划线来分隔其中的单词
3. Python关键字和函数名不能用作变量名
## 字符串
1. name.title():首字母大写显示每个单词
2. 拼接字符串：+
```python
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
```
3. 使用制表符或换行符来添加空白
\t:制表符，一个tab
\n:换行符，换行
4. 删除空白
rstrip():暂时删除字符串末尾空白
lstrip():暂时删除字符串开头空白
strip():暂时删除字符串两端空白
5. 历遍字符串
```python
for i , n in enumerate(s):
```
## 数字
### 整数（int）
### 浮点数（float）
带小数点的数字
### str()
将得字符串转换为字符串，这样才能print

# 列表
## 概述
1. 定义：由一系列按特定顺序排列的元素组成
2. 访问列表元素：指出索引即可
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
print(bicycles[0])
```
3. 索引从0开始,负数可以反向索引
## 修改、添加和删除元素
### 修改
直接赋值
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles[0] = 'ducati'
```
### 添加
#### 末尾添加元素(.append)
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.append('ducati')
```
#### 在列表中插入元素(.insert)
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.insert(0,'ducati') #在位置0插入decati
```
### 删除
1. del语句
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
del  bicycles[0]
```
2. pop()
删除列表末尾的元素，出栈
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
poped_bicycles = bicycles.pop()
```
3. 弹出列表任意位置处的元素
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
poped_bicycles = bicycles.pop(0)
```
4. 根据值删除元素(.remove)
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.remove('trek')
```
## 组织列表
### .sort()
永久性按照字母顺序排序
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.sort() #字母顺序
bicycles.sort(reverse=True) #字母反顺序
```
### .sorted()
临时性按照字母顺序排序
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.sorted() #字母顺序
bicycles.sorted(reverse=True) #字母反顺序
```
### .reverse()
永久性反转列表
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
bicycles.reverse()
```
### 确定列表长度len()
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
len(bicycles)
```
## 历遍列表
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
for bicycle in bicycles:
    print(bicycle)
```
## 创建数值列表
```python
numbers = list(range(1,7,2)) #从1到7每2个取1个
[1,3,5]
numbers = [] #空列表
min(numbers)
max(numbers)
sum(numbers)
```
## 使用列表的一部分
### 切片
```python
numbers = list(range(1,7,))
print(numbers[1:5:-1]) #从1到5反向切片
[5,4,3,2]
```
### 遍历切片
```python
numbers = list(range(1,7,))
for number in numbers[:4]:
    print(number)
[1,2,3,4]
```
### 复制列表
```python
bicycles = ['trek' , 'cannondale','redline' , 'speciaized']
#如果直接相等是复制的地址
list1 = bicycles
list1.append('ducati')
bicycles.append('')
print(list1)
['trek' , 'cannondale','redline' , 'speciaized' , 'ducati' , '']
print(bicycles)
['trek' , 'cannondale','redline' , 'speciaized' , 'ducati' , '']
#需要通过切片的形式复制
list1 = bicycles[:]
list1.append('ducati')
bicycles.append('')
print(list1)
['trek' , 'cannondale','redline' , 'speciaized' , 'ducati']
print(bicycles)
['trek' , 'cannondale','redline' , 'speciaized' , '']
```
## 元组
不可变的列表
### 定义元组
用()而不是[]
```python
dimensions = (200,50)
```
### 遍历元组
和列表一样
### 修改元组变量
重新定义，不能单独修改一个值

# if
## 条件测试
条件测试：值为True或Flase的表达式
### 检查是否相等
1. 使用==
2. 直接使用时考虑大小写
3. 加上.lower()时就可全部变为小写判断
### 检查是否不相等
使用!=
### 比较数字
可以包含等于、不等于、大于、小于等
### 检查多个条件
1. and表示和
2. or表示或
### 检查特定值是否在/不在
1. in表示在
2. not in表示不在
### 布尔表达式
## 语句结构
### if-else
### if-elif-else
### 多个elif
### 省略else

# 字典
## 使用字典
字典是一系列键——值对，每个键都与一个值相关，使用键来访问与之相关的值
```python
alien_0 = {'color':'green'}
```
'color'是键，与之相关的值是'green'
### 访问字典
```python
alien_0 = {'color':'green'}
print（alien_0['color']） 
```
### 创建字典
```python
alien_0 = {}
alien_0['color'] = 'green'
```
### 修改字典中的值
```python
alien_0 = {'color':'green'}
alien_0['color'] = 'yellow'
```
### 删除键——对值
```python
alien_0 = {'color':'green' , 'points':5}
del ailen_0['points']
```
## 历遍字典
### 历遍所有键——值对
.items()
```python
alien_0 = {'color':'green' , 'points':5}
for key,value in alien_0.items():
```
### 历遍字典中的所有键
.keys()
```python
alien_0 = {'color':'green' , 'points':5}
for key,value in alien_0.keys():
```
### 历遍字典中的所有值
.values()
```python
alien_0 = {'color':'green' , 'points':5}
for key,value in alien_0.values():
```
## 嵌套
### 字典列表
```python
alien_0 = {'color':'green' , 'points':5}
alien_1 = {'color':'yellow' , 'points':10}
alien_2 = {'color':'red' , 'points':15}
aliens = [alien_0 , alien_1 , alien_2]
for alien in aliens:
    if alien['color'] == 'green':
        print(alien['points'])
```
### 字典中存储列表
```python
favorite_languages = {'jen':['python' , 'ruby'] , 'sarah':['ruby' , 'go'] , 'edward':['c']}
for name,languages in favorite_languages.item():
    for language in  languages:
        print(language)
```
### 字典中存储字典
```python
users = {
    'aeinstein': {'first': 'albert' , 'last': 'einstein' ,'location':'princeton'},
    'mcurie': {'first': 'marie' , 'last': 'curie' , 'location': 'paris'}
    }
for username,user_info in users.item():
    print("\nUsername: " + username)
    for key,value in user_info:
        print(key + value)
```

# 用户输入与while循环
## 函数input()
```python
height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!"
else:
    print("\nYou'll be able to ride when you're a little olde.")
```
## while循环
### 使用while循环
```python
current_number = 1
while current_number <= 5:
    print(current_number)    current_number += 1
```
### 使用break退出循环
```python
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
```
### 使用continue继续
```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
```

# 函数
## 定义函数
```python
def greet_user(username):
    print('Hello' + username.title() + '!')

greet_user()
```
输入的username是一个形参，如果直接输入信息则为实参
## 传递实参
### 位置实参
一种函数调用中的实参与函数定义中的形参的关联方式，基于实参的顺序
```python
def describe_pet(animal_type , pet_name):
    print("\nI have a" + animal_type + ',')
    print('My' + animal_type + "'s name is" + pet_name.title() + '.')

describe_pet('hamster' , 'harry')
```
### 关键字实参
传递给函数名称——值对
```python
def describe_pet(animal_type , pet_name):
    print("\nI have a" + animal_type + ',')
    print('My' + animal_type + "'s name is" + pet_name.title() + '.')

describe_pet(animal_type ='hamster' , pet_name = 'harry')
```
### 默认值
定义函数时可以设置默认值
```python
def describe_pet(animal_type , pet_name = 'harry'):
    print("\nI have a" + animal_type + ',')
    print('My' + animal_type + "'s name is" + pet_name.title() + '.')

describe_pet('hamster')
```
## 返回值
### 返回简单值
```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
### 令实参变成可选的
```python
def get_formatted_name(first_name, last_name , middle_name = ''):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
### 返回字典
```python
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
### 结合使用函数和while
```python
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: "
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!"
```
## 传递列表
```python
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```
### 禁止函数修改列表
```python
def function(list_name):

function(list1[:])
```
通过传递列表副本禁止函数修改列表
## 传递任意数量的实参
```python
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('mushrooms', 'green peppers', 'extra cheese')
```
形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
### 位置实参和任意数量实参结合
先匹配位置实参和关键字实参，剩余实参都收集到最后一个任意数量形参中去
## 将函数存储在模块中
模块是扩展名为.py的文件，包含要导入到程序中的代码
```python
import pizza
from module_name import function_0, function_1, function_2
from pizza import make_pizza as mp
import pizza as p
from pizza import * #导入模块中所有函数
```