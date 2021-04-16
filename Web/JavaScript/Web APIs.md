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
1. 获取事件源`var div = document.querySelector('div')`
1. 注册事件（绑定事件）`div.onclick`
2. 添加事件处理程序（采取函数赋值形式）`div.onclick = function(){}`
3. 常见鼠标事件
![常见鼠标事件.jpg](https://i.loli.net/2021/03/05/3Ku6IEfPV5Gg7M2.jpg)
4. 事件补充
   + onfocus获取焦点
   + onblur失去焦点

## 操作元素
1. 可以不用事件直接使用元素
### 修改元素内容
1. element.innerText
   + 语法`DOM.innerText = 内容`
   + 不识别HTML标签，里面的标签会直接显示
   + 可以获取元素的内容，会去除空格和换行
2. element.innerHTML
   + 语法`DOM.innerHTML = 内容`
   + 识别HTML标签
   + 用的多，是W3C标准
   + 可以获取元素内容，保留空格和换行
### 修改元素属性
1. 语法`DOM.属性 = 内容`
   + 获取的是内置的属性值，元素本身自带的属性
2. 第二种得到元素属性的方法`DOM.getAttribute('属性')`
   + 可以获取自定义属性
3. 第二种更改元素属性值的方法`DOM.setAttribute('属性','值')`
   + 主要针对于自定义属性
4. 移除属性值`DOM.removeAttribute('属性')`
5. 表单元素操纵
   + 使用表单自己的属性改变里面的内容
   + 改变表单值使用value属性
   + 表单被禁用使用disabled属性
### 修改样式属性
1. element.style 行内样式操作
   + style里的属性采用驼峰命名法
   + 产生的是行内样式，css权重比较高
2. element.className 类名样式操作
   + 将当前元素类名进行修改，是直接替换的
   + 要添加新的类可以使用+=
### H5自定义属性
1. 规定自定义属性以data-开头并赋值
2. 新增一种获取自定义属性方法`DOM.dataset.data后面的属性名`或者`DOM.dataset[data后面的属性名]`
3. dataset是一个存放了所有以data开头自定义属性的集合
4. 自定义属性中有多个-，获取的时候采取驼峰命名法

## 节点操作
1. 节点至少拥有nodeType节点类型、nodeName节点名称和nodeValue节点值这三个基本属性
2. nodeType
   + 元素节点为1
   + 属性节点为2
   + 文本节点为3（文本节点包含文字、空格、换行等）
### 节点层次
1. 利用DOM树可以把节点划分为不同的层次关系
2. 父级节点
   + 语法`DOM.parentNode`
   + 得到的是离元素最近的父级节点
3. 子节点
   + 语法`DOM.childNodes`
   + 得到的子节点集合，包含元素节点、文本节点等
   + 要获得里面的元素节点需要专门处理
   + 子元素节点语法`DOM.children`，不是标准方法
   + 获取第一个子节点`DOM.firstChild`
   + 获取最后一个子节点`DOM.lastChild`
   + 获取第一个子元素节点`DOM.firstElementChild`IE9以上才支持
   + 获取最后一个子元素节点`DOM.lastElementChild`IE9以上才支持
4. 兄弟节点
   + 语法`DOM.nextSibling`，得到下一个兄弟节点，包括文本节点
   + 语法`DOM.previousSibling`，得到上一个兄弟节点，包括文本节点。找不到则返回null
   + 语法`DOM.nextElementSibling`，得到下一个元素兄弟节点，找不到则返回null，IE9以上才支持
   + 语法`DOM.previousElementSibling`，得到上一个元素兄弟节点，找不到则返回null，IE9以上才支持
### 创建节点
1. `document.write('标签')`
   + 文档执行完毕会导致页面全部重绘，会重新创建新的页面
2. `DOM.createElement('节点名')`
   + 需要通过添加节点使用
   + 创建新元素，效率高
3. `DOM.innerHTML = '标签'`
   + 本质是拼接字符串，效率低
   + 但如果使用数组拼接，效率最高
### 添加节点
1. `DOM.appendChild(变量)`添加到父节点的子节点的末尾
2. `DOM.insertBefore(变量,指定元素)`添加到父节点的指定子节点的前面
### 删除节点
1. `DOM.removeChild(子节点)`从DOM中删除子节点
### 复制节点
1. `DOM.cloneNode()`返回调用该方法节点的一个副本
2. 需要通过添加节点使用
3. 括号参数
   + 空或者false，则是浅拷贝。只克隆复制节点本身，不克隆里面的子节点
   + true，则是深拷贝。隆复制节点本身和里面的子节点

## 事件高级
### 注册事件
#### 传统方式
1. 利用on开头的事件
2. 特点：注册事件的唯一性
3. 同一个元素同一个事件只能设置一个处理函数，最后注册的处理函数将会覆盖前面注册的处理函数
#### 方法监听
1. w3c标准 推荐方式
2. `DOM.addEventListener(type,listener[,useCapture])`是一个方法
3. 同一个元素同一个事件可以注册多个监听器
4. type：事件类型字符串，比如click、mouseover，注意不要带on
5. listener：事件处理函数，事件发生时，会调用该监听函数
   + 如果是写调用函数的名字，不需要加()
6. useCapture：可选参数，是一个布尔值，默认false
### 删除事件
#### 传统方式
1. `DOM.onclick = null;`
#### 方法监听
1. `DOM.removeEventListener(type,listener[,useCapture])`
### DOM事件流
1. 事件流描述的是从页面中接收事件的顺序
2. 事件发生时会在元素节点之间按照特定的顺序传播，这个传播过程即DOM事件流
3. 分成三个阶段：捕获阶段、当前目标阶段和冒泡阶段
   + 捕获：由DOM最顶层节点开始，逐级向下传播到最具体的元素接收的过程
   + 目标
   + 冒泡：事件开始时由最具体的元素接收，然后逐层向上传播到DOM最顶层节点的过程
4. JS代码只能执行捕获或者冒泡其中的一个阶段
5. onclick和attachEvent只能得到冒泡阶段
6. addEventListener(type,listener[ ,useCapture])
   + 第三个参数如果是true，表示在事件捕获阶段调用事件处理程序
   + false表示在事件冒泡阶段调用事件处理
7. 有些事件是没有冒泡的，比如onblur、onfocus、onmouseenter、onmouseleave
### 事件对象
1. event就是一个事件对象，写在侦听函数的小括号里，当作形参来看待
2. 事件对象只有有了事件才会存在，是系统给我们自动创建的，不需要传递参数
3. 事件对象是事件的一系列相关数据的集合
4. 事件对象可以自己命名
5. 事件对象也有兼容性问题，ie678要使用window.event
6. 常见属性方法
   + e.target：返回触发事件的对象（标准） PS：this是绑定事件的对象，和这个有区别
   + e.scrElement：返回触发事件的对象（ie678）
   + e.type：返回事件的类型，不带on
   + e.cancelBubble：该属性阻止冒泡（非标准ie678）
   + e.returnValue：该属性阻止默认事件（非标准ie678）
   + e.preventDefault()：该方法阻止默认事件（标准）
   + e.stopPropagation()：阻止冒泡（标准）
### 事件委托
1. 事件委托也称为事件代理，在jQuery里面称为事件委派
2. 事件委托原理：不是每个自建店单独设置事件监听器，而是事件监听器设置在其父节点上，然后利用冒泡原理影响设置每个子节点
3. 事件委托的作用：只操作一次DOM，提高了程序的性能
### 鼠标事件对象
1. e.clientX：返回鼠标相对于浏览器窗口可视区的X坐标
2. e.clientY：返回鼠标相对于浏览器窗口可视区的Y坐标
3. e.pageX：返回鼠标相对于文档页面的X坐标（ie9+支持）
4. e.pageY：返回鼠标相对于文档页面的Y坐标（ie9+支持）
5. e.screenX：返回鼠标相对于电脑屏幕的X坐标
6. e.screenY：返回鼠标相对于电脑屏幕的Y坐标