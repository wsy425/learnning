# DOM

## DOM相关概念
1. DOM:文档对象模型（Document Object Model），是W3C组织推荐的处理可扩展标记语言的标准编程接口
2. DOM树：
    1. 文档：一个界面就是一个文档，document
    2. 元素：页面内的标签，element
    3. 节点：网页中所有内容，node
    4. DOM将以上元素都看作对象

## 获取元素
### 根据ID获取
1. 语法`getElementById(id)`
2. id是一个大小写敏感的字符串
3. 返回匹配ID 的element对象
4. 找不到则返回null
### 根据标签名获取
1. 语法`getElementsByTagName(标签名)`
2. 标签名要求输入大小写敏感字符串
3. 返回获取元素对象的集合，以伪数组形式存储
4. 得到的元素对象是动态的
5. 找不到返回空的伪数组
6. 可以通过指定父元素查询特定父元素内的标签元素
```JavaScript
var ol = document.getElementsByTagName('ol');
console.log(ol[0].getElementsByTagName('ul'));
```
### 根据类选择器获取
1. HTML5才支持
2. 语法`getElementsByClassName(类名)`
3. 类名要求输入大小写敏感字符串
4. 返回获取元素对象的集合，以伪数组形式存储
### 根据选择器直接获取第一个
1. HTML5才支持
2. 语法`querySelector(选择器名)`
3. 返回指定选择器的第一个元素对象
4. 选择器名要求输入大小写敏感字符串，需要加符号表明选择器类型
### 根据选择器直接获取全部
1. HTML5才支持
2. 语法`querySelectorAll(选择器名)`
3. 返回指定选择器的所有元素对象
4. 选择器名要求输入大小写敏感字符串，需要加符号表明选择器类型
### 获取body和html元素
1. `document.body`获取body标签
2. `document.documentElement`获取html标签

## 事件基础
1. 事件：一种被JavaScript侦测到的行为
2. 事件由三部分组成：事件源；事件类型；事件处理程序
### 事件三要素
1. 事件源：事件被触发的对象
2. 事件类型：如何被触发
3. 事件处理程序：通过一个函数赋值的方式完成
4. 例子
```JavaScript
var btn = document.getElementById('btn');
btn.onclick = function(){
    alert('弹出对话框')
}
```
### 执行事件的步骤
1. 获取事件源
2. 注册事件（绑定事件）
3. 添加事件处理程序（采取函数赋值形式）
4. 常见鼠标事件
![常见鼠标事件.jpg](https://i.loli.net/2021/03/05/3Ku6IEfPV5Gg7M2.jpg)
