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
### 常用键盘事件
1. DOM.onkeyup：某个键盘按键被松开时触发，不区分大小写
2. DOM.onkeydown：某个键盘按键被按下时触发，不区分大小写
3. DOM.onkeypress：耨个键盘按键被按下时触发（不能识别功能键），区分大小写
4. 三个事件的执行顺序，先执行down再执行press最后执行up
### 键盘事件对象
1. e.keyCode：返回按键对应的ASCII码值，不区分大小写时是输出大写的ASCII码



# BOM

## BOM相关概念
1. BOM（Browser Object Model）浏览器对象模型，它提供了独立于内容而与浏览器进行交互的对象，其核心对象是window
2. BOM由一系列对象构成，并且每个对象都提供了很多方法与属性
3. BOM缺乏标准，JavaScript语法的标准化祖师是ECMA，DOM的标准化组织是W3C，BOM最初是Netscape浏览器标准的一部分
### BOM的构成
1. BOM比DOM更大，包含DOM
2. window：
   + document
   + location
   + navigation
   + screen
   + history
3. window对象是浏览器的顶级对象，具有双重角色
   + 是JS访问浏览器窗口的一个接口
   + 是一个全局对象，定义在全局作用域中的变量、函数都会变成window对象的属性和方法。调用的时候可以省略window

## window对象常见事件
### 窗口加载事件
1. 语法`window.onload = function(){}`或者`window.addEventListener("load",function(){})`
2. window.onload是窗口加载事件，当文档内容完全加载完成才会触发该事件
3. 有了window.onload就可以吧JS代码写到页面元素的上方
4. window.onload传统注册事件方式只能写一次，如果有多个会以最后一个为准
5. 如果使用addEventListener没有个数限值
6. 有一个类似的事件`document.addEventListener('DOMContentLoaded',function(){})`，仅当DOM加载完成，不包括样式表，图片，flash等，ie9以上才支持
### 调整窗口大小事件
1. 语法`window.onresize = function(){}`或者`window.addEventListener("resize",function(){})`
2. window.onresize是调整窗口大小加载事件
3. 只要窗口大小发生像素变化，就会触发这个事件
4. 经常利用这个事件完成响应式布局。window.innerWidth属性对应当前屏幕的宽度

## 定时器
### 两种定时器
1. setTimeout()
2. setInterval()
### setTimeout()
1. 语法`window.setTimeout(调用函数,[延迟的毫秒数])`
2. 用于设置一个定时器，该定时器在定时器到期后执行调用函数
3. 延时时间单位是毫秒，单位不用写。整体可以省略，默认是0
4. 调用函数可以直接写函数，也可以写函数名，还可以写`函数名()`但不推荐
5. 页面中会存在很多定时器，需要给定时器加标识符
6. setTimeout里的调用函数也称为回调函数callback。这个函数需要等待事件，时间到了才去调用这个函数
### 停止setTimeout()定时器
1. 语法`window.clearTimeout(timeout ID)`
2. clearTimeout()方法取消了先前通过调用setTimeout()建立的定时器
3. window可以省略
4. 括号里面的是定时器的标识符
### setInterval()
1. 语法`window.setInterval(调用函数,[间隔的毫秒数])`
2. setInterval()方法重复调用一个函数，每隔一段时间就去调用一次回调函数
### 停止setInterval()定时器
1. 语法`window.clearInterval(interval ID)`
2. 与停止setTimeout一致
### this
1. 函数定义的时候无法确认，函数被调用的时候才能确定this指向谁，一般指向调用它的对象
2. 全局作用域或者普通函数中this指向全局对象window
3. 定时器里面的this指向window
4. 在方法中this指向方法
5. 构造函数中this指向构造函数的实例

## JS执行队列
### JS是单线程
1. JavaScript语言的一大特点是单线程，就是同一个时间只能做一件事
2. 是因为JavaScript是为了操作DOM，必须先添加再删除，所以必须是单线程
3. 单线程意味着所有任务需要排队，带来的问题是JS执行时间过长，页面渲染不连贯，导致页面渲染加载阻塞的感觉
### 同步和异步
1. 为了解决JS执行过长渲染不连贯的问题，利用多核CPU的计算能力，HTML5提出Web Worker标准，允许JavaScript脚本创建多个线程，JS出现同步和异步
2. 同步：前一个任务结束后再执行后一个任务，程序的执行顺序与任务的排列顺序是一致的、同步的
3. 异步：在做一件事的同事还可以处理其他的事情
4. JS把任务分成两种
   + 同步任务：同步任务都在主线程上执行，形成一个执行栈
   + 异步任务：JS的异步任务是通过回调函数实现的
   + 常见的异步任务
      - 普通事件，click、resize
      - 资源加载，load、error
      - 定时器，setInterval、setTimeout
   + 异步任务相关回调函数添加到任务队列中（任务队列也叫消息队列）
### JS执行机制
1. 先执行执行栈中的同步任务
2. 遇到回调函数把异步任务放入任务队列中
3. 一旦执行栈中的所有同步任务执行完毕，系统就会按次序速去任务队列中的异步任务，于是被读取的异步任务结束等待状态，进入执行栈，开始执行
4. 事件循环(event loop)：由于主线程不断的重复获得任务、执行任务的机制

## location对象
1. window对象给我们提供了一个location属性用于获取或设置窗体的URL，并且可以用于解析URL
2. 因为这个属性返回的是一个对象，所以将这个属性称为location对象
### URL
1. 统一资源定位符是互联网上标准资源的地址
2. 一般语法格式`protocol://host[:port]/path/[?query]#fragment`
3. protocol:通信协议 常用的http，ftp，maito等
4. host：主机(域名)
5. port：端口号，可选，省略时使用方案的默认端口
6. path：路径，由零活多个'/'符号隔开的字符串，一般用来表示主机上的一个目录或文件地址
7. query：参数，以键值对的相识，通过&符号分隔开
8. fragment:片段，#后面内容常见于连接锚点
### location对象的属性
![location常见属性.png](https://i.loli.net/2021/04/28/uHX4yLh3GMZF7qt.png)
### location对象的方法
![location常见方法.png](https://i.loli.net/2021/04/28/TJDAL6keQuSCXwy.png)

## navigator对象
1. navigator对象包含浏览器的相关信息
2. navigator对象最常用的属性是userAgent，返回有客户机发送服务器的user-agent头部值

## history对象
1. window对象提供一个history对象，与浏览器历史记录进行交互。该对象包含用户（在浏览器窗口中）
2. back()：后退功能
3. forward()：前进功能
4. go(参数)：前进后退功能。参数是1前进1个页面，-1后退1个页面



# PC网页特效
## 元素三大系列
### 元素偏移量offset系列
1. 使用offset系列相关属性可以动态地得到该元素的位置、大小
2. 获得元素距离带有定位父元素的位置
3. 获得元素自身的大小（宽度高度）
4. 返回的数值不带单位
#### offsetLeft与offsetTop
1. 各自返回元素相对于有定位父元素的上方、左边偏移量
2. 如果没有定位的父元素，则以body为准
#### offsetWidth与offsetHeight
1. 各自返回元素包括padding、边框、内容区的宽度、高度
#### offsetParent
1. 返回该元素带有定位的父级元素
2. 父级都没有定位则返回body
#### offset与style区别
1. offset
   + 可以得到任意样式表中的样式值
   + 获得的数值没有段位
   + offsetWidth包含padding、border和width
   + 只能读属性不能赋值
   + 更合适获取元素大小位置
2. style
   + 只能得到行内样式表中的样式值
   + 获得带有单位的字符串
   + style.width不包含padding和border
   + 可读写属性
   + 更适合给元素赋值
### 元素可视区client系列
1. 使用client系列的相关属性可以动态得到元素边框大小、元素大小等
#### clientTop与clientLeft
1. 各自返回元素包括上边、左边边框大小
#### clientWidth与clientHight
1. 各自返回元素包括padding、内容区的宽度、高度
2. 与offset最大的区别就是不包含边框大小
### 元素滚动scroll系列
1. 使用scroll系列的相关属性可以动态地得到该元素的大小、滚动距离等
2. 滚动条滚动会触发onscroll事件
3. 页面的滚动距离使用`window.pageXOffset`获得
#### scrollTop与scrollLeft
1. 各自返回被卷去的上侧、左侧距离
2. 返回数值不带单位
#### scrollWidth与scrollHight
1. 各自返回自身实际宽度、高度，不含边框
2. 返回数值不带单位
3. 返回的是包含内容overflow的大小
### 立即执行函数
1. 不需要调用，立马能够自己执行的函数
2. 语法1`(function() {})()`
3. 语法2`(function() {}())`
4. 立即执行函数最大的作用是独立创建了一个作用域
5. 所有变量都是局部变量，不存在命名冲突
### moseenter和mouseover区别
#### mouseenter
1. 当鼠标移动到元素上时会触发mouseenter事件
2. mouseenter只在经过自身盒子时触发
3. 不会有冒泡的概念
4. 搭配使用的是mouseleave，同样不会冒泡
#### mouseover
1. 当鼠标移动到元素上时会触发mouseover事件
2. 不仅经过自身盒子会触发，经过子盒子也会触发

## 动画函数
### 动画实现原理
通过定时器setInterval()不断移动盒子位置
1. 获得盒子当前的位置
2. 让盒子在当前位置上加移动距离
3. 加一个结束定时器的条件
4. 注意此元素需要添加定位，才能使用element.style.left
### 动画函数简单封装
1. 函数需要传递2个参数，动画对象和移动到的距离
### 缓动动画
1. 原理：让元素运动有所变化，最常见的是让速度慢慢停下
2. 核心算法：每次移动步长=Math.ceil/floor((目标值-现在的位置)/10)
### 动画函数添加回调函数
1. 回调函数原理：函数作为一个参数。将这个函数作为参数传到另一个函数里面，当那个函数执行完之后，再执行传进去的这个函数，这个过程叫做回调
2. 可以把函数当做一个参数输入另一个函数中
### 动画函数封装
1. 单独创建一个JS文件
2. 把函数写在里面
3. 在html中引入JS文件

# WebStorage js本地存储
1. 存储内容大小一般支持 5MB 左右（不同浏览器可能还不一样） 
2. 浏览器端通过Window.sessionStorage和Window.localStorage属性来实现本地存储机制 
3. 相关API
   xxxStorage.setItem('key', 'value')该方法接受一个键和值作为参数，会把键值对添加到存储中，如果键名存在，则更新其对应的值
   xxxStorage.getItem('key')该方法接受一个键名作为参数，返回键名对应的值
   xxxStorage.removeItem('key')该方法接受一个键名作为参数，并把该键名从存储中删除
   xxxStorage.clear()该方法会清空存储中的所有数据
4. 备注
   1. SessionStorage存储的内容会随着浏览器窗口关闭而消失
   2. LocalStorage存储的内容，需要手动清除才会消失
   3. xxxStorage.getItem(xxx)如果 xxx 对应的 value 获取不到，那么getItem()的返回值是null
   4. JSON.parse(null)的结果依然是null