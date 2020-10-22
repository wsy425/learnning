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
1. 用()而不是[]
```python
dimensions = (200,50)
```
2. 一个元素的元组必须加","，因为小括号有优先级问题
```python
dimensions = (200,)
```
### 遍历元组
和列表一样
### 修改元组变量
1. 重新定义，不能单独修改一个值
2. 元组本身不能改变，但元组内可变元素（列表等）是可以改变的

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
1. 检索方式，查找不到key会报错
```python
alien_0 = {'color':'green'}
print（alien_0['color']） 
```
2. get方式查找不到会返回None
```python
alien_0 = {'color':'green'}
print（alien_0.get('color')） 
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

# 类
1. 面向对象：编写表示现实世界中的事物和情景的类，基于这些类来创建对象
2. 实例化：根据类来创建对象
## 创建和使用类
### 创建类
```python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.title() + " rolled over!")
```
1. 类中的函数称为方法，与函数的差别在于调用方法的方式。方法`__init__()`很特殊，根据Dog类创建新实例时，python都会自动运行它。
2. 对于方法`__init__()`，形参self必不可少且必须位于其他形参前面，是指向实例本身的引用，让实例能够访问类中的属性和方法
3. 属性：以self为前缀的变量，可供类中所有方法使用，可以通过类的任何实例来访问这些变量
### 根据类创建实例
#### 访问属性
```python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.title() + " rolled over!")

my_dog = Dog('willie', 6）
print(my_dog.name)
```
#### 调用方法
```python
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.title() + " rolled over!")

my_dog = Dog('willie', 6）
my_dog.sit()
my_dog.roll_over()
```
## 使用类和实例
### 给属性指定默认值
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 #对该属性设定初始值在方法__int__中就不需要该属性的形参
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

my_new_car = Car('audi' , 'a4' , 2016)
my_new_car.read_odometer()
```
### 修改属性值
#### 直接修改属性值
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

my_new_car = Car('audi' , 'a4' , 2016)
my_new_car.odometer_reading = 23 #直接在外部修改类内属性值
my_new_car.read_odometer()
```
#### 通过方法修改属性的值
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    #设置一个def的方法
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

my_new_car = Car('audi' , 'a4' , 2016)
my_new_car.update_odometer(23)
my_new_car.read_odometer()
```
## 继承
编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，可使用继承继承。一个类继承继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为父类父类，而新类称为子类子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法
### 子类的方法__int__()
创建子类时，父类必须包含在当前文件中，且位于子类前面
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

class ElectricCar(Car):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)#将父类和子类关联起来

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla,get_descriptive_name())
```
### 给子类定义属性和方法
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 
    def update_odometer(self,mileage):
        self.odometer_reading = mileage
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has" + str(self.odometer_reading) + "miles on it.")

class ElectricCar(Car):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)
        self.battery_size = 70 #子类设置新的属性
    
    def describe_battery(self):
        print("This car has a" + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla,get_descriptive_name())
my_tesla.describe_battery()
```
### 重写父类的方法
对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。这样，Python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = 0 
    def fill_gas_tank(gas):
        gas_tank += gas

class ElectricCar(Car):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)
    # 添加一种父类里存在的方法改写父类
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")
```
### 将实例用作属性
```python
class Car():
    def __int__(self , make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.gas_tank = 0 
    def fill_gas_tank(gas):
        gas_tank += gas

class Battery():
    def __int__(self, battery_size = 70):
        self.battery_size = battery_size
    def describe_battery(self):
        print("This car has a" + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    def __int__(self, make, model, year):
        super().__int__(make, model, year)
        self.battery = Battery() #将属性连接上前面的实例

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
```
## 导入类
### 导入单个类
```python
from car import Car
```
### 从一个模块中导入多个类
```python
from car import Car, ElectricCar
```
### 导入整个模块
```python
import car
```
### 导入模块中的所有类
```python
from module_name import *
```
### 在一个模块中导入另一个模块

# 文件和异常
## 读取文件数据
### 读取整个文件
```python
with open('pi.txt') as file_object:
    contents = file_object.read()
    print(contents)
```
1. open()函数：打开在当前文件同目录下的接收参数文件
2. with关键字：在不再需要访问文件后将文件关闭，就可以不用调用close()，减少出现bug的可能性，python会自动帮你关闭
3. .read()方法：读取文件的全部内容
### 文件路径
1. 相对路径
`with open('text_files/filename.txt') as file_object`
在当前文件所处文件夹下的text_files内的filename.txt处
2. 绝对路径
```python
file_path = 'C:\\Users\\ehmatthes\\other_files\\text_files\\filename.txt'
with open(file_path) as file_object
```
### 逐行读取
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
        for line in file_object:      print(line.rstrip())
```
### 创建包含文件各行内容的列表
```python
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()#从文件中读取每一行形成一个列表
    for line in lines:
        print(line.rstrip())
```
## 写入文件
### 写入空文件
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming
```
1. open()函数的两个常用实参：第一个为文件名称；第二个为文件打开方式，可指定为：
    + 读取模式'r'
    + 写入模式'w'
    + 附加模式'a'
    + 同时读取和写入'r+'
2. 如果写入的文件不存在函数open()会自动创建
3. 以写入打开，如果指定文件存在，python将在返回文件对象前清空该文件
### 写入多行
函数write()不会在你写入的文本末尾添加换行符
```python
filename = 'programming.txt'
with open(filename, 'w') as file_object:  
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n)
```
### 附加到文件
以附加模式打开文件，给文件添加内容但不覆盖原有内容；如果文件不存在自动创建一个空文件
```python
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n)
```
## 异常
python发生错误时会创建一个异常对象，如果编写了处理该异常的代码，程序将继续运行；若未对异常进行处理，程序将停止并显示一个traceback
### try-except代码块
```python
try:
    print(5/0)
except ZeroDivisionError:
    print("你不能拿0当除数！")
```
1. try后面的代码没问题将跳过except代码块
2. try后面的代码有问题且报错与except后标注一致则运行except代码块
### 使用异常避免崩溃
```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```
### 不报错
```python
try:
    print(5/0)
except ZeroDivisionError:
    pass
```
## 存储数据
### json.dump()和json.load()
```python
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)#将numbers存储到f_obj文件中
```
```python
import json
filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)#读取json文件
    print(numbers)
```
### 保存和读取用户生成的数据
```python
import json
# 如果以前存储了用户名，就加载它
#否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
else:
    print("Welcome back, " + username + "!")
```
### 重构
```python
import json
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
```

# 测试代码
## 测试函数
```python
import unittest
from name_function import get_formatted_name
class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()
```
1. 首先导入模块unittest和要测试的函数get_formatted_name
2. 创建一个类，用于包含一系列针对get_formatted_name()的单元测试，这个类必须继承unittest.TestCase类
3. assertEqual()断言方法：核实结果是否与期望的结果一致
## 断言方法
| 序号 | 断言方法 | 断言描述 |
| :----: | ----: | :----: |
| 1 | assertEqual(a, b, msg=None) | 验证a = b |
| 2 | assertNotEqual(a, b, msg=None) | 验证a != b |
| 3 | assertTrue(x, msg=None) | 验证x是true|
| 4 | assertFalse(x, msg=None) | 验证x是false|
| 5 | assertIsInstance(obj, cls, msg=None) | 验证obj是cls的实例|
| 6 | assertIn(arg1, arg2, msg=None) | 验证arg1是arg2的子串|
## 测试类
```python
import unittest
from survey import AnonymousSurvey
class TestAnonmyousSurvey(unittest.TestCase):
    """针对AnonymousSurvey类的测试"""
    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
         """测试单个答案会被妥善地存储"""
        question = "What language did you first learn to speak?"
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善地存储"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```
1. 应用setUp()使测试中只用实例化一次类