# JavaScript编程语言

## 1 简介

### 1.1 JavaScript简介
#### 1.1.1 JavaScript特性
JavaScript是一种**脚本**语言，以纯文本形式提供和执行，不需要特殊的准备或编译即可运行  
JavaScript可以被直接写在网页的HTML中，在页面加载时自动执行  
ECMAScript是JavaScript的语言规范  
JavaScript 不仅可以在浏览器中执行，也可以在服务端执行，甚至可以在任意搭载了 JavaScript 引擎 的设备中执行  
##### JavaScript 引擎  
* 有时也称作“JavaScript 虚拟机”
* 不同的引擎有不同的“代号”
* 引擎的工作流程
   1. 引擎（如果是浏览器，则引擎被嵌入在其中）读取（“解析”）脚本
   2. 引擎将脚本转化（“编译”）为机器语言
   3. 机器代码快速地执行

##### JavaScript独特性
JavaScript 是将这三件事结合在一起的唯一的浏览器技术
1. 与 HTML/CSS 完全集成
2. 简单的事，简单地完成
3. 被所有的主流浏览器支持，并且默认开启
#### 1.1.2 浏览器中的JavaScript
JavaScript 的能力很大程度上取决于它运行的环境。例如，Node.js 支持允许 JavaScript 读取/写入任意文件，执行网络请求等的函数  
##### 浏览器中JavaScript功能
浏览器中的 JavaScript 可以做与网页操作、用户交互和 Web 服务器相关的所有事情
1. 在网页中添加新的 HTML，修改网页已有内容和网页的样式
2. 响应用户的行为，响应鼠标的点击，指针的移动，按键的按动
3. 向远程服务器发送网络请求，下载和上传文件（所谓的 AJAX 和 COMET 技术）。
4. 获取或设置 cookie，向访问者提出问题或发送消息
5. 记住客户端的数据（“本地存储”）  
##### 浏览器中JavaScript限制
为了用户的（信息）安全，在浏览器中的 JavaScript 的能力是受限的。目的是防止恶意网页获取用户私人信息或损害用户数据
1. 网页中的 JavaScript 不能读、写、复制和执行硬盘上的任意文件。它没有直接访问操作系统的功能
2. 不同的标签页/窗口之间通常互不了解
3. JavaScript 可以轻松地通过互联网与当前页面所在的服务器进行通信。但是从其他网站/域的服务器中接收数据的能力被削弱了，需要来自远程服务器的明确协议（在 HTTP header 中）
#### 1.1.3 JavaScript的上层语言
出现了许多新语言，这些语言在浏览器中执行之前，都会被 编译（转化）成 JavaScript。现代化的工具使得编译速度非常快且透明，实际上允许开发者使用另一种语言编写代码并会将其“自动转换”为 JavaScript。
* CoffeeScript 是 JavaScript 的一种语法糖。它引入了更加简短的语法，使我们可以编写更清晰简洁的代码。通常，Ruby 开发者喜欢它。
* TypeScript 专注于添加“严格的数据类型”以简化开发，以更好地支持复杂系统的开发。由微软开发。
* Flow 也添加了数据类型，但是以一种不同的方式。由 Facebook 开发。
* Dart 是一门独立的语言。它拥有自己的引擎，该引擎可以在非浏览器环境中运行（例如手机应用），它也可以被编译成 JavaScript。由 Google 开发。
* Brython 是一个 Python 到 JavaScript 的转译器，让我们可以在不使用 JavaScript 的情况下，以纯 Python 编写应用程序。
* Kotlin 是一个现代、简洁且安全的编程语言，编写出的应用程序可以在浏览器和 Node 环境中运行。
#### 1.1.4 总结
* JavaScript 最开始是专门为浏览器设计的一门语言，但是现在也被用于很多其他的环境。
* JavaScript 作为被应用最广泛的浏览器语言，且与 HTML/CSS 完全集成，具有独特的地位。
* 有很多其他的语言可以被“编译”成 JavaScript，这些语言还提供了更多的功能。建议最好了解一下这些语言，至少在掌握了 JavaScript 之后大致的了解一下。


## 2 JavaScript基础知识
### 2.1 运行脚本
#### 2.1.1 script标签
我们几乎可以使用 `<script>` 标签将 JavaScript 程序插入到 HTML 文档的任何位置。
`<script>`标签中包裹了 JavaScript 代码，当浏览器遇到 `<script>` 标签，代码会自动运行
#### 2.1.2 script标签属性
`<script>` 标签有一些现在很少用到的特性（attribute），但是我们可以在老代码中找到它们
##### type 特性：`<script type=…>`
在老的 HTML4 标准中，要求 script 标签有 type 特性。通常是 type="text/javascript"。
##### language 特性：`<script language=…>`
这个特性是为了显示脚本使用的语言。这个特性现在已经没有任何意义，因为语言默认就是 JavaScript
##### 脚本前后的注释
在非常古老的书籍和指南中，你可能会在 `<script>` 标签里面找到注释，就像这样：
```html
<script type="text/javascript"><!--
    ...
//--></script>
```
这些注释是用于不支持 `<script>` 标签的古老的浏览器隐藏 JavaScript 代码的。由于最近 15 年内发布的浏览器都没有这样的问题
#### 2.1.3 外部脚本
脚本文件可以通过 src 特性（attribute）添加到 HTML 文件中
```html
<script src="/path/to/script.js"></script>
```
##### src路径
1. `/path`脚本文件从网站根目录开始的绝对路径
2. `./path`脚本文件对于当前页面的相对路径
3. `https://path`完整的 URL 地址
##### 外部脚本加载
1. 浏览器会下载外部脚本，并将它保存到浏览器缓存中
2. 其他页面想要相同的脚本就会从缓存中获取，而不是下载它。所以文件实际上只会下载一次
3. 可以节省流量，并使得页面（加载）更快

::: danger
如果设置了 src 特性，script 标签内容将会被忽略
:::
#### 2.1.3 总结
1. 我们可以使用一个 `<script>` 标签将 JavaScript 代码添加到页面中。
2. type 和 language 特性（attribute）不是必需的。
3. 外部的脚本可以通过 `<script src="path/to/script.js"></script>` 的方式插入。

### 2.2 代码结构
#### 2.2.1 语句
语句是执行行为（action）的语法结构和命令。  
我们可以在代码中编写任意数量的语句。语句之间可以使用<mark>分号</mark>进行分割。  
通常，每条语句独占一行，以提高代码的可读性  
#### 2.2.2 分号
当存在换行符（line break）时，在大多数情况下可以省略分号 
##### 自动分号插入
JavaScript 将换行符理解成“隐式”的分号
在大多数情况下，换行意味着一个分号。但是“大多数情况”并不意味着“总是”
```javascript
alert(3 +
1
+ 2);
```
**存在 JavaScript 无法确定是否真的需要自动插入分号的情况**
```javascript
alert("Hello")
[1, 2].forEach(alert);
// 会理解为
alert("Hello")[1, 2].forEach(alert);
```
#### 2.2.3 注释
单行注释以两个正斜杠字符 `//` 开始
多行注释以一个正斜杠和星号开始 `“/*”` 并以一个星号和正斜杠结束 `“*/”`
::: tip
在大多数的编辑器中，一行代码可以使用 <kbd>Ctrl</kbd>+<kbd>/</kbd> 快捷键进行单行注释，诸如 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>/</kbd> 的快捷键可以进行多行注释（选择代码，然后按下快捷键）
:::
::: danger
不支持注释嵌套
:::

### 2.3 现代模式
ES5 规范增加了新的语言特性并且修改了一些已经存在的特性。为了保证旧的功能能够使用，大部分的修改是默认不生效的。你需要一个特殊的指令 —— `"use strict"` 来明确地激活这些特性
`"use strict"` 或者 `'use strict'`。当它处于脚本文件的顶部时，则整个脚本文件都将以“现代”模式进行工作
`"use strict"` 可以被放在函数体的开头。这样则可以只在该函数中启用严格模式
::: danger
请确保 `"use strict"` 出现在脚本的最顶部，否则严格模式可能无法启用
没有办法取消 `use strict`
:::

### 2.4 变量
<mark>变量</mark>是数据的命名存储  

#### 2.4.1 变量使用
##### 变量声明
**声明**或者**定义**一个名为massage的变量`let massage`
可以将变量定义和赋值合并成一行`let message = 'Hello!'`
也可以在一行中声明多个变量`let user = 'John', age = 25, message = 'Hello';`
::: danger 多次声明
声明两次会触发 error
一个变量应该只被声明一次。
对同一个变量进行重复声明会触发 error：
:::
##### 变量赋值
对massage变量**赋值**`message = 'Hello'`
##### 变量访问
**访问**massage变量`alert(massage)`

#### 2.4.2 变量命名
##### 变量命名限制
1. 变量名称必须仅包含字母、数字、符号 `$` 和 `_`
2. 首字符必须非数字

如果命名包括多个单词，通常采用驼峰式命名法（camelCase）
js中变量名区分大小写
::: danger 保留字
js中存在保留字无法用作变量命名
:::
::: danger
未采用`use strict`时可以通过直接赋值的方式使程序自动声明变量
但严格模式下则会报错
:::

#### 2.4.3 常量
声明一个常数（不变）变量，通常使用 `const` 而非 `let`
使用 `const` 声明的变量称为“常量”。它们不能被修改，如果你尝试修改就会发现报错
##### 大写形式的常数
一般代码执行前就知晓且不变的数据用大写形式的常量存储，在代码执行过程中得到的不变的数据用普通常量存储

#### 2.4.4 总结
我们可以使用 var、let 或 const 声明变量来存储数据。
* `let` — 现代的变量声明方式。
* `var` — 老旧的变量声明方式。一般情况下，我们不会再使用它。但是，我们会在 老旧的 "var" 章节介绍 var 和 let 的微妙差别，以防你需要它们。
* `const` — 类似于 let，但是变量的值无法被修改。
变量应当以一种容易理解变量内部是什么的方式进行命名

### 2.5 数据类型
#### 2.5.1 动态类型
JavaScript 中的值都具有特定的类型
在 JavaScript 中有 8 种基本的数据类型（译注：7 种原始类型和 1 种引用类型）
JavaScript是<mark>动态类型</mark>（dynamically typed）的编程语言，虽然编程语言中有不同的数据类型，但是你定义的变量并不会在定义后，被限制为某一数据类型

#### 2.5.2 Number
number 类型代表整数和浮点数
数字可以有很多操作，比如，乘法 `*`、除法 `/`、加法 `+`、减法 `-` 等等。
除了常规的数字，还包括所谓的“特殊数值（“special numeric values”）”也属于这种类型：`Infinity`、`-Infinity` 和 `NaN`
##### `Infinity`
Infinity 代表数学概念中的 无穷大 ∞。是一个比任何数字都大的特殊值
我们可以通过除以 0 来得到它
或者在代码中直接使用它
##### `NaN`
NaN 代表一个计算错误。它是一个不正确的或者一个未定义的数学操作所得到的结果
NaN 是粘性的。任何对 NaN 的进一步数学运算都会返回 NaN
::: danger NaN数学运算的例外
`NaN ** 0` 结果为 1
:::
::: tip
在 JavaScript 中做数学运算是安全的。我们可以做任何事：除以 0，将非数字字符串视为数字，等等。

脚本永远不会因为一个致命的错误（“死亡”）而停止。最坏的情况下，我们会得到 NaN 的结果。
:::

#### 2.5.3 BigInt
"number" 类型无法表示大于 <code>(2<sup>53</sup>-1)</code>（即 `9007199254740991`），或小于 <code>-(2<sup>53</sup>-1)</code> 的整数
`BigInt` 类型是最近被添加到 JavaScript 语言中的，用于表示任意长度的整数。

可以通过将 `n` 附加到整数字段的末尾来创建 `BigInt` 值

#### 2.5.4 String
在 JavaScript 中，有三种包含字符串的方式。

1. 双引号：`"Hello"`.
2. 单引号：`'Hello'`.
3. 反引号：<code>&#96;Hello&#96;</code>.

双引号和单引号都是“简单”引用，在 JavaScript 中两者几乎没有什么差别
##### 反引号
反引号是 **功能扩展** 引号。它们允许我们通过将变量和表达式包装在 `${…}` 中，来将它们嵌入到字符串中
```js
let name = "John";
// 嵌入一个变量
alert( `Hello, *!*${name}*/!*!` ); // Hello, John!
// 嵌入一个表达式
alert( `the result is *!*${1 + 2}*/!*` ); // the result is 3
```
`${…}` 内的表达式会被计算，计算结果会成为字符串的一部分。可以在 `${…}` 内放置任何东西：诸如名为 `name` 的变量，或者诸如 `1 + 2` 的算数表达式，或者其他一些更复杂的
::: warning
需要注意的是，这仅仅在反引号内有效，其他引号不允许这种嵌入
:::

#### 2.5.5 Boolean
boolean 类型仅包含两个值：`true` 和 `false`
布尔值也可作为比较的结果

#### 2.5.6 null值
特殊的 `null` 值不属于上述任何一种类型。
它构成了一个独立的类型，只包含 `null` 值
相比较于其他编程语言，JavaScript 中的 `null` 不是一个“对不存在的 `object` 的引用”或者 “null 指针”。
JavaScript 中的 `null` 仅仅是一个代表“无”、“空”或“值未知”的特殊值

#### 2.5.7 undefined值
特殊值 `undefined` 和 `null` 一样自成类型

`undefined` 的含义是 `未被赋值`

如果一个变量已被声明，但未被赋值，那么它的值就是 `undefined`
::: warning
从技术上讲，可以显式地将 `undefined` 赋值给变量
但是不建议这样做。通常，使用 `null` 将一个“空”或者“未知”的值写入变量中，而 `undefined` 则保留作为未进行初始化的事物的默认初始值
:::

#### 2.5.8 Object
`object` 类型是一个特殊的类型，其他所有的数据类型都被称为“原始类型”，因为它们的值只包含一个单独的内容（字符串、数字或者其他）。相反，`object` 则用于储存数据集合和更复杂的实体

#### 2.5.9 Symbol
`symbol` 类型用于创建对象的唯一标识符

#### 2.5.10 typeof 运算符
`typeof` 运算符返回参数的类型
```js{7,8}
typeof undefined // "undefined"
typeof 0 // "number"
typeof 10n // "bigint"
typeof true // "boolean"
typeof "foo" // "string"
typeof Symbol("id") // "symbol"
typeof Math // "object"  (1)
typeof null // "object"  (2)
typeof alert // "function"  (3)
```
::: warning typeof null
`typeof null` 的结果为 `"object"`。这是官方承认的 `typeof` 的错误，这个问题来自于 JavaScript 语言的早期阶段，并为了兼容性而保留了下来。`null` 绝对不是一个 `object`。`null` 有自己的类型，它是一个特殊值。`typeof` 的行为在这里是错误的。
:::
::: warning function
`typeof alert` 的结果是 `"function"`，因为 `alert` 在 JavaScript 语言中是一个函数。我们会在下一章学习函数，那时我们会了解到，在 JavaScript 语言中没有一个特别的 "function" 类型。函数隶属于 `object` 类型。但是 `typeof` 会对函数区分对待，并返回 `"function"`。这也是来自于 JavaScript 语言早期的问题。从技术上讲，这种行为是不正确的，但在实际编程中却非常方便
:::
::: tip `typeof(x)` 语法
你可能还会遇到另一种语法：`typeof(x)`。它与 `typeof x` 相同。
简单点说：`typeof` 是一个操作符，不是一个函数。这里的括号不是 `typeof` 的一部分。它是数学运算分组的括号。
通常，这样的括号里包含的是一个数学表达式，例如 `(2 + 2)`，但这里它只包含一个参数 `(x)`。从语法上讲，它们允许在 `typeof` 运算符和其参数之间不打空格，有些人喜欢这样的风格。
有些人更喜欢用 `typeof(x)`，尽管 `typeof x` 语法更为常见
:::

#### 2.5.11 总结
JavaScript 中有八种基本的数据类型（译注：前七种为基本数据类型，也称为原始类型，而 `object` 为复杂数据类型）。

- `number` 用于任何类型的数字：整数或浮点数，在 <code>±(2<sup>53</sup>-1)</code> 范围内的整数。
- `bigint` 用于任意长度的整数。
- `string` 用于字符串：一个字符串可以包含 0 个或多个字符，所以没有单独的单字符类型。
- `boolean` 用于 `true` 和 `false`。
- `null` 用于未知的值 —— 只有一个 `null` 值的独立类型。
- `undefined` 用于未定义的值 —— 只有一个 `undefined` 值的独立类型。
- `symbol` 用于唯一的标识符。
- `object` 用于更复杂的数据结构。

我们可以通过 `typeof` 运算符查看存储在变量中的数据类型。

- 通常用作 `typeof x`，但 `typeof(x)` 也可行。
- 以字符串的形式返回类型名称，例如 `"string"`。
- `typeof null` 会返回 `"object"` —— 这是 JavaScript 编程语言的一个错误，实际上它并不是一个 `object`


### 2.6 交互
#### 2.6.1 alert
浏览器中显示一条信息，并等待用户按下”OK”
弹出的这个带有信息的小窗口被称为 **模态窗**。"modal" 意味着用户不能与页面的其他部分（例如点击其他按钮等）进行交互，直到他们处理完窗口。在上面示例这种情况下 —— 直到用户点击“确定”按钮。

#### 2.6.2 prompt
`prompt` 函数接收两个参数：

```js
result = prompt(title, [default]);
```

浏览器会显示一个带有文本消息的模态窗口，还有 input 框和确定/取消按钮。
访问者可以在提示输入栏中输入一些内容，然后按“确定”键。然后我们在 `result` 中获取该文本。或者他们可以按取消键或按 `key:Esc` 键取消输入，然后我们得到 `null` 作为 `result`。
`prompt` 将返回用户在 `input` 框内输入的文本，如果用户取消了输入，则返回 `null`
##### title
显示给用户的文本
##### default
可选的第二个参数，指定 input 框的初始值

#### 2.6.2 confirm
```js
result = confirm(question);
```
`confirm` 函数显示一个带有 `question` 以及确定和取消两个按钮的模态窗口。

点击确定返回 `true`，点击取消返回 `false`

#### 2.6.3 总结
我们学习了与用户交互的 3 个浏览器的特定函数：

`alert`
: 显示信息。

`prompt`
: 显示信息要求用户输入文本。点击确定返回文本，点击取消或按下 `key:Esc` 键返回 `null`。

`confirm`
: 显示信息等待用户点击确定或取消。点击确定返回 `true`，点击取消或按下 `key:Esc` 键返回 `false`。

这些方法都是模态的：它们暂停脚本的执行，并且不允许用户与该页面的其余部分进行交互，直到窗口被解除。

上述所有方法共有两个限制：

1. 模态窗口的确切位置由浏览器决定。通常在页面中心。
2. 窗口的确切外观也取决于浏览器。我们不能修改它。


## 3 JavaScript基础语法

### 3.1 类型转换
大多数情况下，运算符和函数会自动将赋予它们的值转换为正确的类型。

比如，`alert` 会自动将任何值都转换为字符串以进行显示。算术运算符会将值转换为数字

#### 3.1.1 字符串转换
`alert(value)` 将 `value` 转换为字符串类型，然后显示这个值
我们也可以显式地调用 `String(value)` 来将 `value` 转换为字符串类型
```js{2,3}
let value = true;
alert(typeof value); // boolean
value = String(value); // 现在，值是一个字符串形式的 "true"
alert(typeof value); // string
```

#### 3.1.2 数字型转换
在算术函数和表达式中，会自动进行 number 类型转换
```js
alert( "6" / "2" ); // 3, string 类型的值被自动转换成 number 类型后进行计算
```
我们也可以使用 `Number(value)` 显式地将这个 `value` 转换为 number 类型
```js
let str = "123";
alert(typeof str); // string
let num = Number(str); // 变成 number 类型 123
alert(typeof num); // number
```
number 类型转换规则：

| 值                                   | 变成……                                                                                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `undefined`                          | `NaN`                                                                                                                                                   |
| `null`                               | `0`                                                                                                                                                     |
| <code>true&nbsp;和&nbsp;false</code> | `1` and `0`                                                                                                                                             |
| `string`                             | 去掉首尾空格后的纯数字字符串中含有的数字。如果剩余字符串为空，则转换结果为 `0`。否则，将会从剩余字符串中“读取”数字。当类型转换出现 error 时返回 `NaN`。 |

```js
alert( Number("   123   ") ); // 123
alert( Number("123z") );      // NaN（从字符串“读取”数字，读到 "z" 时出现错误）
alert( Number(true) );        // 1
alert( Number(false) );       // 0
```
::: warning
请注意 `null` 和 `undefined` 在这有点不同：`null` 变成数字 `0`，`undefined` 变成 `NaN`
:::

#### 3.1.3 布尔型转换
它发生在逻辑运算中（稍后我们将进行条件判断和其他类似的东西），但是也可以通过调用 Boolean(value) 显式地进行转换
| 值                                    | 变成……  |
| ------------------------------------- | ------- |
| `0`, `null`, `undefined`, `NaN`, `""` | `false` |
| 其他值                                | `true`  |
```js
alert( Boolean(1) ); // true
alert( Boolean(0) ); // false
alert( Boolean("hello") ); // true
alert( Boolean("") ); // false
```
::: warning
包含 0 的字符串 `\"0\"` 是 `true`"
:::

#### 3.1.4 总结
有三种常用的类型转换：转换为 string 类型、转换为 number 类型和转换为 boolean 类型。

**字符串转换** —— 转换发生在输出内容的时候，也可以通过 `String(value)` 进行显式转换。原始类型值的 string 类型转换通常是很明显的。

**数字型转换** —— 转换发生在进行算术操作时，也可以通过 `Number(value)` 进行显式转换
**布尔型转换** —— 转换发生在进行逻辑操作时，也可以通过 `Boolean(value)` 进行显式转换
上述的大多数规则都容易理解和记忆。人们通常会犯错误的值得注意的例子有以下几个：

- 对 `undefined` 进行数字型转换时，输出结果为 `NaN`，而非 `0`。
- 对 `"0"` 和只有空格的字符串（比如：`"   "`）进行布尔型转换时，输出结果为 `true`

### 3.2 基础运算符
#### 3.2.1 运算符相关术语
##### 运算元
运算符应用的对象。比如说乘法运算 `5 * 2`，有两个运算元：左运算元 `5` 和右运算元 `2`。有时候人们也称其为“参数”而不是“运算元”
##### 一元运算符
如果一个运算符对应的只有一个运算元，那么它是 **一元运算符**
```js
let x = 1;
x = -x;
alert( x ); // -1，一元负号运算符生效
```
##### 二元运算符
如果一个运算符拥有两个运算元，那么它是 **二元运算符**
```js
let x = 1, y = 3;
alert( y - x ); // 2，二元运算符减号做减运算
```

#### 3.2.2 数学运算符
支持以下数学运算：

- 加法 `+`,
- 减法 `-`,
- 乘法 `*`,
- 除法 `/`,
- 取余 `%`,
- 求幂 `**`.

##### 取余 %
`a % b` 的结果是 `a` 整除 `b` 的 余数
```js
alert( 5 % 2 ); // 1，5 除以 2 的余数
alert( 8 % 3 ); // 2，8 除以 3 的余数
```
##### 求幂 **
求幂运算 `a ** b` 将 `a` 提升至 `a` 的 `b` 次幂
```js 
alert( 2 ** 2 ); // 2² = 4
alert( 2 ** 3 ); // 2³ = 8
alert( 2 ** 4 ); // 2⁴ = 16
```

#### 3.2.3  用二元运算符 + 连接字符串
通常，加号 `+` 用于求和。

但是如果加号 `+` 被应用于字符串，它将合并（连接）各个字符串：

```js
let s = "my" + "string";
alert(s); // mystring
```

注意：只要任意一个运算元是字符串，那么另一个运算元也将被转化为字符串。

举个例子：

```js 
alert( '1' + 2 ); // "12"
alert( 2 + '1' ); // "21"
```
```js
alert(2 + 2 + '1' ); // "41"，不是 "221"
```

在这里，运算符是按顺序工作。第一个 `+` 将两个数字相加，所以返回 `4`，然后下一个 `+` 将字符串 `1` 加入其中，所以就是 `4 + '1' = '41'`。

```js
alert('1' + 2 + 2); // "122"，不是 "14"
```
这里，第一个操作数是一个字符串，所以编译器将其他两个操作数也视为了字符串。`2` 被与 `'1'` 连接到了一起，也就是像 `'1' + 2 = "12"` 然后 `"12" + 2 = "122"` 这样。

二元 `+` 是唯一一个以这种方式支持字符串的运算符。其他算术运算符只对数字起作用，并且总是将其运算元转换为数字。

下面是减法和除法运算的示例：

```js
alert( 6 - '2' ); // 4，将 '2' 转换为数字
alert( '6' / '2' ); // 3，将两个运算元都转换为数字
```

#### 3.2.4 数字转化，一元运算符 +
加号 `+` 有两种形式。一种是上面我们刚刚讨论的二元运算符，还有一种是一元运算符。

一元运算符加号，或者说，加号 `+` 应用于单个值，对数字没有任何作用。但是如果运算元不是数字，加号 `+` 则会将其转化为数字。

例如：

```js{6,7}
// 对数字无效
let x = 1;
alert( +x ); // 1
let y = -2;
alert( +y ); // -2
// 转化非数字
alert( +true ); // 1
alert( +"" );   // 0
```

它的效果和 `Number(...)` 相同，但是更加简短

#### 3.2.5 运算符优先级
这是一个摘抄自 Mozilla 的 [优先级表](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence)（你没有必要把这全记住，但要记住一元运算符优先级高于二元运算符）：

| 优先级 | 名称     | 符号 |
| ------ | -------- | ---- |
| ...    | ...      | ...  |
| 15     | 一元加号 | `+`  |
| 15     | 一元负号 | `-`  |
| 14     | 求幂     | `**` |
| 13     | 乘号     | `*`  |
| 13     | 除号     | `/`  |
| 12     | 加号     | `+`  |
| 12     | 减号     | `-`  |
| ...    | ...      | ...  |
| 2      | 赋值符   | `=`  |
| ...    | ...      | ...  |

我们可以看到，“一元加号运算符”的优先级是 `15`，高于“二元加号运算符”的优先级 `12`。这也是为什么表达式 `"+apples + +oranges"` 中的一元加号先生效，然后才是二元加法

#### 3.2.6 赋值运算符
赋值符号 `=` 也是一个运算符。从优先级表中可以看到它的优先级非常低，只有 `2`。
所以当我们赋值时，比如 `x = 2 * 2 + 1`，所有的计算先执行，然后 `=` 才执行，将计算结果存储到 `x`
#####  赋值 = 返回一个值
在 JavaScript 中，所有运算符都会返回一个值。这对于 `+` 和 `-` 来说是显而易见的，但对于 `=` 来说也是如此
语句 `x = value` 将值 `value` 写入 `x` **然后返回 value**。

下面是一个在复杂语句中使用赋值的例子：

```js {2}
let a = 1;
let b = 2;
let c = 3 - (a = b + 1);
alert( a ); // 3
alert( c ); // 0
```

上面这个例子，`(a = b + 1)` 的结果是赋给 `a` 的值（也就是 `3`）。然后该值被用于进一步的运算
##### 链式赋值（Chaining assignments）
```js
let a, b, c;
a = b = c = 2 + 2;
alert( a ); // 4
alert( b ); // 4
alert( c ); // 4
```
链式赋值从右到左进行计算。首先，对最右边的表达式 `2 + 2` 求值，然后将其赋给左边的变量：`c`、`b` 和 `a`。最后，所有的变量共享一个值

#### 3.2.7 原地修改
我们经常需要对一个变量做运算，并将新的结果存储在同一个变量中
可以使用运算符 `+=` 和 `*=` 来缩写这种表示，所有算术和位运算符都有简短的“修改并赋值”运算符
```js
let n = 2;
n += 5; // 现在 n = 7（等同于 n = n + 5）
n *= 2; // 现在 n = 14（等同于 n = n * 2）
alert( n ); // 14
```
这类运算符的优先级与普通赋值运算符的优先级相同，所以它们在大多数其他运算之后执行：

```js
let n = 2;
n *= 3 + 5;
alert( n ); // 16 （右边部分先被计算，等同于 n *= 8）
```

#### 3.2.8 自增/自减
##### 自增`++`
将变量与 1 相加
```js
let counter = 2;
counter++;      // 和 counter = counter + 1 效果一样，但是更洁
alert( counter ); // 3
```
##### 自减`--`
```js no-beautify
let counter = 2;
counter--;      // 和 counter = counter - 1 效果一样，但是更洁
alert( counter ); // 1
```
:::warning 只用于变量
自增/自减只能应用于变量。试一下，将其应用于数值（比如 `5++`）则会报错
:::
##### 前置与后置
运算符 `++` 和 `--` 可以置于变量前，也可以置于变量后。

- 当运算符置于变量后，被称为“后置形式”：`counter++`。
- 当运算符置于变量前，被称为“前置形式”：`++counter`。


```js
let counter = 1;
let a = ++counter; // (*)
alert(a); // 2
```

`(*)` 所在的行是前置形式 `++counter`，对 `counter` 做自增运算，返回的是新的值 `2`。因此 `alert` 显示的是 `2`。

下面让我们看看后置形式：

```js
let counter = 1;
let a = counter++; // (*) 将 ++counter 改为 counter++
alert(a); // 1
```

`(*)` 所在的行是后置形式 `counter++`，它同样对 `counter` 做加法，但是返回的是 **旧值**（做加法之前的值）。因此 `alert` 显示的是 `1`。
::: tip 自增/自减和其它运算符的对比
`++/--` 运算符同样可以在表达式内部使用。它们的优先级比绝大部分的算数运算符要高。
举个例子：
```js
let counter = 1;
alert( 2 * ++counter ); // 4
```
:::

#### 3.2.9 位运算符
下面是位运算符：

- 按位与 ( `&` )
- 按位或 ( `|` )
- 按位异或 ( `^` )
- 按位非 ( `~` )
- 左移 ( `<<` )
- 右移 ( `>>` )
- 无符号右移 ( `>>>` )

#### 3.2.10 逗号运算符
逗号运算符能让我们处理多个语句，使用 `,` 将它们分开。每个语句都运行了，但是只有最后的语句的结果会被返回

```js {0}
let a = (1 + 2, 3 + 4);
alert( a ); // 7（3 + 4 的结果）
```
这里，第一个语句 `1 + 2` 运行了，但是它的结果被丢弃了。随后计算 `3 + 4`，并且该计算结果被返回
::: tip 逗号运算符的优先级非常低
请注意逗号运算符的优先级非常低，比 `=` 还要低，因此上面你的例子中圆括号非常重要。
如果没有圆括号：`a = 1 + 2, 3 + 4` 会先执行 `+`，将数值相加得到 `a = 3, 7`，然后赋值运算符 `=` 执行 `a = 3`，然后逗号之后的数值 `7` 不会再执行，它被忽略掉了。相当于 `(a = 1 + 2), 3 + 4`。
:::

### 3.3 比较运算符
- 大于 / 小于：<code>a &gt; b</code>，<code>a &lt; b</code>。
- 大于等于 / 小于等于：<code>a &gt;= b</code>，<code>a &lt;= b</code>。
- 检查两个值的相等：`a == b`，请注意双等号 `==` 表示相等性检查，而单等号 `a = b` 表示赋值。
- 检查两个值不相等：不相等在数学中的符号是 <code>&ne;</code>，但在 JavaScript 中写成 <code>a != b</code>。

#### 3.3.1 比较运算符结果为Boolean 类型
所有比较运算符均返回布尔值：

- `true` —— 表示“yes（是）”，“correct（正确）”或“the truth（真）”。
- `false` ——  表示“no（否）”，“wrong（错误）”或“not the truth（非真）”。

和其他类型的值一样，比较的结果可以被赋值给任意变量
```js
let result = 5 > 4; // 把比较的结果赋值给 result
alert( result ); // true
```

#### 3.3.2 字符串比较
在比较字符串的大小时，JavaScript 会使用“字典（dictionary）”或“词典（lexicographical）”顺序进行判定，字符串是按字符（母）逐个进行比较的
```js
alert( 'Z' > 'A' ); // true
alert( 'Glow' > 'Glee' ); // true
alert( 'Bee' > 'Be' ); // true
```
字符串的比较算法非常简单：

1. 首先比较两个字符串的首位字符大小。
2. 如果一方字符较大（或较小），则该字符串大于（或小于）另一个字符串。算法结束。
3. 否则，如果两个字符串的首位字符相等，则继续取出两个字符串各自的后一位字符进行比较。
4. 重复上述步骤进行比较，直到比较完成某字符串的所有字符为止。
5. 如果两个字符串的字符同时用完，那么则判定它们相等，否则未结束（还有未比较的字符）的字符串更大

:::tip 非真正的字典顺序，而是 Unicode 编码顺序
在上面的算法中，比较大小的逻辑与字典或电话簿中的排序很像，但也不完全相同。
比如说，字符串比较对字母大小写是敏感的。大写的 `"A"` 并不等于小写的 `"a"`。哪一个更大呢？实际上小写的 `"a"` 更大。这是因为在 JavaScript 使用的内部编码表中（Unicode），小写字母的字符索引值更大
:::

#### 3.3.3 不同类型间的比较
当对不同类型的值进行比较时，JavaScript 会首先将其转化为数字（number）再判定大小
```js
alert( '2' > 1 ); // true，字符串 '2' 会被转化为数字 2
alert( '01' == 1 ); // true，字符串 '01' 会被转化为数字 1
alert( true == 1 ); // true
alert( false == 0 ); // true
```
:::tip 一个有趣的现象
有时候，以下两种情况会同时发生：
- 若直接比较两个值，其结果是相等的。
- 若把两个值转为布尔值，它们可能得出完全相反的结果，即一个是 `true`，一个是 `false`。
例如：
```js
let a = 0;
alert( Boolean(a) ); // false
let b = "0";
alert( Boolean(b) ); // true
alert(a == b); // true!
```
对于 JavaScript 而言，这种现象其实挺正常的。因为 JavaScript 会把待比较的值转化为数字后再做比较（因此 `"0"` 变成了 `0`）。若只是将一个变量转化为 `Boolean` 值，则会使用其他的类型转换规则。
:::

#### 3.3.4 严格相等
普通的相等性检查 `==` 存在一个问题，它不能区分出 `0` 和 `false`,也同样无法区分空字符串和 `false`
这是因为在比较不同类型的值时，处于相等判断符号 `==` 两侧的值会先被转化为数字。空字符串和 `false` 也是如此，转化后它们都为数字 0
**严格相等运算符 `===` 在进行比较时不会做任何的类型转换。**
```js
alert( 0 === false ); // false，因为被比较值的数据类型不同
```
同样的，与“不相等”符号 `!=` 类似，“严格不相等”表示为 `!==`

#### 3.3.5 对 null 和 undefined 进行比较
当使用严格相等 `===` 比较二者时 
: 它们不相等，因为它们属于不同的类型。

    ```js
    alert( null === undefined ); // false
    ```

当使用非严格相等 `==` 比较二者时
: JavaScript 存在一个特殊的规则，会判定它们相等。它们俩就像“一对恋人”，仅仅等于对方而不等于其他任何的值（只在非严格相等下成立）。

    ```js
    alert( null == undefined ); // true
    ```

当使用数学式或其他比较方法 `< > <= >=` 时：
: `null/undefined` 会被转化为数字：`null` 被转化为 `0`，`undefined` 被转化为 `NaN`。

##### null vs 0
```js{2}
alert( null > 0 );  // (1) false
alert( null == 0 ); // (2) false
alert( null >= 0 ); // (3) true
```
相等性检查 `==` 和普通比较符 `> < >= <=` 的代码逻辑是相互独立的
进行值的比较时，`null` 会被转化为数字，因此它被转化为了 `0`。这就是为什么（3）中 `null >= 0` 返回值是 true，（1）中 `null > 0` 返回值是 false。  
`undefined` 和 `null` 在相等性检查 `==` 中不会进行任何的类型转换，它们有自己独立的比较规则，所以除了它们之间互等外，不会等于任何其他的值。这就解释了为什么（2）中 `null == 0` 会返回 false。


##### undefined
```js
alert( undefined > 0 ); // false (1)
alert( undefined < 0 ); // false (2)
alert( undefined == 0 ); // false (3)
```
`(1)` 和 `(2)` 都返回 `false` 是因为 `undefined` 在比较中被转换为了 `NaN`，而 `NaN` 是一个特殊的数值型值，它与任何值进行比较都会返回 `false`
`(3)` 返回 `false` 是因为这是一个相等性检查，而 `undefined` 只与 `null` 相等，不会与其他值相等


### 3.4 条件分支
#### 3.4.1 "if" 语句
`if(...)` 语句计算括号里的条件表达式，如果计算结果是 `true`，就会执行对应的代码块
```js
if (year == 2015) {
  alert( "That's correct!" );
  alert( "You're so smart!" );
}
```

#### 3.4.2 布尔转换
`if (…)` 语句会计算圆括号内的表达式，并将计算结果转换为布尔型

#### 3.4.3 "else" 语句
`if` 语句有时会包含一个可选的 "else" 块。如果判断条件不成立，就会执行它内部的代码

#### 3.4.4 多个条件："else if"
有时我们需要测试一个条件的几个变体。我们可以通过使用 `else if` 子句实现
```js
let year = prompt('In which year was ECMAScript-2015 specification published?', '');
if (year < 2015) {
  alert( 'Too early...' );
} else if (year > 2015) {
  alert( 'Too late' );
} else {
  alert( 'Exactly!' );
}
```
可以有更多的 `else if` 块。结尾的 `else` 是可选的

#### 3.4.5 条件运算符 '?'
问号 `?` 有时它被称为三元运算符，被称为“三元”是因为该运算符中有三个操作数
```js
let result = condition ? value1 : value2;
```
计算条件结果，如果结果为真，则返回 `value1`，否则返回 `value2`

#### 3.4.6 多个 '?'
使用一系列问号 `?` 运算符可以返回一个取决于多个条件的值
```js
let age = prompt('age?', 18);
let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';
alert( message );
```
1. 第一个问号检查 `age < 3`。
2. 如果为真 — 返回 `'Hi, baby!'`。否则，会继续执行冒号 `":"` 后的表达式，检查 `age < 18`。
3. 如果为真 — 返回 `'Hello!'`。否则，会继续执行下一个冒号 `":"` 后的表达式，检查 `age < 100`。
4. 如果为真 — 返回 `'Greetings!'`。否则，会继续执行最后一个冒号 `":"` 后面的表达式，返回 `'What an unusual age!'`

#### 3.4.6 '?' 的非常规使用
有时可以使用问号 `?` 来代替 `if` 语句
```js no-beautify
let company = prompt('Which company created JavaScript?', '');
(company == 'Netscape') ?
   alert('Right!') : alert('Wrong.');
```
根据条件 `company =='Netscape'`，要么执行 `?` 后面的第一个表达式并显示对应内容，要么执行第二个表达式并显示对应内容
**不建议这样使用问号运算符。**

### 3.5 逻辑运算符
JavaScript 中有四个逻辑运算符：`||`（或），`&&`（与），`!`（非），`??`（空值合并运算符）
虽然它们被称为“逻辑”运算符，但这些运算符却可以被应用于任意类型的值，而不仅仅是布尔值。它们的结果也同样可以是任意类型

#### 3.5.1 ||（或）
两个竖线符号表示“或”运算符：

```js
result = a || b;
```
```js
alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false
```
如果操作数不是布尔值，那么它将会被转化为布尔值来参与运算
##### 或运算寻找第一个真值
给定多个参与或运算的值：

```js
result = value1 || value2 || value3;
```

或运算符 `||` 做了如下的事情：

- 从左到右依次计算操作数。
- 处理每一个操作数时，都将其转化为布尔值。如果结果是 `true`，就停止计算，返回这个操作数的初始值。
- 如果所有的操作数都被计算过（也就是，转换结果都是 `false`），则返回最后一个操作数。

返回的值是操作数的初始形式，不会做布尔转换。

换句话说，一个或运算 `||` 的链，将返回第一个真值，如果不存在真值，就返回该链的最后一个值
```js
alert( 1 || 0 ); // 1（1 是真值）
alert( null || 1 ); // 1（1 是第一个真值）
alert( null || 0 || 1 ); // 1（第一个真值）
alert( undefined || null || 0 ); // 0（都是假值，返回最后一个值）
```
1. **获取变量列表或者表达式中的第一个真值**
    我们用或运算 `||` 来选择有数据的那一个，并显示出来（如果没有设置，则用 `"Anonymous"`）：

    ```js{3}
    let firstName = "";
    let lastName = "";
    let nickName = "SuperCoder";
    alert( firstName || lastName || nickName || "Anonymous"); // SuperCoder
    ```
2. **短路求值（Short-circuit evaluation）**
    `||` 对其参数进行处理，直到达到第一个真值，然后立即返回该值，而无需处理其他参数
    ```js
    true || alert("not printed");
    false || alert("printed");
    ```
    在第一行中，或运算符 `||` 在遇到 `true` 时立即停止运算，所以 `alert` 没有运行

#### 3.5.2 &&（与）
两个 & 符号表示 `&&` 与运算符
```js
result = a && b;
```
在传统的编程中，当两个操作数都是真值时，与运算返回 `true`，否则返回 `false`：

```js
alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false
```
就像或运算一样，与运算的操作数可以是任意类型的值：

```js
if (1 && 0) { // 作为 true && false 来执行
  alert( "won't work, because the result is falsy" );
}
```
##### 与运算寻找第一个假值
```js
result = value1 && value2 && value3;
```
与运算 `&&` 做了如下的事：

- 从左到右依次计算操作数。
- 在处理每一个操作数时，都将其转化为布尔值。如果结果是 `false`，就停止计算，并返回这个操作数的初始值。
- 如果所有的操作数都被计算过（例如都是真值），则返回最后一个操作数。

换句话说，与运算返回第一个假值，如果没有假值就返回最后一个值
```js
// 如果第一个操作数是真值，
// 与运算返回第二个操作数：
alert( 1 && 0 ); // 0
alert( 1 && 5 ); // 5
// 如果第一个操作数是假值，
// 与运算将直接返回它。第二个操作数会被忽略
alert( null && 5 ); // null
alert( 0 && "no matter what" ); // 0

alert( 1 && 2 && null && 3 ); // null
//如果所有的值都是真值，最后一个值将会被返回
alert( 1 && 2 && 3 ); // 3，最后一个值
```
::: tip 与运算 `&&` 在或运算 `||` 之前进行
与运算 `&&` 的优先级比或运算 `||` 要高。
所以代码 `a && b || c && d` 跟 `&&` 表达式加了括号完全一样：`(a && b) || (c && d)`
:::
::: warning
不要用 `||` 或 `&&` 来取代 `if`
:::

#### 3.5.3 !（非）
感叹符号 `!` 表示布尔非运算符
```js
result = !value;
```
逻辑非运算符接受一个参数，并按如下运作：

1. 将操作数转化为布尔类型：`true/false`。
2. 返回相反的值

```js
alert( !true ); // false
alert( !0 ); // true
```
非运算符 `!` 的<mark>优先级</mark>在所有逻辑运算符里面<mark>最高</mark>，所以它总是在 `&&` 和 `||` 之前执行

##### `!!`
两个非运算 `!!` 有时候用来将某个值转化为布尔类型

#### 3.5.4 空值合并运算符 '??'
空值合并运算符（nullish coalescing operator）的写法为两个问号 `??`
由于它对待 `null` 和 `undefined` 的方式类似，所以在本文中我们将使用一个特殊的术语对其进行表示。为简洁起见，当一个值既不是 `null` 也不是 `undefined` 时，我们将其称为“已定义的（defined）”

`a ?? b` 的结果是：
- 如果 `a` 是已定义的，则结果为 `a`，
- 如果 `a` 不是已定义的，则结果为 `b`

```js
let user;
alert(user ?? "匿名"); // 匿名（user 未定义）
```
```js
let user = "John";
alert(user ?? "匿名"); // John（user 已定义）
```

我们还可以使用 `??` 序列从一系列的值中选择出第一个非 `null/undefined` 的值
```js
let firstName = null;
let lastName = null;
let nickName = "Supercoder";
// 显示第一个已定义的值：
alert(firstName ?? lastName ?? nickName ?? "匿名"); // Supercoder
```

##### 与 || 比较
或运算符 `||` 可以以与 `??` 运算符相同的方式使用

它们之间重要的区别是：
- `||` 返回第一个 **真** 值。
- `??` 返回第一个 **已定义的** 值

##### 优先级
`??` 运算符的优先级与 `||` 相同，它们的的优先级都为 `4`
##### ?? 与 && 或 || 一起使用
出于安全原因，JavaScript 禁止将 `??` 运算符与 `&&` 和 `||` 运算符一起使用，除非使用括号明确指定了优先级




### 3.6 循环
#### 3.6.1 while循环
`while` 循环的语法如下：当 `condition` 为真时，执行循环体的 `code`。
```js
while (condition) {
  // 代码
  // 所谓的“循环体” 
}
```
在 `while` 中的循环条件会被计算，计算结果会被转化为布尔值。
单行循环体不需要大括号"，如果循环体只有一条语句，则可以省略大括号 `{…}`：
```js
let i = 3;
while (i) alert(i--);
```

#### 3.6.2 do...while循环
使用 `do..while` 语法可以将条件检查移至循环体 **下面**：

```js
do {
  // 循环体
} while (condition);
```
循环首先执行循环体，然后检查条件，当条件为真时，重复执行循环体
不管条件是否为真，循环体 **至少执行一次**

#### 3.6.3 for循环
```js
for (begin; condition; step) {
  // ……循环体……
}
```
| 语句段         |             |                                                  |
| -------------- | ----------- | ------------------------------------------------ |
| begin          | `let i = 0` | 进入循环时执行一次。                             |
| condition      | `i < 3`     | 在每次循环迭代之前检查，如果为 false，停止循环。 |
| body（循环体） | `alert(i)`  | 条件为真时，重复运行。                           |
| step           | `i++`       | 在每次循环体迭代后执行。                         |
##### 内联变量声明
“计数”变量 `i` 是在循环中声明的。这叫做“内联”变量声明。这样的变量只在循环中可见。
```js
for (let i = 0; i < 3; i++) {
  alert(i); // 0, 1, 2
}
alert(i); // 错误，没有这个变量。
```
##### 省略语句段
`for` 循环的任何语句段都可以被省略
```js
let i = 0; // 我们已经声明了 i 并对它进行了赋值
for (; i < 3; i++) { // 不再需要 "begin" 语句段
  alert( i ); // 0, 1, 2
}
```
::: warning
请注意 for 的两个 `;` 必须存在，否则会出现语法错误
:::

#### 3.6.4 break
循环中随时都可以使用 break 指令强制退出
```js
let sum = 0;
while (true) {
  let value = +prompt("Enter a number", '');
  if (!value) break; 
  sum += value;
}
alert( 'Sum: ' + sum );
```
根据需要，"无限循环 + `break`" 的组合非常适用于不必在循环开始/结束时检查条件，但需要在中间甚至是主体的多个位置进行条件检查的情况。

#### 3.6.5 continue
`continue` 指令是 `break` 的“轻量版”。它不会停掉整个循环。而是停止当前这一次迭代，并强制启动新一轮循环（如果条件允许的话）
```js
for (let i = 0; i < 10; i++) {
  //如果为真，跳过循环体的剩余部分。
  if (i % 2 == 0) continue;
  alert(i); // 1，然后 3，5，7，9
}
```
:::danger 禁止 `break/continue` 在 ‘?’ 的右边
请注意非表达式的语法结构不能与三元运算符 `?` 一起使用。特别是 `break/continue` 这样的指令是不允许这样使用的
```js no-beautify
(i > 5) ? alert(i) : continue; // continue 不允许在这个位置,代码会停止运行，并显示有语法错误
```
:::

#### 3.6.6 break/continue 标签
使用标签可以一次从多层嵌套的循环中跳出来
**标签** 是在循环之前带有冒号的标识符：
```js
labelName: for (...) {
  ...
}
```
`break <labelName>` 语句跳出循环至标签处：

```js
outer:for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    let input = prompt(`Value at coords (${i},${j})`, '');
    // 如果是空字符串或被取消，则中断并跳出这两个循环。
    if (!input) break outer; // (*)
    // 用得到的值做些事……
  }
}
alert('Done!');
```
::: warning 标签并不允许“跳到”所有位置
`break` 指令必须在代码块内。从技术上讲，任何被标记的代码块都有效，例如：
```js
label: {
  // ...
  break label; // 有效
  // ...
}
```
`continue` 只有在循环内部才可行
:::

### 3.7 switch
`switch` 语句可以替代多个 `if` 判断

#### 3.7.1 switch语法
`switch` 语句有至少一个 `case` 代码块和一个可选的 `default` 代码块。
```js
switch(x) {
  case 'value1':  // if (x === 'value1')
    ...
    [break]
  case 'value2':  // if (x === 'value2')
    ...
    [break]
  default:
    ...
    [break]
}
```

- 比较 `x` 值与第一个 `case`（也就是 `value1`）是否严格相等，然后比较第二个 `case`（`value2`）以此类推
- 如果相等，`switch` 语句就执行相应 `case` 下的代码块，直到遇到最靠近的 `break` 语句（或者直到 `switch` 语句末尾）
- 如果没有符合的 case，则执行 `default` 代码块（如果 `default` 存在）

::: tip 任何表达式都可以成为 `switch/case` 的参数
`switch` 和 `case` 都允许任意表达式。
```js
let a = "1";
let b = 0;
switch (+a) {
  case b + 1:
    alert("this runs, because +a is 1, exactly equals b+1");
    break;
  default:
    alert("this doesn't run");
}
```
:::

#### 3.7.2 switch中的break
```js
let a = 2 + 2;
switch (a) {
  case 3:
    alert( 'Too small' );
    break;
  case 4:
    alert( 'Exactly!' );
    break;
  case 5:
    alert( 'Too big' );
    break;
  default:
    alert( "I don't know such values" );
}//输出Exactly!
switch (a) {
  case 3:
    alert( 'Too small' );
  case 4:
    alert( 'Exactly!' );
  case 5:
    alert( 'Too big' );
  default:
    alert( "I don't know such values" );
}//输出Exactly! Too big I don't know such values
```

#### 3.7.3 case分组
共享同一段代码的几个 `case` 分支可以被分为一组
```js {8-12}
let a = 3;
switch (a) {
  case 4:
    alert('Right!');
    break;
  case 3: // (*) 下面这两个 case 被分在一组
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;
  default:
    alert('The result is strange. Really.');
}
```
`switch/case` 有通过 case 进行“分组”的能力，其实是 switch 语句没有 `break` 时的副作用。因为没有 `break`，`case 3` 会从 `(*)` 行执行到 `case 5`

#### 3.7.4 switch严格相等
switch的相等是严格相等。被比较的值必须是相同的类型才能进行匹配



### 3.8 函数
#### 3.8.1 函数声明
`function` 关键字首先出现，然后是 **函数名**，然后是括号之间的 **参数** 列表，最后是花括号之间的代码（即“函数体”）
```js
function showMessage() {
  alert( 'Hello everyone!' );
}
```
我们的新函数可以通过名称调用：`showMessage()`

#### 3.8.2 局部变量
在函数中声明的变量只在该函数内部可见
```js
function showMessage() {
  let message = "Hello, I'm JavaScript!"; // 局部变量
  alert( message );
}
showMessage(); // Hello, I'm JavaScript!
alert( message ); // <-- 错误！变量是函数的局部变量
```

#### 3.8.3 外部变量
##### 外部变量读写
函数对外部变量拥有全部的访问权限。函数可以读写外部变量
```js
let userName = 'John';
function showMessage() {
  userName = "Bob"; // (1) 改变外部变量
  let message = 'Hello, ' + *!*userName*/!*;
  alert(message);
}
alert( userName ); // *!*John*/!* 在函数调用之前
showMessage();
alert( userName ); // *!*Bob*/!*，值被函数修改了
```
###### 外部变量遮蔽
只有在没有局部变量的情况下才会使用外部变量。如果在函数内部声明了同名变量，那么函数会 **遮蔽** 外部变量
```js
let userName = 'John';
function showMessage() {
  let userName = "Bob"; // 声明一个局部变量
  let message = 'Hello, ' + userName; // Bob
  alert(message);
}
// 函数会创建并使用它自己的 userName
showMessage();
alert( userName ); // John，未被更改，函数没有访问外部变量。
```

#### 3.8.4 参数
##### 形参与实参
我们可以通过参数将任意数据传递给函数
函数被调用的时候，给定值被复制到了局部变量的形参上，然后函数使用它们进行计算
函数执行中会修改函数内的局部变量，但不会修改传递进来的实参，因为函数修改的是复制的实参值副本
```js
function showMessage(from, text) {
  from = '*' + from + '*'; // 让 "from" 看起来更优雅
  alert( from + ': ' + text );
}
let from = "Ann";
showMessage(from, "Hello"); // *Ann*: Hello
// "from" 值相同，函数修改了一个局部的副本。
alert( from ); // Ann
```
- 形参（parameter）是函数声明中括号内列出的变量（它是函数声明时的术语）
- 实参（argument）是调用函数时传递给函数的值（它是函数调用时的术语）

##### 形参默认值
如果一个函数被调用，但有参数（argument）未被提供，那么相应的值就会变成 `undefined`
我们可以使用 `=` 为函数声明中的参数指定所谓的“默认”（如果对应参数的值未被传递则使用）值
```js
function showMessage(from, text = "no text given") {
  alert( from + ": " + text );
}
showMessage("Ann"); // Ann: no text given
```
::: tip 在 JavaScript 老代码中的默认参数
几年前，JavaScript 不支持默认参数的语法。所以人们使用其他方式来设置默认参数
显式地检查 `undefined`：
```js
function showMessage(from, text) {
  if (text === undefined) {
    text = 'no text given';
  }
  alert( from + ": " + text );
}
```
……或者使用 `||` 运算符：
```js
function showMessage(from, text) {
  // 如果 text 的值为假值，则分配默认值
  // 这样赋值 text == "" 与 text 无值相同
  text = text || 'no text given';
  ...
}
```
:::

#### 3.8.5 返回值
函数可以将一个值返回到调用代码中作为结果
指令 `return` 可以在函数的任意位置。当执行到达时，函数停止，并将值返回给调用代码（分配给上述代码中的 `result`）
只使用 `return` 但没有返回值也是可行的。但这会导致函数立即退出
::: tip 空值的 `return` 或没有 `return` 的函数返回值为 `undefined`
```js
function doNothing1() { /* 没有代码 */ }
alert( doNothing1() === undefined ); // true
function doNothing2() {
  return;
}
alert( doNothing2() === undefined ); // true
```
:::
::: warning 不要在 `return` 与返回值之间添加新行
JavaScript 默认会在 `return` 之后加上分号，如果添加空行就会导致返回值变成空值
```js
return
  (some + long + expression + or + whatever * f(a) + f(b))
// 等价于
return;
 (some + long + expression + or + whatever * f(a) + f(b))
```
如果我们想要将返回的表达式写成跨多行的形式，那么应该在 `return` 的同一行开始写此表达式
```js
return (
  some + long + expression
  + or +
  whatever * f(a) + f(b)
  )
```
:::

#### 3.8.6 函数表达式
**函数表达式**是一种创建函数的语法，它允许我们在任何表达式的中间创建一个新函数
```js
let sayHi = function() {
  alert( "Hello" );
};
```
由于函数创建发生在赋值表达式的上下文中（在 `=` 的右侧），因此这是一个 **函数表达式**。

请注意，`function` 关键字后面没有函数名。函数表达式允许省略函数名


##### 函数是一个值
无论函数是如何创建的，函数都是一个值
我们还可以用 `alert` 打印这个变量的值：

```js
function sayHi() {
  alert( "Hello" );
}
alert( sayHi ); // 显示函数代码
```
最后一行代码并不会运行函数，因为 `sayHi` 后没有括号
在 JavaScript 中，函数是一个值，所以我们可以把它当成值对待。上面代码显示了一段字符串值，即函数的源码

##### 函数声明vs函数表达式
**函数表达式是在代码执行到达时被创建，并且仅从那一刻起可用**
**在函数声明被定义之前，它就可以被调用**
**严格模式下，当一个函数声明在一个代码块内时，它在该代码块内的任何位置都是可见的。但在代码块外不可见。**


#### 3.8.7 回调函数
在一个函数中将其他的函数当做参数传入，被传入的函数就是被称为 **回调函数** 或简称 **回调**
:::tip 一个函数是表示一个“行为”的值
字符串或数字等常规值代表 **数据**。
函数可以被视为一个 **行为（action）**。
我们可以在变量之间传递它们，并在需要时运行。
:::

#### 3.8.8 箭头函数
创建了一个函数 `func`，它接受参数 `arg1..argN`，然后使用参数对右侧的 `expression` 求值并返回其结果。
```js
let func = (arg1, arg2, ..., argN) => expression;
```

```js
let sum = (a, b) => a + b;
/* 这个箭头函数是下面这个函数的更短的版本：
let sum = function(a, b) {
  return a + b;
};
*/
alert( sum(1, 2) ); // 3
```
- 如果我们只有一个参数，还可以省略掉参数外的圆括号，使代码更短。

    ```js
    let double = n => n * 2;
    // 差不多等同于：let double = function(n) { return n * 2 }
    alert( double(3) ); // 6
    ```

- 如果没有参数，括号则是空的（但括号必须保留）：

    ```js
    let sayHi = () => alert("Hello!");
    sayHi();
    ```
##### 多行箭头函数
我们可以使用花括号将它们括起来。主要区别在于，用花括号括起来之后，需要包含 `return` 才能返回值（就像常规函数一样）
```js
let sum = (a, b) => {  // 花括号表示开始一个多行函数
  let result = a + b;
  return result; // 如果我们使用了花括号，那么我们需要一个显式的 “return”
};
alert( sum(1, 2) ); // 3
```





## 4 Object对象

### 4.1 对象基础
#### 4.1.1 创建对象
我们可以用下面两种语法，构造函数或**字面量**中的任一种来创建一个空的对象
```js
let user = new Object(); // “构造函数” 的语法
let user = {};  // “字面量” 的语法
```

#### 4.1.2 键值对
我们可以在创建对象的时候，立即将一些属性以键值对的形式放到 `{...}` 中
```js
let user = {     // 一个对象
  name: "John",  // 键 "name"，值 "John"
  age: 30        // 键 "age"，值 30
};
```
属性有键（或者也可以叫做“名字”或“标识符”），位于冒号 `":"` 的前面，值在冒号的右边
可以随时添加、删除和读取属性值
##### 点符号访问属性值
```js
// 读取文件的属性：
alert( user.name ); // John
alert( user.age ); // 30
```
#####  `delete` 操作符移除属性
```js
delete user.age;
```
##### 多词属性
多字词语来作为属性名，但必须给它们加上引号
```js
let user = {
  name: "John",
  age: 30,
  "likes birds": true  // 多词属性名必须加引号
};
```
#### 4.1.3 []
##### 多词属性
多词属性，点操作就不能用
```js
// 这将提示有语法错误
user.likes birds = true
```
点符号要求 `key` 是有效的变量标识符。这意味着：不包含空格，不以数字开头，也不包含特殊字符（允许使用 `$` 和 `_`）
```js
let user = {};
// 设置
user["likes birds"] = true;
// 读取
alert(user["likes birds"]); // true
// 删除
delete user["likes birds"];
```
请注意方括号中的字符串要放在**引号**中，单引号或双引号都可以
##### 变量 `key`由表达式得到
```js
let user = {
  name: "John",
  age: 30
};
let key = prompt("What do you want to know about the user?", "name");
// 访问变量
alert( user[key] ); // John（如果输入 "name"）
let key = "name";
alert( user.key ) // undefined
```

#### 4.1.4 计算属性
当创建一个对象时，我们可以在对象字面量中使用方括号。这叫做 **计算属性**
```js {4}
let fruit = prompt("Which fruit to buy?", "apple");
let bag = {
  [fruit]: 5, // 属性名是从 fruit 变量中得到的
};
alert( bag.apple ); // 5 如果 fruit="apple"
```

#### 4.1.5 属性值简写
属性名跟变量名一样。这种通过变量生成属性的应用场景很常见，在这有一种特殊的 **属性值缩写** 方法，使属性名变得更短
```js {3,4}
function makeUser(name, age) {
  return {
    name, // 与 name: name 相同
    age,  // 与 age: age 相同
    // ...
  };
}
```

#### 4.1.6 属性名称限制
变量名不能是编程语言的某个保留字，如 "for"、"let"、"return" 等，但对象的属性名并<mark>不受此限制</mark>
属性名可以是任何字符串或者 symbol。
其他类型会被自动地转换为字符串

#### 4.1.7  属性存在性测试，"in" 操作符
JavaScript 的对象有一个需要注意的特性：能够被访问任何属性。即使属性不存在也不会报错！
读取不存在的属性只会得到 `undefined`
检查属性是否存在的操作符 `"in"`  
```js
"key" in object
```
::: warning
请注意，`in` 的左边必须是 **属性名**。通常是一个带引号的字符串
如果我们省略引号，就意味着左边是一个变量，它应该包含要判断的实际属性名
:::

属性存在，但存储的值是 `undefined` 的时候，使用`undefined`判断属性存在与否会有问题：
```js
let obj = {
  test: undefined
};
alert( obj.test ); // 显示 undefined，所以属性不存在？
alert( "test" in obj ); // true，属性存在！
```

#### 4.1.8 for..in
为了遍历一个对象的所有键（key），可以使用一个特殊形式的循环：`for..in`
```js
for (key in object) {
  // 对此对象属性中的每个键执行的代码
}
```


### 4.2 对象引用和复制
对象与原始类型的根本区别之一是，对象是“通过引用”存储和复制的，而原始类型：字符串、数字、布尔值等 —— 总是“作为一个整体”复制
**赋值了对象的变量存储的不是对象本身，而是该对象“在内存中的地址” —— 换句话说就是对该对象的“引用”。**
**当一个对象变量被复制 —— 引用被复制，而该对象自身并没有被复制。**

#### 4.2.1 对象通过引用比较
仅当两个对象为同一对象时，两者才相等
```js
let a = {};
let b = a; // 复制引用
alert( a == b ); // true，都引用同一对象
alert( a === b ); // true

let c = {};
let d = {}; // 两个独立的对象
alert( c == d ); // false
```

#### 4.2.2 Object.assign,克隆与合并
拷贝一个对象变量会又创建一个对相同对象的引用
要复制一个对象需要创建一个新对象，并通过遍历现有属性的结构，在原始类型值的层面，将其复制到新对象，以复制已有对象的结构
```js {6-11}
let user = {
  name: "John",
  age: 30
};
let clone = {}; // 新的空对象
// 将 user 中所有的属性拷贝到其中
for (let key in user) {
  clone[key] = user[key];
}
// 现在 clone 是带有相同内容的完全独立的对象
clone.name = "Pete"; // 改变了其中的数据
alert( user.name ); // 原来的对象中的 name 属性依然是 John
```
我们也可以使用 [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) 方法来达成同样的效果
```js
Object.assign(dest, [src1, src2, src3...])
```

- 第一个参数 `dest` 是指目标对象。
- 更后面的参数 `src1, ..., srcN`（可按需传递多个参数）是源对象。
- 该方法将所有源对象的属性拷贝到目标对象 `dest` 中。换句话说，从第二个开始的所有参数的属性都被拷贝到第一个参数的对象中。
- 调用结果返回 `dest`。

我们可以用它来合并多个对象：
```js {4,5}
let user = { name: "John" };
let permissions1 = { canView: true };
let permissions2 = { canEdit: true };
// 将 permissions1 和 permissions2 中的所有属性都拷贝到 user 中
Object.assign(user, permissions1, permissions2);
// 现在 user = { name: "John", canView: true, canEdit: true }
```

如果被拷贝的属性的属性名已经存在，那么它会被覆盖：

```js
let user = { name: "John" };
Object.assign(user, { name: "Pete" });
alert(user.name); // 现在 user = { name: "Pete" }
```

#### 4.2.3 深层克隆
如果对象中的属性存在对象，那么该属性会被以引用形式拷贝
```js
let user = {
  name: "John",
  sizes: {
    height: 182,
    width: 50
  }
};
let clone = Object.assign({}, user);
alert( user.sizes === clone.sizes ); // true，同一个对象
// user 和 clone 分享同一个 sizes
user.sizes.width++;       // 通过其中一个改变属性值
alert(clone.sizes.width); // 51，能从另外一个看到变更的结果
```
为了解决这个问题，我们应该使用一个拷贝循环来检查 `user[key]` 的每个值，如果它是一个对象，那么也复制它的结构。这就是所谓的<mark>**深拷贝**</mark>。
:::tip const 声明的对象是可以被修改的
通过引用对对象进行存储的一个重要的副作用是声明为 `const` 的对象 **可以** 被修改。
例如：
```js
const user = {
  name: "John"
};
*!*
user.name = "Pete"; // (*)
*/!*
alert(user.name); // Pete
```
看起来 `(*)` 行的代码会触发一个错误，但实际并没有。`user` 的值是一个常量，它必须始终引用同一个对象，但该对象的属性可以被自由修改
:::



### 4.3 垃圾回收
对于开发者来说，JavaScript 的内存管理是自动的、无形的

#### 4.3.1 可达性（Reachability）
JavaScript 中主要的内存管理概念是 **可达性**
“可达”值是那些以某种方式可访问或可用的值。它们一定是存储在内存中的
1. 这里列出固有的可达值的基本集合，这些值明显不能被释放。

    比方说：

    - 当前执行的函数，它的局部变量和参数。
    - 当前嵌套调用链上的其他函数、它们的局部变量和参数。
    - 全局变量。
    - （还有一些内部的）

    这些值被称作 **根（roots）**。

2. 如果一个值可以通过引用链从根访问任何其他值，则认为该值是可达的

#### 4.3.2  简单的例子
```js
// user 具有对这个对象的引用
let user = {
  name: "John"
};
user = null;
```
全局变量 `"user"` 引用了对象 `{name："John"}`（为简洁起见，我们称它为 John）。John 的 `"name"` 属性存储一个原始值，所以它被写在对象内部。
如果 `user` 的值被重写了，这个引用就没了。John 变成不可达的了。因为没有引用了，就不能访问到它了。垃圾回收器会认为它是垃圾数据并进行回收，然后释放内存。
![引用状态](https://pic.imgdb.cn/item/62c69200f54cd3f937792344.jpg)![被重写后](https://pic.imgdb.cn/item/62c6922ff54cd3f9377963a1.jpg)

#### 4.3.3 两个引用
我们把 `user` 的引用复制给 `admin`：
```js
// user 具有对这个对象的引用
let user = {
  name: "John"
};
let admin = user;
user = null;
```
对象仍然可以被通过 `admin` 这个全局变量访问到，所以对象还在内存中。如果我们又重写了 `admin`，对象就会被删除

#### 4.3.4 相互关联的对象
```js
function marry(man, woman) {
  woman.husband = man;
  man.wife = woman;
  return {
    father: man,
    mother: woman
  }
}
let family = marry({
  name: "John"
}, {
  name: "Ann"
});
```
`marry` 函数通过让两个对象相互引用使它们“结婚”了，并返回了一个包含这两个对象的新对象。
由此产生的内存结构
![初始内存结构](https://pic.imgdb.cn/item/62c692c2f54cd3f9377a6703.jpg)
现在让我们移除两个引用：
```js
delete family.father;
delete family.mother.husband;
```
![移除两个引用](https://pic.imgdb.cn/item/62c692e6f54cd3f9377aad3c.jpg)![回收John](https://pic.imgdb.cn/item/62c692fef54cd3f9377ad8d5.jpg)
对外引用不重要，只有传入引用才可以使对象可达。所以，John 现在是不可达的，并且将被从内存中删除，同时 John 的所有数据也将变得不可达

#### 4.3.5 无法到达的岛屿
几个对象相互引用，但外部没有对其任意对象的引用，这些对象也可能是不可达的，并被从内存中删除
```js
family = null;
```
![无法到达的岛屿](https://pic.imgdb.cn/item/62c69360f54cd3f9377b7530.jpg)

#### 4.3.6 垃圾回收内部算法
垃圾回收的基本算法被称为 "mark-and-sweep"。

定期执行以下“垃圾回收”步骤：

- 垃圾收集器找到所有的根，并“标记”（记住）它们。
- 然后它遍历并“标记”来自它们的所有引用。
- 然后它遍历标记的对象并标记 **它们的** 引用。所有被遍历到的对象都会被记住，以免将来再次遍历到同一个对象。
- ……如此操作，直到所有可达的（从根部）引用都被访问到。
- 没有被标记的对象都会被删除。

这是垃圾收集工作的概念。JavaScript 引擎做了许多优化，使垃圾回收运行速度更快，并且不影响正常代码运行。

一些优化建议：

- **分代收集（Generational collection）**—— 对象被分成两组：“新的”和“旧的”。许多对象出现，完成它们的工作并很快死去，它们可以很快被清理。那些长期存活的对象会变得“老旧”，而且被检查的频次也会减少。
- **增量收集（Incremental collection）**—— 如果有许多对象，并且我们试图一次遍历并标记整个对象集，则可能需要一些时间，并在执行过程中带来明显的延迟。所以引擎试图将垃圾收集工作分成几部分来做。然后将这几部分会逐一进行处理。这需要它们之间有额外的标记来追踪变化，但是这样会有许多微小的延迟而不是一个大的延迟。
- **闲时收集（Idle-time collection）**—— 垃圾收集器只会在 CPU 空闲时尝试运行，以减少可能对代码执行的影响。


### 4.4 对象方法，this
在 JavaScript 中，行为（action）由属性中的函数来表示

#### 4.4.1 对象方法示例
作为对象属性的函数被称为 **方法**
```js
let user = {
  name: "John",
  age: 30
};
user.sayHi = function() {
  alert("Hello!");
};
user.sayHi(); // Hello!
```
使用函数表达式创建了一个函数，并将其指定给对象的 `user.sayHi` 属性
也可以使用预先声明的函数作为方法
```js 
let user = {
  // ...
};
// 首先，声明函数
function sayHi() {
  alert("Hello!");
}
// 然后将其作为一个方法添加
user.sayHi = sayHi;
user.sayHi(); // Hello!
```
##### 方法简写
在对象字面量中，有一种更短的（声明）方法的语法
```js
user = {
  sayHi: function() {
    alert("Hello");
  }
};
// 方法简写看起来更好，对吧？
let user = {
  sayHi() { // 与 "sayHi: function(){...}" 一样
    alert("Hello");
  }
};
```

#### 4.4.2 方法中的this
**为了访问该对象，方法中可以使用 `this` 关键字。**
`this` 的值就是在点之前的这个对象，即调用该方法的对象
```js
let user = {
  name: "John",
  age: 30,
  sayHi() {
    // "this" 指的是“当前的对象”
    alert(this.name);
  }
};
user.sayHi(); // John
```
技术上讲，也可以在不使用 `this` 的情况下，通过外部变量名来引用它。但这样的代码是不可靠的
```js
let user = {
  name: "John",
  age: 30,
  sayHi() {
    alert( user.name ); // 导致错误
  }
};
let admin = user;
user = null; // 重写让其更明显
admin.sayHi(); // TypeError: Cannot read property 'name' of null
```

#### 4.4.3 "this" 不受限制
JavaScript 中的 `this` 可以用于任何函数，即使它不是对象的方法
`this` 的值是在代码运行时计算出来的，它取决于代码上下文。

例如，这里相同的函数被分配给两个不同的对象，在调用中有着不同的 "this" 值：

```js
let user = { name: "John" };
let admin = { name: "Admin" };
function sayHi() {
  alert( this.name );
}
// 在两个对象中使用相同的函数
user.f = sayHi;
admin.f = sayHi;
// 这两个调用有不同的 this 值
// 函数内部的 "this" 是“点符号前面”的那个对象
user.f(); // John（this == user）
admin.f(); // Admin（this == admin）
admin['f'](); // Admin（使用点符号或方括号语法来访问这个方法，都没有关系。）
```
如果 `obj.f()` 被调用了，则 `this` 在 `f` 函数调用期间是 `obj`。所以在上面的例子中 this 先是 `user`，之后是 `admin`
:::tip 在没有对象的情况下调用：`this == undefined`
```js
function sayHi() {
  alert(this);
}
sayHi(); // undefined
```
在这种情况下，严格模式下的 `this` 值为 `undefined`。如果我们尝试访问 `this.name`，将会报错。
在非严格模式的情况下，`this` 将会是 **全局对象**（浏览器中的 `window`）。这是一个历史行为，`"use strict"` 已经将其修复了
:::

#### 4.4.4 箭头函数没有自己的 "this"
箭头函数有些特别：它们没有自己的 `this`。如果我们在这样的函数中引用 `this`，`this` 值取决于外部“正常的”函数。

举个例子，这里的 `arrow()` 使用的 `this` 来自于外部的 `user.sayHi()` 方法：
```js
let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => alert(this.firstName);
    arrow();
  }
};
user.sayHi(); // Ilya
```

这是箭头函数的一个特性，当我们并不想要一个独立的 `this`，反而想从外部上下文中获取时，它很有用



### 4.5 构造器与new
#### 4.5.1 构造函数
构造函数在技术上是常规函数。不过有两个约定：

1. 它们的命名以大写字母开头。
2. 它们只能由 `"new"` 操作符来执行

```js
function User(name) {
  this.name = name;
  this.isAdmin = false;
}
let user = new User("Jack");
alert(user.name); // Jack
alert(user.isAdmin); // false
```

当一个函数被使用 `new` 操作符执行时，它按照以下步骤：

1. 一个新的空对象被创建并分配给 `this`。
2. 函数体执行。通常它会修改 `this`，为其添加新的属性。
3. 返回 `this` 的值

```js
function User(name) {
  // this = {};（隐式创建）
  // 添加属性到 this
  this.name = name;
  this.isAdmin = false;
  // return this;（隐式返回）
}
```

#### 4.5.2 构造器模式测试：new.target
在一个函数内部，我们可以使用 `new.target` 属性来检查它是否被使用 `new` 进行调用了。

对于常规调用，它为 undefined，对于使用 `new` 的调用，则等于该函数：

```js
function User() {
  alert(new.target);
}
// 不带 "new"：
User(); // undefined
// 带 "new"：
new User(); // function User { ... }
```

我们也可以让 `new` 调用和常规调用做相同的工作，像这样：

```js
function User(name) {
  if (!new.target) { // 如果你没有通过 new 运行我
    return new User(name); // ……我会给你添加 new
  }
  this.name = name;
}
let john = User("John"); // 将调用重定向到新用户
alert(john.name); // John
```

#### 4.5.3 构造器的 return
通常，构造器没有 `return` 语句。它们的任务是将所有必要的东西写入 `this`，并自动转换为结果。

但是，如果这有一个 `return` 语句，那么规则就简单了：

- 如果 `return` 返回的是一个对象，则返回这个对象，而不是 `this`。
- 如果 `return` 返回的是一个原始类型，则忽略

```js
function BigUser() {
  this.name = "John";
  return { name: "Godzilla" };  // <-- 返回这个对象
}
alert( new BigUser().name );  // Godzilla，得到了那个对象

function SmallUser() {
  this.name = "John";
  return; // <-- 返回 this
}
alert( new SmallUser().name );  // John
```
:::tip 省略括号
如果没有参数，我们可以省略 `new` 后的括号：
```js
let user = new User; // <-- 没有参数
// 等同于
let user = new User();
```
:::

#### 4.5.4 构造器中的方法
我们不仅可以将属性添加到 `this` 中，还可以添加方法
```js 
function User(name) {
  this.name = name;
  this.sayHi = function() {
    alert( "My name is: " + this.name );
  };
}
let john = new User("John");
john.sayHi(); // My name is: John
/*
john = {
   name: "John",
   sayHi: function() { ... }
}
*/
```



### 4.6 可选链 ?.
可选链 `?.` 是一种访问嵌套对象属性的安全的方式。即使中间的属性不存在，也不会出现错误
#### 4.6.1 可选链语法
如果可选链 `?.` 前面的值为 `undefined` 或者 `null`，它会停止运算并返回 `undefined`
例如 `value?.prop`：
- 如果 `value` 存在，则结果与 `value.prop` 相同，
- 否则（当 `value` 为 `undefined/null` 时）则返回 `undefined`

请注意：`?.` 语法使其前面的值成为可选值，但不会对其后面的起作用

:::warning `?.` 前的变量必须已声明
如果未声明变量 `user`，那么 `user?.anything` 会触发一个错误：
```js
// ReferenceError: user is not defined
user?.address;
```
`?.` 前的变量必须已声明（例如 `let/const/var user` 或作为一个函数参数）。可选链仅适用于已声明的变量
:::

#### 4.6.2 短路效应
如果 `?.` 左边部分不存在，就会立即停止运算（“短路效应”）。

因此，如果在 `?.` 的右侧有任何进一步的函数调用或操作，它们均不会执行。

```js
let user = null;
let x = 0;
user?.sayHi(x++); // 没有 "user"，因此代码执行没有到达 sayHi 调用和 x++
alert(x); // 0，值没有增加
```

#### 4.6.3 其它变体：?.()，?.[]
可选链 `?.` 不是一个运算符，而是一个特殊的语法结构。它还可以与函数和方括号一起使用
```js
let userAdmin = {
  admin() {
    alert("I am admin");
  }
};
let userGuest = {};
userAdmin.admin?.(); // I am admin
userGuest.admin?.(); // 啥都没发生（没有这样的方法）
```

此外，我们还可以将 `?.` 跟 `delete` 一起使用：

```js
delete user?.name; // 如果 user 存在，则删除 user.name
```

:::warning 我们可以使用 `?.` 来安全地读取或删除，但不能写入
可选链 `?.` 不能用在赋值语句的左侧。
```js
let user = null;
user?.name = "John"; // Error，不起作用
// 因为它在计算的是：undefined = "John"
```
:::

### 4.7 symbol 类型
根据规范，只有两种原始类型可以用作对象属性键：

- 字符串类型
- symbol 类型

#### 4.7.1 symbol
"symbol" 值表示唯一的标识符。

可以使用 `Symbol()` 来创建这种类型的值：

```js
let id = Symbol();
```

创建时，我们可以给 symbol 一个描述（也称为 symbol 名），这在代码调试时非常有用：

```js
// id 是描述为 "id" 的 symbol
let id = Symbol("id");
```

symbol 保证是唯一的。即使我们创建了许多具有相同描述的 symbol，它们的值也是不同。描述只是一个标签，不影响任何东西
两个描述相同的 symbol —— 它们不相等：

```js
let id1 = Symbol("id");
let id2 = Symbol("id");
alert(id1 == id2); // false
```
:::warning symbol 不会被自动转换为字符串
JavaScript 中的大多数值都支持字符串的隐式转换

```js run
let id = Symbol("id");
alert(id); // 类型错误：无法将 symbol 值转换为字符串。
```
这是一种防止混乱的“语言保护”，因为字符串和 symbol 有本质上的不同，不应该意外地将它们转换成另一个
如果我们真的想显示一个 symbol，我们需要在它上面调用 `.toString()`，如下所示：
```js run
let id = Symbol("id");
alert(id.toString()); // Symbol(id)，现在它有效了
```
或者获取 `symbol.description` 属性，只显示描述（description）：
```js run
let id = Symbol("id");
alert(id.description); // id
```
:::

#### 4.7.2 “隐藏”属性
symbol 允许我们创建对象的“隐藏”属性，代码的任何其他部分都不能意外访问或重写这些属性
```js run
let user = { // 属于另一个代码
  name: "John"
};
let id = Symbol("id");
user[id] = 1;
alert( user[id] ); // 我们可以使用 symbol 作为键来访问数据
```
##### 对象字面量中的 symbol
如果我们要在对象字面量 `{...}` 中使用 symbol，则需要使用方括号把它括起来。

就像这样：

```js
let id = Symbol("id");
let user = {
  name: "John",
  [id]: 123 // 而不是 "id"：123
};
```
这是因为我们需要变量 `id` 的值作为键，而不是字符串 "id"
##### symbol 在 for..in 中会被跳过
symbol 属性不参与 `for..in` 循环
```js run
let id = Symbol("id");
let user = {
  name: "John",
  age: 30,
  [id]: 123
};
for (let key in user) alert(key); // name, age（没有 symbol）
// 使用 symbol 任务直接访问
alert( "Direct: " + user[id] );
```
[Object.keys(user)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/keys) 也会忽略它们。这是一般“隐藏符号属性”原则的一部分
相反，[Object.assign](mdn:js/Object/assign) 会同时复制字符串和 symbol 属性

#### 4.7.3 全局 symbol
有一个 **全局 symbol 注册表**。我们可以在其中创建 symbol 并在稍后访问它们，它可以确保每次访问相同名字的 symbol 时，返回的都是相同的 symbol
要从注册表中读取（不存在则创建）symbol，请使用 `Symbol.for(key)`。

该调用会检查全局注册表，如果有一个描述为 `key` 的 symbol，则返回该 symbol，否则将创建一个新 symbol（`Symbol(key)`），并通过给定的 `key` 将其存储在注册表中
```js run
// 从全局注册表中读取
let id = Symbol.for("id"); // 如果该 symbol 不存在，则创建它
// 再次读取（可能是在代码中的另一个位置）
let idAgain = Symbol.for("id");
// 相同的 symbol
alert( id === idAgain ); // true
```
##### Symbol.keyFor
对于全局 symbol，不仅有 `Symbol.for(key)` 按名字返回一个 symbol，还有一个反向调用：`Symbol.keyFor(sym)`，它的作用完全反过来：通过全局 symbol 返回一个名字
```js run
// 通过 name 获取 symbol
let sym = Symbol.for("name");
let sym2 = Symbol.for("id");
// 通过 symbol 获取 name
alert( Symbol.keyFor(sym) ); // name
alert( Symbol.keyFor(sym2) ); // id
```
`Symbol.keyFor` 内部使用全局 symbol 注册表来查找 symbol 的键。所以它不适用于非全局 symbol。如果 symbol 不是全局的，它将无法找到它并返回 `undefined`

#### 4.7.4 系统 symbol
JavaScript 内部有很多“系统” symbol，我们可以使用它们来微调对象的各个方面
[众所周知的 symbol](https://tc39.github.io/ecma262/#sec-well-known-symbols) 表的规范中：
- `Symbol.hasInstance`
- `Symbol.isConcatSpreadable`
- `Symbol.iterator`
- `Symbol.toPrimitive`

### 4.8 对象 — 原始值转换
当对象相加 `obj1 + obj2`，相减 `obj1 - obj2`，或者使用 `alert(obj)` 打印时会发生什么？
在此类运算的情况下，对象会被自动转换为原始值，然后对这些原始值进行运算，并得到运算结果（也是一个原始值）

#### 4.8.1 转换规则
1. 没有转换为布尔值。所有的对象在布尔上下文（context）中均为 `true`，就这么简单。只有字符串和数字转换。
2. 数字转换发生在对象相减或应用数学函数时。例如，`Date` 对象（将在 <info:date> 一章中介绍）可以相减，`date1 - date2` 的结果是两个日期之间的差值。
3. 至于字符串转换 —— 通常发生在我们像 `alert(obj)` 这样输出一个对象和类似的上下文中。

#### 4.8.2 hint
类型转换在各种情况下有三种变体。它们被称为 "hint"  

`"string"`
: 对象到字符串的转换，当我们对期望一个字符串的对象执行操作时，如 "alert"：

    ```js
    // 输出
    alert(obj);
    // 将对象作为属性键
    anotherObj[obj] = 123;
    ```

`"number"`
: 对象到数字的转换，例如当我们进行数学运算时：

    ```js
    // 显式转换
    let num = Number(obj);
    // 数学运算（除了二元加法）
    let n = +obj; // 一元加法
    let delta = date1 - date2;
    // 小于/大于的比较
    let greater = user1 > user2;
    ```

    大多数内建的数学函数也包括这种转换。

`"default"`
: 在少数情况下发生，当运算符“不确定”期望值的类型时。

    例如，二元加法 `+` 可用于字符串（连接），也可以用于数字（相加）。因此，当二元加法得到对象类型的参数时，它将依据 `"default"` hint 来对其进行转换。

    此外，如果对象被用于与字符串、数字或 symbol 进行 `==` 比较，这时到底应该进行哪种转换也不是很明确，因此使用 `"default"` hint。

    ```js
    // 二元加法使用默认 hint
    let total = obj1 + obj2;
    // obj == number 使用默认 hint
    if (user == 1) { ... };
    ```

    像 `<` 和 `>` 这样的小于/大于比较运算符，也可以同时用于字符串和数字。不过，它们使用 "number" hint，而不是 "default"。这是历史原因。  

**为了进行转换，JavaScript 尝试查找并调用三个对象方法：**

1. 调用 `obj[Symbol.toPrimitive](hint)` —— 带有 symbol 键 `Symbol.toPrimitive`（系统 symbol）的方法，如果这个方法存在的话，
2. 否则，如果 hint 是 `"string"`
   —— 尝试调用 `obj.toString()` 或 `obj.valueOf()`，无论哪个存在。
3. 否则，如果 hint 是 `"number"` 或 `"default"`
   —— 尝试调用 `obj.valueOf()` 或 `obj.toString()`，无论哪个存在。

#### 4.8.3 Symbol.toPrimitive

如果 `Symbol.toPrimitive` 方法存在，则它会被用于所有 hint，无需更多其他方法。

例如，这里 `user` 对象实现了它：

```js run
let user = {
  name: "John",
  money: 1000,
  [Symbol.toPrimitive](hint) {
    alert(`hint: ${hint}`);
    return hint == "string" ? `{name: "${this.name}"}` : this.money;
  }
};
// 转换演示：
alert(user); // hint: string -> {name: "John"}
alert(+user); // hint: number -> 1000
alert(user + 500); // hint: default -> 1500
```

#### 4.8.4 toString/valueOf
如果没有 `Symbol.toPrimitive`，那么 JavaScript 将尝试寻找 `toString` 和 `valueOf` 方法：

- 对于 `"string"` hint：调用 `toString` 方法，如果它不存在，则调用 `valueOf` 方法（因此，对于字符串转换，优先调用 `toString`）。
- 对于其他 hint：调用 `valueOf` 方法，如果它不存在，则调用 `toString` 方法（因此，对于数学运算，优先调用 `valueOf` 方法）。

默认情况下，普通对象具有 `toString` 和 `valueOf` 方法：

- `toString` 方法返回一个字符串 `"[object Object]"`。
- `valueOf` 方法返回对象自身。

##### 转换可以返回任何原始类型
关于所有原始转换方法，有一个重要的点需要知道，就是它们不一定会返回 "hint" 的原始值。

没有限制 `toString()` 是否返回字符串，或 `Symbol.toPrimitive` 方法是否为 `"number"` hint 返回数字。

唯一强制性的事情是：这些方法必须返回一个原始值，而不是对象



## 5 数据类型
### 5.1 原始数据类型方法
JavaScript 允许我们像使用对象一样使用原始类型（字符串，数字等）。JavaScript 还提供了这样的调用方法
#### 5.1.1 原始类型与对象
原始值：
- 是原始类型中的一种值。
- 在 JavaScript 中有 7 种原始类型：`string`，`number`，`bigint`，`boolean`，`symbol`，`null` 和 `undefined`。

对象：

- 能够存储多个值作为属性。
- 可以使用大括号 `{}` 创建对象，例如：`{name: "John", age: 30}`。JavaScript 中还有其他种类的对象，例如函数就是对象

对象比原始类型“更重”。它们需要额外的资源来支持运作

#### 5.1.2 当作对象的原始类型
在保持原始类型轻量的前提下提供可以用方法访问的操作，所以提出了**对象包装器**，实现下面的解决方案  
1. 原始类型仍然是原始的。与预期相同，提供单个值
2. JavaScript 允许访问字符串，数字，布尔值和 symbol 的方法和属性
3. 为了使它们起作用，创建了提供额外功能的特殊“对象包装器”，使用后即被销毁

<mark>“对象包装器”</mark>对于每种原始类型都是不同的，它们被称为 `String`、`Number`、`Boolean`、`Symbol` 和 `BigInt`。因此，它们提供了不同的方法

用法演示如下：

```js
let str = "Hello";
alert( str.toUpperCase() ); // HELLO
```
以下是 `str.toUpperCase()` 中实际发生的情况：

1. 字符串 `str` 是一个原始值。因此，在访问其属性时，会创建一个包含字符串字面值的特殊对象，并且具有有用的方法，例如 `toUpperCase()`。
2. 该方法运行并返回一个新的字符串（由 `alert` 显示）。
3. 特殊对象被销毁，只留下原始值 `str`。

JavaScript 引擎高度优化了这个过程。它甚至可能跳过创建额外的对象。但是它仍然必须遵守规范，并且表现得好像它创建了一样

::: warning 构造器 `String/Number/Boolean` 仅供内部使用
像 Java 这样的一些语言允许我们使用 `new Number(1)` 或 `new Boolean(false)` 等语法，明确地为原始类型创建“对象包装器”。
在 JavaScript 中，由于历史原因，这也是可以的，但极其 **不推荐**。因为这样会出问题。
例如：
```js
alert( typeof 0 ); // "number"
alert( typeof new Number(0) ); // "object"!
```
对象在 `if` 中始终为真，因此此处的 alert 将显示：
```js
let zero = new Number(0);
if (zero) { // zero 为 true，因为它是一个对象
  alert( "zero is truthy?!?" );
}
```
另一方面，调用不带 `new`（关键字）的 `String/Number/Boolean` 函数是完全理智和有用的。它们将一个值转换为相应的类型：转成字符串、数字或布尔值（原始类型）。
例如，下面完全是有效的：
```js
let num = Number("123"); // 将字符串转成数字
```
:::

::: warning null/undefined 没有任何方法
特殊的原始类型 `null` 和 `undefined` 是例外。它们没有对应的“对象包装器”，也没有提供任何方法。从某种意义上说，它们是“最原始的”。
尝试访问这种值的属性会导致错误：
```js
alert(null.test); // error
```
:::


### 5.2 数字类型
在现代 JavaScript 中，数字（number）有两种类型：

1. JavaScript 中的常规数字以 64 位的格式 [IEEE-754](https://en.wikipedia.org/wiki/IEEE_754-2008_revision) 存储，也被称为“双精度浮点数”。这是我们大多数时候所使用的数字，我们将在本章中学习它们。

2. BigInt 数字，用于表示任意长度的整数。有时会需要它们，因为常规数字不能安全地超过 <code>2<sup>53</sup></code> 或小于 <code>-2<sup>53</sup></code>。由于仅在少数特殊领域才会用到 BigInt

所以，此章节我们讨论的都是常规数字类型
#### 5.2.1 编写数字的更多方法
##### 下划线 `_`
可以使用下划线 `_` 作为数字的分隔符，下划线 `_` 扮演了“[语法糖](https://en.wikipedia.org/wiki/Syntactic_sugar)”的角色，使得数字具有更强的可读性。JavaScript 引擎会直接忽略
```js
let billion1 = 1000000000;
let billion2 = 1_000_000_000;
```
##### 字母 `e`
`e` 把数字乘以 `1` 后面跟着给定数量的 0 的数字
```js
1e3 === 1 * 1000; // e3 表示 *1000
1.23e6 === 1.23 * 1000000; // e6 表示 *1000000
// -3 除以 1 后面跟着 3 个 0 的数字
1e-3 === 1 / 1000; // 0.001
// -6 除以 1 后面跟着 6 个 0 的数字
1.23e-6 === 1.23 / 1000000; // 0.00000123
```

#### 5.2.2 十六进制，二进制和八进制数字
十六进制有一种较短的写方法：`0x`，然后是数字
```js
// 十六进制
alert( 0xff ); // 255
alert( 0xFF ); // 255（一样，大小写没影响）
```
二进制和八进制数字系统很少使用，但也支持使用 `0b` 和 `0o` 前缀
```js
let a = 0b11111111; // 二进制形式的 255
let b = 0o377; // 八进制形式的 255
alert( a == b ); // true，两边是相同的数字，都是 255
```
只有这三种进制支持这种写法。对于其他进制，我们应该使用函数 `parseInt`

#### 5.2.3 toString(base)
方法 `num.toString(base)` 返回在给定 `base` 进制数字系统中 `num` 的字符串表示形式
```js
let num = 255;
alert( num.toString(16) );  // ff
alert( num.toString(2) );   // 11111111
```

`base` 的范围可以从 `2` 到 `36`。默认情况下是 `10`
常见的用例如下：

- **base=16** 用于十六进制颜色，字符编码等，数字可以是 `0..9` 或 `A..F`。
- **base=2** 主要用于调试按位操作，数字可以是 `0` 或 `1`。
- **base=36** 是最大进制，数字可以是 `0..9` 或 `A..Z`。所有拉丁字母都被用于了表示数字。对于 `36` 进制来说，一个有趣且有用的例子是，当我们需要将一个较长的数字标识符转换成较短的时候，例如做一个短的 URL。可以简单地使用基数为 `36` 的数字系统表示：

::: warning 使用两个点来调用一个方法
请注意 `123456..toString(36)` 中的两个点不是打错了。如果我们想直接在一个数字上调用一个方法，比如上面例子中的 `toString`，那么我们需要在它后面放置两个点 `..`。  

如果我们放置一个点：`123456.toString(36)`，那么就会出现一个 error，因为 JavaScript 语法隐含了第一个点之后的部分为小数部分。如果我们再放一个点，那么 JavaScript 就知道小数部分为空，现在使用该方法。  

也可以写成 `(123456).toString(36)`。
::: 

#### 5.2.4 舍入
舍入（rounding）是使用数字时最常用的操作之一
`Math.floor`
: 向下舍入：`3.1` 变成 `3`，`-1.1` 变成 `-2`。

`Math.ceil`
: 向上舍入：`3.1` 变成 `4`，`-1.1` 变成 `-1`。

`Math.round`
: 向最近的整数舍入：`3.1` 变成 `3`，`3.6` 变成 `4`，中间值 `3.5` 变成 `4`。

`Math.trunc`（IE 浏览器不支持这个方法）
: 移除小数点后的所有内容而没有舍入：`3.1` 变成 `3`，`-1.1` 变成 `-1`。

这个是总结它们之间差异的表格：

|        | `Math.floor` | `Math.ceil` | `Math.round` | `Math.trunc` |
| ------ | ------------ | ----------- | ------------ | ------------ |
| `3.1`  | `3`          | `4`         | `3`          | `3`          |
| `3.6`  | `3`          | `4`         | `4`          | `3`          |
| `-1.1` | `-2`         | `-1`        | `-1`         | `-1`         |
| `-1.6` | `-2`         | `-1`        | `-2`         | `-1`         |

##### 数字舍入到小数点后 `n` 位
1. 乘除法

    例如，要将数字舍入到小数点后两位，我们可以将数字乘以 `100`，调用舍入函数，然后再将其除回。
    ```js run
    let num = 1.23456;
    alert( Math.round(num * 100) / 100 ); // 1.23456 -> 123.456 -> 123 -> 1.23
    ```

2. 函数 [toFixed(n)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed) 将数字舍入到小数点后 `n` 位，并以字符串形式返回结果。
        
    ```js run
    let num = 12.34;
    alert( num.toFixed(1) ); // "12.3"
    ```

    这会向上或向下舍入到最接近的值，类似于 `Math.round`：

    ```js run
    let num = 12.36;
    alert( num.toFixed(1) ); // "12.4"
    ```

    请注意 `toFixed` 的结果是一个字符串。如果小数部分比所需要的短，则在结尾添加零：

    ```js run
    let num = 12.34;
    alert( num.toFixed(5) ); // "12.34000"，在结尾添加了 0，以达到小数点后五位
    ```

    我们可以使用一元加号或 `Number()` 调用，将其转换为数字，例如 `+ num.toFixed(5)`。


#### 5.2.5 不精确的计算
在内部，数字是以 64 位格式 [IEEE-754](http://en.wikipedia.org/wiki/IEEE_754-1985) 表示的，所以正好有 64 位可以存储一个数字：其中 52 位被用于存储这些数字，其中 11 位用于存储小数点的位置（对于整数，它们为零），而 1 位用于符号。

如果一个数字真的很大，则可能会溢出 64 位存储，变成一个特殊的数值 `Infinity`：

```js
alert( 1e500 ); // Infinity
```

这可能不那么明显，但经常会发生的是，精度的损失
```js
alert( 0.1 + 0.2 == 0.3 ); // false
```
一个数字以其二进制的形式存储在内存中，一个 1 和 0 的序列。但是在十进制数字系统中看起来很简单的 `0.1`，`0.2` 这样的小数，实际上在二进制形式中是无限循环小数。

什么是 `0.1`？`0.1` 就是 `1` 除以 `10`，`1/10`，即十分之一。在十进制数字系统中，这样的数字表示起来很容易。将其与三分之一进行比较：`1/3`。三分之一变成了无限循环小数 `0.33333(3)`。

在十进制数字系统中，可以保证以 `10` 的整数次幂作为除数能够正常工作，但是以 `3` 作为除数则不能。也是同样的原因，在二进制数字系统中，可以保证以 `2` 的整数次幂作为除数时能够正常工作，但 `1/10` 就变成了一个无限循环的二进制小数。

使用二进制数字系统无法 **精确** 存储 *0.1* 或 *0.2*，就像没有办法将三分之一存储为十进制小数一样。

解决方法中最可靠的是借助`toFixed(n)`对结果进行舍入
```js
let sum = 0.1 + 0.2;
alert( sum.toFixed(2) ); // 0.30
```
::: tip 
```js run
// Hello！我是一个会自我增加的数字！
alert( 9999999999999999 ); // 显示 10000000000000000
```
出现了同样的问题：精度损失。有 64 位来表示该数字，其中 52 位可用于存储数字，但这还不够。所以最不重要的数字就消失了。  

JavaScript 不会在此类事件中触发 error。它会尽最大努力使数字符合所需的格式，但不幸的是，这种格式不够大到满足需求。
::: 

::: tip 两个零
数字内部表示的另一个有趣结果是存在两个零：`0` 和 `-0`。

这是因为在存储时，使用一位来存储符号，因此对于包括零在内的任何数字，可以设置这一位或者不设置。

在大多数情况下，这种区别并不明显，因为运算符将它们视为相同的值
::: 

#### 5.2.6 isFinite 和 isNaN
- `Infinity`（和 `-Infinity`）是一个特殊的数值，比任何数值都大（小）。
- `NaN` 代表一个 error。

它们属于 `number` 类型，但不是“普通”数字，因此，这里有用于检查它们的特殊函数
##### `isNaN(value)`
将其参数转换为数字，然后测试它是否为 `NaN`
```js run
alert( isNaN(NaN) ); // true
alert( isNaN("str") ); // true
```
::: warning NaN独一无二
我们不能使用 `=== NaN` 比较。"NaN" 是独一无二的，它不等于任何东西，包括它自身：

```js run
alert( NaN === NaN ); // false
```
:::

##### `isFinite(value)`
将其参数转换为数字，如果是常规数字而不是 `NaN/Infinity/-Infinity`，则返回 `true`
```js run
alert( isFinite("15") ); // true
alert( isFinite("str") ); // false，因为是一个特殊的值：NaN
alert( isFinite(Infinity) ); // false，因为是一个特殊的值：Infinity
```

有时 `isFinite` 被用于验证字符串值是否为常规数字：


```js run
let num = +prompt("Enter a number", '');
// 结果会是 true，除非你输入的是 Infinity、-Infinity 或不是数字
alert( isFinite(num) );
```

::: warning
请注意，在所有数字函数中，包括 `isFinite`，空字符串或仅有空格的字符串均被视为 `0`
:::

::: tip 与 `Object.is` 进行比较
有一个特殊的内建方法 `Object.is`，它类似于 `===` 一样对值进行比较，但它对于两种边缘情况更可靠：
1. 它适用于 `NaN`：`Object.is(NaN，NaN) === true`，这是件好事。
2. 值 `0` 和 `-0` 是不同的：`Object.is(0，-0) === false`，从技术上讲这是对的，因为在内部，数字的符号位可能会不同，即使其他所有位均为零。

在所有其他情况下，`Object.is(a，b)` 与 `a === b` 相同。

这种比较方式经常被用在 JavaScript 规范中。当内部算法需要比较两个值是否完全相同时，它使用 `Object.is`（内部称为SameValue）
::: 

#### 5.2.7 parseInt 和 parseFloat
使用加号 `+` 或 `Number()` 的数字转换是严格的。如果一个值不完全是一个数字，就会失败：

```js
alert( +"100px" ); // NaN
```

唯一的例外是字符串开头或结尾的空格，因为它们会被忽略。

`parseInt` 和 `parseFloat` 可以从字符串中“读取”数字，直到无法读取为止。如果发生 error，则返回收集到的数字。函数 `parseInt` 返回一个整数，而 `parseFloat` 返回一个浮点数：
```js
alert( parseInt('100px') ); // 100
alert( parseFloat('12.5em') ); // 12.5
alert( parseInt('12.3') ); // 12，只有整数部分被返回了
alert( parseFloat('12.3.4') ); // 12.3，在第二个点出停止了读取
```

某些情况下，`parseInt/parseFloat` 会返回 `NaN`。当没有数字可读时会发生这种情况：

```js
alert( parseInt('a123') ); // NaN，第一个符号停止了读取
```
::: tip parseInt(str, radix) 的第二个参数
`parseInt()` 函数具有可选的第二个参数。它指定了数字系统的基数，因此 `parseInt` 还可以解析十六进制数字、二进制数字等的字符串：
```js run
alert( parseInt('0xff', 16) ); // 255
alert( parseInt('ff', 16) ); // 255，没有 0x 仍然有效
alert( parseInt('2n9c', 36) ); // 123456
```
:::

#### 5.2.8 Math对象
JavaScript 有一个内建的 [Math](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math) 对象，它包含了一个小型的数学函数和常量库
`Math.random()`
: 返回一个从 0 到 1 的随机数（不包括 1）。

    ```js run
    alert( Math.random() ); // 0.1234567894322
    alert( Math.random() ); // 0.5435252343232
    alert( Math.random() ); // ... (任何随机数)
    ```

`Math.max(a, b, c...)` / `Math.min(a, b, c...)`
: 从任意数量的参数中返回最大/最小值。

    ```js run
    alert( Math.max(3, 5, -10, 0, 1) ); // 5
    alert( Math.min(1, 2) ); // 1
    ```

`Math.pow(n, power)`
: 返回 `n` 的给定（power）次幂。

    ```js run
    alert( Math.pow(2, 10) ); // 2 的 10 次幂 = 1024
    ```


### 5.3 字符串
在 JavaScript 中，文本数据被以字符串形式存储，单个字符没有单独的类型。

字符串的内部格式始终是 [UTF-16](https://en.wikipedia.org/wiki/UTF-16)，它不依赖于页面编码

#### 5.3.1 引号（Quotes）
字符串可以包含在单引号、双引号或反引号中：

```js
let single = 'single-quoted';
let double = "double-quoted";
let backticks = `backticks`;
```

单引号和双引号基本相同。但是，反引号允许我们通过 `${…}` 将任何表达式嵌入到字符串中：

```js run
function sum(a, b) {
  return a + b;
}
alert(`1 + 2 = ${sum(1, 2)}.`); // 1 + 2 = 3.
```

使用反引号的另一个优点是它们允许字符串跨行：

```js run
let guestList = `Guests:
 * John
 * Pete
 * Mary
`;
alert(guestList); // 客人清单，多行
```

#### 5.3.2 特殊字符
我们可以通过使用“换行符（newline character）”，以支持使用单引号和双引号来创建跨行字符串。换行符写作 `\n`，用来表示换行：

```js run
let guestList = "Guests:\n * John\n * Pete\n * Mary";
alert(guestList); // 一个多行的客人列表
```

例如，这两行描述的是一样的，只是书写方式不同：

```js run
let str1 = "Hello\nWorld"; // 使用“换行符”创建的两行字符串
// 使用反引号和普通的换行创建的两行字符串
let str2 = `Hello
World`;
alert(str1 == str2); // true
```

还有其他不常见的“特殊”字符。

这是完整列表：

| 字符                                    | 描述                                                                                                                                                      |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `\n`                                    | 换行                                                                                                                                                      |
| `\r`                                    | 在 Windows 文本文件中，两个字符 `\r\n` 的组合代表一个换行。而在非 Windows 操作系统上，它就是 `\n`。这是历史原因造成的，大多数的 Windows 软件也理解 `\n`。 |
| `\'`, `\"`                              | 引号                                                                                                                                                      |
| `\\`                                    | 反斜线                                                                                                                                                    |
| `\t`                                    | 制表符                                                                                                                                                    |
| `\b`, `\f`, `\v`                        | 退格，换页，垂直标签 —— 为了兼容性，现在已经不使用了。                                                                                                    |
| `\xXX`                                  | 具有给定十六进制 Unicode `XX` 的 Unicode 字符，例如：`'\x7A'` 和 `'z'` 相同。                                                                             |
| `\uXXXX`                                | 以 UTF-16 编码的十六进制代码 `XXXX` 的 Unicode 字符，例如 `\u00A9` —— 是版权符号 `©` 的 Unicode。它必须正好是 4 个十六进制数字。                          |
| `\u{X…XXXXXX}`（1 到 6 个十六进制字符） | 具有给定 UTF-32 编码的 Unicode 符号。一些罕见的字符用两个 Unicode 符号编码，占用 4 个字节。这样我们就可以插入长代码了。                                   |

Unicode 示例：

```js run
alert( "\u00A9" ); // ©
alert( "\u{20331}" ); // 佫，罕见的中国象形文字（长 Unicode）
alert( "\u{1F60D}" ); // 😍，笑脸符号（另一个长 Unicode）
```

所有的特殊字符都以反斜杠字符 `\` 开始。它也被称为“转义字符”。
:::warning
注意反斜杠 `\` 在 JavaScript 中用于正确读取字符串，然后消失。内存中的字符串没有 `\`。
:::

#### 5.3.3 字符串长度
`length` 属性表示字符串长度：

```js run
alert( `My\n`.length ); // 3
```

注意 `\n` 是一个单独的“特殊”字符，所以长度确实是 `3`

::: warning `length` 是一个属性
掌握其他编程语言的人，有时会错误地调用 `str.length()` 而不是 `str.length`。这是行不通的。

请注意 `str.length` 是一个数字属性，而不是函数。后面不需要添加括号
:::

#### 5.3.4 访问字符
要获取在 `pos` 位置的一个字符，可以使用方括号 `[pos]` 或者调用 [str.charAt(pos)](mdn:js/String/charAt) 方法。第一个字符从零位置开始
```js run
let str = `Hello`;
// 第一个字符
alert( str[0] ); // H
alert( str.charAt(0) ); // H
// 最后一个字符
alert( str[str.length - 1] ); // o
```
方括号是获取字符的一种现代化方法，而 `charAt` 是历史原因才存在的。

它们之间的唯一区别是，如果没有找到字符，`[]` 返回 `undefined`，而 `charAt` 返回一个空字符串：

```js run
let str = `Hello`;
alert( str[1000] ); // undefined
alert( str.charAt(1000) ); // ''（空字符串）
```

可以使用`for.. of`遍历字符
```js
for(let char of "Hello"){
  alert(char); //H,e,l,l,o
}
```

#### 5.3.5 字符串是不可变的
在 JavaScript 中，字符串不可更改。改变字符是不可能的。

我们证明一下为什么不可能：

```js run
let str = 'Hi';
str[0] = 'h'; // error
alert( str[0] ); // 无法运行
```

通常的解决方法是创建一个新的字符串，并将其分配给 `str` 而不是以前的字符串。

例如：

```js run
let str = 'Hi';
str = 'h' + str[1];  // 替换字符串
alert( str ); // hi
```

#### 5.3.6 改变大小写
[toLowerCase()](mdn:js/String/toLowerCase) 和 [toUpperCase()](mdn:js/String/toUpperCase) 方法可以改变大小写：

```js run
alert( 'Interface'.toUpperCase() ); // INTERFACE
alert( 'Interface'.toLowerCase() ); // interface
```

或者我们想要使一个字符变成小写：

```js
alert( 'Interface'[0].toLowerCase() ); // 'i'
```

#### 5.3.7 查找子字符串
##### str.indexOf
[str.indexOf(substr, pos)](mdn:js/String/indexOf)从给定位置 `pos` 开始，在 `str` 中查找 `substr`，如果没有找到，则返回 `-1`，否则返回匹配成功的位置。

例如：

```js run
let str = 'Widget with id';
alert( str.indexOf('Widget') ); // 0，因为 'Widget' 一开始就被找到
alert( str.indexOf('widget') ); // -1，没有找到，检索是大小写敏感的
alert( str.indexOf("id") ); // 1，"id" 在位置 1 处（……idget 和 id）
```

可选的第二个参数允许我们从一个给定的位置开始检索。

例如，`"id"` 第一次出现的位置是 `1`。查询下一个存在位置时，我们从 `2` 开始检索：

```js run
let str = 'Widget with id';
alert( str.indexOf('id', 2) ) // 12
```

::: tip `str.lastIndexOf(substr, pos)`
还有一个类似的方法 [str.lastIndexOf(substr, position)](mdn:js/String/lastIndexOf)，它从字符串的末尾开始搜索到开头。

它会以相反的顺序列出这些事件
:::

在 `if` 测试中 `indexOf` 有一点不方便。我们不能像这样把它放在 `if` 中：

```js run
let str = "Widget with id";
if (str.indexOf("Widget")) {
    alert("We found it"); // 不工作！
}
```

上述示例中的 `alert` 不会显示，因为 `str.indexOf("Widget")` 返回 `0`（意思是它在起始位置就查找到了匹配项）。是的，但是 `if` 认为 `0` 表示 `false`。

因此我们应该检查 `-1`，像这样：

```js {2}
let str = "Widget with id";
if (str.indexOf("Widget") != -1) {
    alert("We found it"); // 现在工作了！
}
```

::: tip 按位（bitwise）NOT 技巧
这里使用的一个老技巧是 [bitwise NOT](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT) `~` 运算符。它将数字转换为 32-bit 整数（如果存在小数部分，则删除小数部分），然后对其二进制表示形式中的所有位均取反

只有当 `n == -1` 时，`~n` 才为零（适用于任何 32-bit 带符号的整数 `n`）
```js run
let str = "Widget";
if (~str.indexOf("Widget")) {
  alert( 'Found it!' ); // 正常运行
}
```
由于 `~` 运算符将大数字截断为 32 位，因此存在给出 `0` 的其他数字，最小的数字是 `~4294967295=0`。这使得这种检查只有在字符串没有那么长的情况下才是正确的
现在我们只会在旧的代码中看到这个技巧，因为现代 JavaScript 提供了 `.includes` 方法（见下文）
:::

#### includes，startsWith，endsWith
更现代的方法 [str.includes(substr, pos)](mdn:js/String/includes) 根据 `str` 中是否包含 `substr` 来返回 `true/false`。

如果我们需要检测匹配，但不需要它的位置，那么这是正确的选择：

```js run
alert( "Widget with id".includes("Widget") ); // true
alert( "Hello".includes("Bye") ); // false
```

`str.includes` 的第二个可选参数是开始搜索的起始位置：

```js run
alert( "Widget".includes("id") ); // true
alert( "Widget".includes("id", 3) ); // false, 从位置 3 开始没有 "id"
```

方法 [str.startsWith](mdn:js/String/startsWith) 和 [str.endsWith](mdn:js/String/endsWith) 的功能与其名称所表示的意思相同：

```js run
alert( "Widget".startsWith("Wid") ); // true，"Widget" 以 "Wid" 开始
alert( "Widget".endsWith("get") ); // true，"Widget" 以 "get" 结束
```

#### 5.3.8 获取子字符串
JavaScript 中有三种获取字符串的方法：`substring`、`substr` 和 `slice`
##### `str.slice(start [, end])`
返回字符串从 `start` 到（但不包括）`end` 的部分
```js run
let str = "stringify";
alert( str.slice(0, 5) ); // 'strin'，从 0 到 5 的子字符串（不包括 5）
alert( str.slice(0, 1) ); // 's'，从 0 到 1，但不包括 1，所以只有在 0 处的字符
```
如果没有第二个参数，`slice` 会一直运行到字符串末尾：
```js run
let str = "stringify";
alert( str.slice(2) ); // 从第二个位置直到结束
```
`start/end` 也有可能是负值。它们的意思是起始位置从字符串结尾计算：
```js run
let str = "stringify";
// 从右边的第四个位置开始，在右边的第一个位置结束
alert( str.slice(-4, -1) ); // 'gif'
```
##### `str.substring(start [, end])`
返回字符串在 `start` 和 `end` **之间** 的部分
这与 `slice` 几乎相同，但它允许 `start` 大于 `end`。

例如：
```js run
let str = "stringify";
// 这些对于 substring 是相同的
alert( str.substring(2, 6) ); // "ring"
alert( str.substring(6, 2) ); // "ring"
// ……但对 slice 是不同的：
alert( str.slice(2, 6) ); // "ring"（一样）
alert( str.slice(6, 2) ); // ""（空字符串）
```
不支持负参数（不像 slice），它们被视为 `0`。

##### `str.substr(start [, length])`
返回字符串从 `start` 开始的给定 `length` 的部分
与以前的方法相比，这个允许我们指定 `length` 而不是结束位置：

```js run
let str = "stringify";
alert( str.substr(2, 4) ); // 'ring'，从位置 2 开始，获取 4 个字符
```
第一个参数可能是负数，从结尾算起：
```js run
let str = "stringify";
alert( str.substr(-4, 2) ); // 'gi'，从第 4 位获取 2 个字符
```
| 方法                    | 选择方式……                                            | 负值参数            |
| ----------------------- | ----------------------------------------------------- | ------------------- |
| `slice(start, end)`     | 从 `start` 到 `end`（不含 `end`）                     | 允许                |
| `substring(start, end)` | `start` 与 `end` 之间（包括 `start`，但不包括 `end`） | 负值代表 `0`        |
| `substr(start, length)` | 从 `start` 开始获取长为 `length` 的字符串             | 允许 `start` 为负数 |
::: tip 使用哪一个？
它们都可用于获取子字符串。正式一点来讲，`substr` 有一个小缺点：它不是在 JavaScript 核心规范中描述的，而是在附录 B 中。附录 B 的内容主要是描述因历史原因而遗留下来的仅浏览器特性。因此，理论上非浏览器环境可能无法支持 `substr`，但实际上它在别的地方也都能用。

相较于其他两个变体，`slice` 稍微灵活一些，它允许以负值作为参数并且写法更简短。因此仅仅记住这三种方法中的 `slice` 就足够了
:::

#### 5.3.8 比较字符串
所有的字符串都使用 [UTF-16](https://en.wikipedia.org/wiki/UTF-16) 编码。即：每个字符都有对应的数字代码。有特殊的方法可以获取代码表示的字符，以及字符对应的代码。

`str.codePointAt(pos)`
: 返回在 `pos` 位置的字符代码 :

    ```js run
    // 不同的字母有不同的代码
    alert( "z".codePointAt(0) ); // 122
    alert( "Z".codePointAt(0) ); // 90
    ```

`String.fromCodePoint(code)`
: 通过数字 `code` 创建字符

    ```js run
    alert( String.fromCodePoint(90) ); // Z
    ```

    我们还可以用 `\u` 后跟十六进制代码，通过这些代码添加 Unicode 字符：

    ```js run
    // 在十六进制系统中 90 为 5a
    alert( '\u005a' ); // Z
    ```

字符通过数字代码进行比较。越大的代码意味着字符越大。`a`（97）的代码大于 `Z`（90）的代码。

- 所有小写字母追随在大写字母之后，因为它们的代码更大。
- 一些像 `Ö` 的字母与主要字母表不同。这里，它的代码比任何从 `a` 到 `z` 的代码都要大。

##### 正确的比较
现代浏览器（IE10- 需要额外的库 [Intl.JS](https://github.com/andyearnshaw/Intl.js/)) 都支持国际化标准 [ECMA-402](http://www.ecma-international.org/ecma-402/1.0/ECMA-402.pdf)。

它提供了一种特殊的方法来比较不同语言的字符串，遵循它们的规则。

调用 [str.localeCompare(str2)](mdn:js/String/localeCompare) 会根据语言规则返回一个整数，这个整数能指示字符串 `str` 在排序顺序中排在字符串 `str2` 前面、后面、还是相同：

- 如果 `str` 排在 `str2` 前面，则返回负数。
- 如果 `str` 排在 `str2` 后面，则返回正数。
- 如果它们在相同位置，则返回 `0`。

#### 5.3.9 Unicode
##### 代理对
所有常用的字符都是一个 2 字节的代码。大多数欧洲语言，数字甚至大多数象形文字中的字母都有 2 字节的表示形式。

但 2 字节只允许 65536 个组合，这对于表示每个可能的符号是不够的。所以稀有的符号被称为“代理对”的一对 2 字节的符号编码。

这些符号的长度是 `2`：

```js run
alert( '𝒳'.length ); // 2，大写数学符号 X
alert( '😂'.length ); // 2，笑哭表情
alert( '𩷶'.length ); // 2，罕见的中国象形文字
```
注意，代理对在 JavaScript 被创建时并不存在，因此无法被编程语言正确处理！

我们实际上在上面的每个字符串中都有一个符号，但 `length` 显示长度为 `2`。

`String.fromCodePoint` 和 `str.codePointAt` 是几种处理代理对的少数方法。它们最近才出现在编程语言中。在它们之前，只有 [String.fromCharCode](mdn:js/String/fromCharCode) 和 [str.charCodeAt](mdn:js/String/charCodeAt)。这些方法实际上与 `fromCodePoint/codePointAt` 相同，但是不适用于代理对。

获取符号可能会非常麻烦，因为代理对被认为是两个字符：

```js run
alert( '𝒳'[0] ); // 奇怪的符号……
alert( '𝒳'[1] ); // ……代理对的一块
```

请注意，代理对的各部分没有任何意义。因此，上述示例中的 alert 显示的实际上是垃圾信息。

技术角度来说，代理对也是可以通过它们的代码检测到的：如果一个字符的代码在 `0xd800..0xdbff` 范围内，那么它是代理对的第一部分。下一个字符（第二部分）必须在 `0xdc00..0xdfff` 范围中。这些范围是按照标准专门为代理对保留的。

在上述示例中：

```js run
// charCodeAt 不理解代理对，所以它给出了代理对的代码
alert( '𝒳'.charCodeAt(0).toString(16) ); // d835，在 0xd800 和 0xdbff 之间
alert( '𝒳'.charCodeAt(1).toString(16) ); // dcb3, 在 0xdc00 和 0xdfff 之间
```

本章节后面的 iterable 章节中，你可以找到更多处理代理对的方法

##### 变音符号与规范化
在许多语言中，都有一些由基本字符组成的符号，在其上方/下方有一个标记。

最常见的“复合”字符在 UTF-16 表中都有自己的代码。但不是全部，因为可能的组合太多。

为了支持任意组合，UTF-16 允许我们使用多个 Unicode 字符：基本字符紧跟“装饰”它的一个或多个“标记”字符。

例如，如果我们 `S` 后跟有特殊的 "dot above" 字符（代码 `\u0307`），则显示 Ṡ。

```js run
alert( 'S\u0307' ); // Ṡ
```
两个视觉上看起来相同的字符，可以用不同的 Unicode 组合表示。

例如：

```js run
let s1 = 'S\u0307\u0323'; // Ṩ，S + 上点 + 下点
let s2 = 'S\u0323\u0307'; // Ṩ，S + 下点 + 上点
alert( `s1: ${s1}, s2: ${s2}` );
alert( s1 == s2 ); // false，尽管字符看起来相同（?!）
```

为了解决这个问题，有一个 “Unicode 规范化”算法，它将每个字符串都转化成单个“通用”格式。

它由 [str.normalize()](mdn:js/String/normalize) 实现。

```js run
alert( "S\u0307\u0323".normalize() == "S\u0323\u0307".normalize() ); // true
```

有趣的是，在实际情况下，`normalize()` 实际上将一个由 3 个字符组成的序列合并为一个：`\u1e68`（S 有两个点）。

```js run
alert( "S\u0307\u0323".normalize().length ); // 1
alert( "S\u0307\u0323".normalize() == "\u1e68" ); // true
```

事实上，情况并非总是如此，因为符号 `Ṩ` 是“常用”的，所以 UTF-16 创建者把它包含在主表中并给它了对应的代码。


### 5.4 数组
特殊的数据结构数组（`Array`）是一种 **有序集合**，里面的元素都是按顺序排列的

#### 5.4.1 声明数组
创建一个空数组有两种语法：

```js
let arr = new Array();
let arr = [];
```

#### 5.4.2 简单使用数组
数组元素从 0 开始编号。

我们可以通过方括号中的数字获取元素：

```js run
let fruits = ["Apple", "Orange", "Plum"];
alert( fruits[0] ); // Apple
alert( fruits[1] ); // Orange
alert( fruits[2] ); // Plum
```

可以替换元素：

```js
fruits[2] = 'Pear'; // 现在变成了 ["Apple", "Orange", "Pear"]
```

……或者向数组新加一个元素：

```js
fruits[3] = 'Lemon'; // 现在变成 ["Apple", "Orange", "Pear", "Lemon"]
```

`length` 属性的值是数组中元素的总个数：

```js run
let fruits = ["Apple", "Orange", "Plum"];
alert( fruits.length ); // 3
```

也可以用 `alert` 来显示整个数组。

```js run
let fruits = ["Apple", "Orange", "Plum"];
alert( fruits ); // Apple,Orange,Plum
```

数组可以存储任何类型的元素。

例如:

```js run no-beautify
// 混合值
let arr = [ 'Apple', { name: 'John' }, true, function() { alert('hello'); } ];
// 获取索引为 1 的对象然后显示它的 name
alert( arr[1].name ); // John
// 获取索引为 3 的函数并执行
arr[3](); // hello
```

#### 5.4.3 使用 "at" 获取最后一个元素
假设我们想要数组的最后一个元素。

一些编程语言允许我们使用负数索引来实现这一点，例如 `fruits[-1]`。

但在 JavaScript 中这行不通。结果将是 `undefined`，因为方括号中的索引是被按照其字面意思处理的。

我们可以显式地计算最后一个元素的索引，然后访问它：`fruits[fruits.length - 1]`。

```js run
let fruits = ["Apple", "Orange", "Plum"];
alert( fruits[fruits.length-1] ); // Plum
```

有一个更简短的语法 `fruits.at(-1)`：

```js run
let fruits = ["Apple", "Orange", "Plum"];
// 与 fruits[fruits.length-1] 相同
alert( fruits.at(-1) ); // Plum
```

换句话说，`arr.at(i)`：
- 如果 `i >= 0`，则与 `arr[i]` 完全相同。
- 对于 `i` 为负数的情况，它则从数组的尾部向前数。

#### 5.4.4 pop/push, shift/unshift 方法
[队列（queue）](https://en.wikipedia.org/wiki/Queue_(abstract_data_type))是最常见的使用数组的方法之一。在计算机科学中，这表示支持两个操作的一个有序元素的集合：

- `push` 在末端添加一个元素.
- `shift` 取出队列首端的一个元素，整个队列往前移，这样原先排第二的元素现在排在了第一

数组还有另一个用例，就是数据结构 [栈](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))。

它支持两种操作：

- `push` 在末端添加一个元素.
- `pop` 从末端取出一个元素.

所以新元素的添加和取出都是从“末端”开始的。

JavaScript 中的数组既可以用作队列，也可以用作栈。它们允许你从首端/末端来添加/删除元素。

这在计算机科学中，允许这样的操作的数据结构被称为 [双端队列（deque）](https://en.wikipedia.org/wiki/Double-ended_queue)。

**作用于数组末端的方法：**

`pop`
: 取出并返回数组的最后一个元素：

    ```js run
    let fruits = ["Apple", "Orange", "Pear"];
    alert( fruits.pop() ); // 移除 "Pear" 然后 alert 显示出来
    alert( fruits ); // Apple, Orange
    ```

    `fruits.pop()` 和 `fruits.at(-1)` 都返回数组的最后一个元素，但 `fruits.pop()` 同时也删除了数组的最后一个元素，进而修改了原数组。

`push`
: 在数组末端添加元素：

    ```js run
    let fruits = ["Apple", "Orange"];
    fruits.push("Pear");
    alert( fruits ); // Apple, Orange, Pear
    ```

    调用 `fruits.push(...)` 与 `fruits[fruits.length] = ...` 是一样的。

**作用于数组首端的方法：**

`shift`
: 取出数组的第一个元素并返回它：

    ```js run
    let fruits = ["Apple", "Orange", "Pear"];
    alert( fruits.shift() ); // 移除 Apple 然后 alert 显示出来
    alert( fruits ); // Orange, Pear
    ```

`unshift`
: 在数组的首端添加元素：

    ```js run
    let fruits = ["Orange", "Pear"];
    fruits.unshift('Apple');
    alert( fruits ); // Apple, Orange, Pear
    ```

`push` 和 `unshift` 方法都可以一次添加多个元素：

```js run
let fruits = ["Apple"];
fruits.push("Orange", "Peach");
fruits.unshift("Pineapple", "Lemon");
// ["Pineapple", "Lemon", "Apple", "Orange", "Peach"]
alert( fruits );
```

#### 5.4.5 数组原理
数组是一种特殊的对象。使用方括号来访问属性 `arr[0]` 实际上是来自于对象的语法。它其实与 `obj[key]` 相同，其中 `arr` 是对象，而数字用作键（key）。

它们扩展了对象，提供了特殊的方法来处理有序的数据集合以及 `length` 属性。但从本质上讲，它仍然是一个对象。

记住，在 JavaScript 中只有 8 种基本的数据类型。数组是一个对象，因此其行为也像一个对象。

数组真正特殊的是它们的内部实现。JavaScript 引擎尝试把这些元素一个接一个地存储在连续的内存区域，就像本章的插图显示的一样，而且还有一些其它的优化，以使数组运行得非常快。

但是，如果我们不像“有序集合”那样使用数组，而是像常规对象那样使用数组，这些就都不生效了。


```js
let fruits = []; // 创建一个数组
fruits[99999] = 5; // 分配索引远大于数组长度的属性
fruits.age = 25; // 创建一个具有任意名称的属性
```

这是可以的，因为数组是基于对象的。我们可以给它们添加任何属性。

但是 Javascript 引擎会发现，我们在像使用常规对象一样使用数组，那么针对数组的优化就不再适用了，然后对应的优化就会被关闭，这些优化所带来的优势也就荡然无存了。

数组误用的几种方式:

- 添加一个非数字的属性，比如 `arr.test = 5`。
- 制造空洞，比如：添加 `arr[0]`，然后添加 `arr[1000]` (它们中间什么都没有)。
- 以倒序填充数组，比如 `arr[1000]`，`arr[999]` 等等。

请将数组视为作用于 **有序数据** 的特殊结构。它们为此提供了特殊的方法。数组在 JavaScript 引擎内部是经过特殊调整的，使得更好地作用于连续的有序数据，所以请以正确的方式使用数组。如果你需要任意键值，那很有可能实际上你需要的是常规对象 `{}`

#### 5.4.6 数组性能
`push/pop` 方法运行的比较快，而 `shift/unshift` 比较慢

`shift` 操作必须做三件事:

1. 移除索引为 `0` 的元素。
2. 把所有的元素向左移动，把索引 `1` 改成 `0`，`2` 改成 `1` 以此类推，对其重新编号。
3. 更新 `length` 属性。

![](array-shift.svg)

**数组里的元素越多，移动它们就要花越多的时间，也就意味着越多的内存操作。**

`unshift` 也是一样：为了在数组的首端添加元素，我们首先需要将现有的元素向右移动，增加它们的索引值。

`push/pop` 不需要移动任何东西。如果从末端移除一个元素，`pop` 方法只需要清理索引值并缩短 `length` 就可以了

**`pop` 和`push`方法不需要移动任何东西，因为其它元素都保留了各自的索引。这就是为什么 `pop` 和`push` 会特别快。**

#### 5.4.7 数组循环
遍历数组最古老的方式就是 `for` 循环：

```js run
let arr = ["Apple", "Orange", "Pear"];
*!*
for (let i = 0; i < arr.length; i++) {
*/!*
  alert( arr[i] );
}
```

但对于数组来说还有另一种循环方式，`for..of`：

```js run
let fruits = ["Apple", "Orange", "Plum"];
// 遍历数组元素
for (let fruit of fruits) {
  alert( fruit ); 
}
```

`for..of` 不能获取当前元素的索引，只是获取元素值

技术上来讲，因为数组也是对象，所以使用 `for..in` 也是可以的：

```js run
let arr = ["Apple", "Orange", "Pear"];
*!*
for (let key in arr) {
*/!*
  alert( arr[key] ); // Apple, Orange, Pear
}
```

但这其实是一个很不好的想法。会有一些潜在问题存在：

1. `for..in` 循环会遍历 **所有属性**，不仅仅是这些数字属性。

    在浏览器和其它环境中有一种称为“类数组”的对象，它们 **看似是数组**。也就是说，它们有 `length` 和索引属性，但是也可能有其它的非数字的属性和方法，这通常是我们不需要的。`for..in` 循环会把它们都列出来。所以如果我们需要处理类数组对象，这些“额外”的属性就会存在问题。

2. `for..in` 循环适用于普通对象，并且做了对应的优化。但是不适用于数组，因此速度要慢 10-100 倍。当然即使是这样也依然非常快。只有在遇到瓶颈时可能会有问题。但是我们仍然应该了解这其中的不同。

通常来说，我们不应该用 `for..in` 来处理数组。

#### 5.4.8 数组 "length"
当我们修改数组的时候，`length` 属性会自动更新。它实际上不是数组里元素的个数，而是最大的数字索引值加一。

例如，一个数组只有一个元素，但是这个元素的索引值很大，那么这个数组的 `length` 也会很大：

```js run
let fruits = [];
fruits[123] = "Apple";
alert( fruits.length ); // 124
```

`length` 属性的另一个有意思的点是它是可写的。

如果我们手动增加它，则不会发生任何有趣的事儿。但是如果我们减少它，数组就会被截断。该过程是不可逆的，下面是例子：

```js run
let arr = [1, 2, 3, 4, 5];
arr.length = 2; // 截断到只剩 2 个元素
alert( arr ); // [1, 2]
arr.length = 5; // 又把 length 加回来
alert( arr[3] ); // undefined：被截断的那些数值并没有回来
```

所以，清空数组最简单的方法就是：`arr.length = 0;`

#### 5.4.9 new Array() 
创建数组的另一种语法：

```js
let arr = new Array("Apple", "Pear", "etc");
```

如果使用单个参数（即数字）调用 `new Array`，那么它会创建一个 **指定了长度，却没有任何项** 的数组。

```js
let arr = new Array(2); // 会创建一个 [2] 的数组吗？
alert( arr[0] ); // undefined！没有元素。
alert( arr.length ); // length 2
```

#### 5.4.10 多维数组
数组里的项也可以是数组。我们可以将其用于多维数组，例如存储矩阵：

```js run
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
alert( matrix[1][1] ); // 最中间的那个数
```

#### 5.4.11 toString
数组有自己的 `toString` 方法的实现，会返回以逗号隔开的元素列表。

例如：


```js run
let arr = [1, 2, 3];
alert( arr ); // 1,2,3
alert( String(arr) === '1,2,3' ); // true
```

此外，我们试试运行一下这个：

```js run
alert( [] + 1 ); // "1"
alert( [1] + 1 ); // "11"
alert( [1,2] + 1 ); // "1,21"
```

数组没有 `Symbol.toPrimitive`，也没有 `valueOf`，它们只能执行 `toString` 进行转换，所以这里 `[]` 就变成了一个空字符串，`[1]` 变成了 `"1"`，`[1,2]` 变成了 `"1,2"`。

#### 5.4.12 不要使用 == 比较数组
该运算符不会对数组进行特殊处理，它会像处理任意对象那样处理数组。

- 仅当两个对象引用的是同一个对象时，它们才相等 `==`。
- 如果 `==` 左右两个参数之中有一个参数是对象，另一个参数是原始类型，那么该对象将会被转换为原始类型
- ……`null` 和 `undefined` 相等 `==`，且各自不等于任何其他的值。

严格比较 `===` 更简单，因为它不会进行类型转换。

所以，如果我们使用 `==` 来比较数组，除非我们比较的是两个引用同一数组的变量，否则它们永远不相等。

例如：
```js run
alert( [] == [] ); // false
alert( [0] == [0] ); // false
```

从技术上讲，这些数组是不同的对象。所以它们不相等。`==` 运算符不会进行逐项比较。

与原始类型的比较也可能会产生看似很奇怪的结果：

```js run
alert( 0 == [] ); // true
alert('0' == [] ); // false
// 在 [] 被转换为 '' 后
alert( 0 == '' ); // true，因为 '' 被转换成了数字 0
alert('0' == '' ); // false，没有进一步的类型转换，是不同的字符串
```

在这里的两个例子中，我们将原始类型和数组对象进行比较。因此，数组 `[]` 被转换为原始类型以进行比较，被转换成了一个空字符串 `''`。



### 5.5 数组方法
#### 5.5.1 添加/移除数组元素
- `arr.push(...items)` —— 从尾端添加元素，
- `arr.pop()` —— 从尾端提取元素，
- `arr.shift()` —— 从首端提取元素，
- `arr.unshift(...items)` —— 从首端添加元素。

##### splice
因为 `delete`方法是通过 `key` 来移除对应的值。对于对象来说是可以的。但是对于数组来说，我们希望剩下的元素能够移动并占据被释放的位置，否则length属性是不会自动变化的

[arr.splice](mdn:js/Array/splice) 方法可以说是处理数组的瑞士军刀。它可以做所有事情：添加，删除和插入元素。


```js
arr.splice(start[, deleteCount, elem1, ..., elemN])
```

它从索引 `start` 开始修改 `arr`：删除 `deleteCount` 个元素并在当前位置插入 `elem1, ..., elemN`。最后返回已被删除元素的数组。

```js run
let arr = ["I", "study", "JavaScript","right", "now"];
// 删除数组的前三项，并使用其他内容代替它们
let removed = arr.splice(0, 3, "Let's", "dance");
alert( arr ) // 现在 ["Let's", "dance", "right", "now"]
alert( removed ) //"I", "study", "JavaScript"
```

::: tip 允许负向索引
在这里和其他数组方法中，负向索引都是被允许的。它们从数组末尾计算位置，如下所示：
```js run
let arr = [1, 2, 5];
// 从索引 -1（尾端前一位）
// 删除 0 个元素，
// 然后插入 3 和 4
arr.splice(-1, 0, 3, 4);
alert( arr ); // 1,2,3,4,5
```
:::

##### slice
```js
arr.slice([start], [end])
```
它会返回一个新数组，将所有从索引 `start` 到 `end`（不包括 `end`）的数组项复制到一个新的数组。`start` 和 `end` 都可以是负数，在这种情况下，从末尾计算索引。

它和字符串的 `str.slice` 方法有点像，就是把子字符串替换成子数组

```js run
let arr = ["t", "e", "s", "t"];
alert( arr.slice(1, 3) ); // e,s（复制从位置 1 到位置 3 的元素）
alert( arr.slice(-2) ); // s,t（复制从位置 -2 到尾端的元素）
```

我们也可以不带参数地调用它：`arr.slice()` 会创建一个 `arr` 的副本。其通常用于获取副本，以进行不影响原始数组的进一步转换。

##### concat
[arr.concat](mdn:js/Array/concat) 创建一个新数组，其中包含来自于其他数组和其他项的值。

```js
arr.concat(arg1, arg2...)
```

它接受任意数量的参数 —— 数组或值都可以。结果是一个包含来自于 `arr`，然后是 `arg1`，`arg2` 的元素的新数组。

如果参数 `argN` 是一个数组，那么其中的所有元素都会被复制。否则，将复制参数本身。

例如：

```js run
let arr = [1, 2];
// create an array from: arr and [3,4]
alert( arr.concat([3, 4]) ); // 1,2,3,4
// create an array from: arr and [3,4] and [5,6]
alert( arr.concat([3, 4], [5, 6]) ); // 1,2,3,4,5,6
// create an array from: arr and [3,4], then add values 5 and 6
alert( arr.concat([3, 4], 5, 6) ); // 1,2,3,4,5,6
```

通常，它只复制数组中的元素。其他对象，即使它们看起来像数组一样，但仍然会被作为一个整体添加：

```js run
let arr = [1, 2];
let arrayLike = {
  0: "something",
  length: 1
};
alert( arr.concat(arrayLike) ); // 1,2,[object Object]
```

……但是，如果类似数组的对象具有 `Symbol.isConcatSpreadable` 属性，那么它就会被 `concat` 当作一个数组来处理：此对象中的元素将被添加：

```js {5}
let arr = [1, 2];
let arrayLike = {
  0: "something",
  1: "else",
  [Symbol.isConcatSpreadable]: true,
  length: 2
};
alert( arr.concat(arrayLike) ); // 1,2,something,else
```

#### 5.5.2 遍历：forEach
[arr.forEach](mdn:js/Array/forEach) 方法允许为数组的每个元素都运行一个函数。

语法：
```js
arr.forEach(function(item, index, array) {
  // ... do something with item
});
```

```js 
["Bilbo", "Gandalf", "Nazgul"].forEach((item, index, array) => {
  alert(`${item} is at index ${index} in ${array}`);
});
```

该函数的结果（如果它有返回）会被抛弃和忽略

#### 5.5.3 搜索数组
##### indexOf/lastIndexOf 和 includes
[arr.indexOf](mdn:js/Array/indexOf) 和 [arr.includes](mdn:js/Array/includes) 方法语法相似，并且作用基本上也与字符串的方法相同，只不过这里是对数组元素而不是字符进行操作：

- `arr.indexOf(item, from)` 从索引 `from` 开始搜索 `item`，如果找到则返回索引，否则返回 `-1`。
- `arr.includes(item, from)` —— 从索引 `from` 开始搜索 `item`，如果找到则返回 `true`（译注：如果没找到，则返回 `false`）。


::: warning
请注意，`indexOf` 使用严格相等 `===` 进行比较。所以，如果我们搜索 `false`，它会准确找到 `false` 而不是数字 `0`。
:::

如果我们想检查数组中是否包含元素 `item`，并且不需要知道其确切的索引，那么 `arr.includes` 是首选。

方法 [arr.lastIndexOf](mdn:js/Array/lastIndexOf) 与 `indexOf` 相同，但从右向左查找。

```js run
let fruits = ['Apple', 'Orange', 'Apple'];
alert( arr.indexOf('Apple') ); // 0（第一个 Apple）
alert( arr.lastIndexOf('Apple') ); // 2（最后一个 Apple）
```

::: tip 方法 `includes` 可以正确的处理 `NaN`
方法 `includes` 的一个次要但值得注意的特性是，它可以正确处理 `NaN`，这与 `indexOf` 不同：
```js run
const arr = [NaN];
alert( arr.indexOf(NaN) ); // -1（错，应该为 0）
alert( arr.includes(NaN) );// true（正确）
```
这是因为 `includes` 是在比较晚的时候才被添加到 JavaScript 中的，并且在内部使用了更新了的比较算法。
:::

##### find 和 findIndex/findLastIndex
```js
let result = arr.find(function(item, index, array) {
  // 如果返回 true，则返回 item 并停止迭代
  // 对于假值（false）的情况，则返回 undefined
});
```

依次对数组中的每个元素调用该函数：

- `item` 是元素。
- `index` 是它的索引。
- `array` 是数组本身。

如果它返回 `true`，则搜索停止，并返回 `item`。如果没有搜索到，则返回 `undefined`。

```js run
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];
let user = users.find(item => item.id == 1);
alert(user.name); // John
```

[arr.findIndex](mdn:js/Array/findIndex) 方法（与 `arr.find`）具有相同的语法，但它返回找到的元素的索引，而不是元素本身。如果没找到，则返回 `-1`。

[arr.findLastIndex](mdn:js/Array/findLastIndex) 方法类似于 `findIndex`，但从右向左搜索，类似于 `lastIndexOf`。

```js run
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"},
  {id: 4, name: "John"}
];
// 寻找第一个 John 的索引
alert(users.findIndex(user => user.name == 'John')); // 0
// 寻找最后一个 John 的索引
alert(users.findLastIndex(user => user.name == 'John')); // 3
```

##### filter
`filter` 语法与 `find` 大致相同，但是返回的是所有匹配元素组成的数组：

```js
let results = arr.filter(function(item, index, array) {
  // 如果 true item 被 push 到 results，迭代继续
  // 如果什么都没找到，则返回空数组
});
```


```js run
let users = [
  {id: 1, name: "John"},
  {id: 2, name: "Pete"},
  {id: 3, name: "Mary"}
];
// 返回前两个用户的数组
let someUsers = users.filter(item => item.id < 3);
alert(someUsers.length); // 2
```

#### 5.5.4 转换数组
##### map
[arr.map](mdn:js/Array/map) 对数组的每个元素都调用函数，并返回结果数组。

```js
let result = arr.map(function(item, index, array) {
  // 返回新值而不是当前元素
})
```

```js run
let lengths = ["Bilbo", "Gandalf", "Nazgul"].map(item => item.length);
alert(lengths); // 5,7,6
```

##### sort(fn)
[arr.sort](mdn:js/Array/sort) 方法对数组进行 **原位（in-place）** 排序，更改元素的顺序。(译注：原位是指在此数组内，而非生成一个新数组。)

它还返回排序后的数组，但是返回值通常会被忽略，因为修改了 `arr` 本身。

语法：

```js run
let arr = [ 1, 2, 15 ];
// 该方法重新排列 arr 的内容
arr.sort();
alert( arr );  // 1, 15, 2
```

**这些元素默认情况下被按字符串进行排序。**

从字面上看，所有元素都被转换为字符串，然后进行比较。对于字符串，按照词典顺序进行排序，实际上应该是 `"2" > "15"`。

要使用我们自己的排序顺序，我们需要提供一个函数作为 `arr.sort()` 的参数。

该函数应该比较两个任意值并返回：

```js
function compare(a, b) {
  if (a > b) return 1; // 如果第一个值比第二个值大
  if (a == b) return 0; // 如果两个值相等
  if (a < b) return -1; // 如果第一个值比第二个值小
}
```

例如，按数字进行排序：

```js run
function compareNumeric(a, b) {
  if (a > b) return 1;
  if (a == b) return 0;
  if (a < b) return -1;
}
let arr = [ 1, 2, 15 ];
arr.sort(compareNumeric);
alert(arr);  // 1, 2, 15
```

现在结果符合预期了。

`arr` 可以是由任何内容组成的数组，它可能包含数字、字符串、对象或其他任何内容。我们有一组 **一些元素**。要对其进行排序，我们需要一个 **排序函数** 来确认如何比较这些元素。默认是按字符串进行排序的。

`arr.sort(fn)` 方法实现了通用的排序算法。我们不需要关心它的内部工作原理（大多数情况下都是经过 [快速排序](https://en.wikipedia.org/wiki/Quicksort) 或 [Timsort](https://en.wikipedia.org/wiki/Timsort) 算法优化的）。它将遍历数组，使用提供的函数比较其元素并对其重新排序，我们所需要的就是提供执行比较的函数 `fn`。

::: tip 比较函数可以返回任何数字
实际上，比较函数只需要返回一个正数表示“大于”，一个负数表示“小于”。
通过这个原理我们可以编写更短的函数：
```js run
let arr = [ 1, 2, 15 ];
arr.sort(function(a, b) { return a - b; });
alert(arr);  // *!*1, 2, 15*/!*
```
:::


::: tip 用 `localeCompare` for strings
字符串比较默认情况下，它通过字母的代码比较字母。
对于许多字母，最好使用 `str.localeCompare` 方法正确地对字母进行排序，例如 `Ö`。
```js run
let countries = ['Österreich', 'Andorra', 'Vietnam'];
alert( countries.sort( (a, b) => a > b ? 1 : -1) ); // Andorra, Vietnam, Österreich（错的）
alert( countries.sort( (a, b) => a.localeCompare(b) ) ); // Andorra,Österreich,Vietnam（对的！）
```
:::

##### reverse
[arr.reverse](mdn:js/Array/reverse) 方法用于颠倒 `arr` 中元素的顺序。


```js run
let arr = [1, 2, 3, 4, 5];
arr.reverse();
alert( arr ); // 5,4,3,2,1
```

它也会返回颠倒后的数组 `arr`

##### split 和 join
[str.split(delim)](mdn:js/String/split) 通过给定的分隔符 `delim` 将字符串分割成一个数组。


`split` 方法有一个可选的第二个数字参数 —— 对数组长度的限制。如果提供了，那么额外的元素会被忽略。但实际上它很少使用：

```js run
let arr = 'Bilbo, Gandalf, Nazgul, Saruman'.split(', ', 2);
alert(arr); // Bilbo, Gandalf
```


[arr.join(glue)](mdn:js/Array/join) 与 `split` 相反。它会在它们之间创建一串由 `glue` 粘合的 `arr` 项。

例如：

```js run
let arr = ['Bilbo', 'Gandalf', 'Nazgul'];
let str = arr.join(';'); // 使用分号 ; 将数组粘合成字符串
alert( str ); // Bilbo;Gandalf;Nazgul
```

##### reduce/reduceRight
[arr.reduce](mdn:js/Array/reduce) 方法和 [arr.reduceRight](mdn:js/Array/reduceRight) 用于根据数组计算单个值。

语法是：

```js
let value = arr.reduce(function(accumulator, item, index, array) {
  // ...
}, [initial]);
```

该函数一个接一个地应用于所有数组元素，并将其结果“搬运（carry on）”到下一个调用。

参数：

- `accumulator` —— 是上一个函数调用的结果，第一次等于  `initial`（如果提供了 `initial` 的话）。
- `item` —— 当前的数组元素。
- `index` —— 当前索引。
- `arr` —— 数组本身。

应用函数时，上一个函数调用的结果将作为第一个参数传递给下一个函数。因此，第一个参数本质上是累加器，用于存储所有先前执行的组合结果。最后，它成为 `reduce` 的结果。


在这里，我们通过一行代码得到一个数组的总和：

```js run
let arr = [1, 2, 3, 4, 5];
let result = arr.reduce((sum, current) => sum + current, 0);
alert(result); // 15
```

让我们看看细节，到底发生了什么。

1. 在第一次运行时，`sum` 的值为初始值 `initial`（`reduce` 的最后一个参数），等于 0，`current` 是第一个数组元素，等于 `1`。所以函数运行的结果是 `1`。
2. 在第二次运行时，`sum = 1`，我们将第二个数组元素（`2`）与其相加并返回。
3. 在第三次运行中，`sum = 3`，我们继续把下一个元素与其相加，以此类推……

计算流程：
每一行代表的是对下一个数组元素的函数调用：

|             | `sum` | `current` | `result` |
| ----------- | ----- | --------- | -------- |
| 第 1 次调用 | `0`   | `1`       | `1`      |
| 第 2 次调用 | `1`   | `2`       | `3`      |
| 第 3 次调用 | `3`   | `3`       | `6`      |
| 第 4 次调用 | `6`   | `4`       | `10`     |
| 第 5 次调用 | `10`  | `5`       | `15`     |


我们也可以省略初始值：

```js run
let arr = [1, 2, 3, 4, 5];
// 删除 reduce 的初始值（没有 0）
let result = arr.reduce((sum, current) => sum + current);
alert( result ); // 15
```

结果是一样的。这是因为如果没有初始值，那么 `reduce` 会将数组的第一个元素作为初始值，并从第二个元素开始迭代。


但是这种使用需要非常小心。如果数组为空，那么在没有初始值的情况下调用 `reduce` 会导致错误。

例如：

```js run
let arr = [];
// Error: Reduce of empty array with no initial value
// 如果初始值存在，则 reduce 将为空 arr 返回它（即这个初始值）。
arr.reduce((sum, current) => sum + current);
```

所以建议始终指定初始值。

[arr.reduceRight](mdn:js/Array/reduceRight) 和 [arr.reduce](mdn:js/Array/reduce) 方法的功能一样，只是遍历为从右到左。

#### 5.5.5 Array.isArray
数组是基于对象的，不构成单独的语言类型。

所以 `typeof` 不能帮助从数组中区分出普通对象：

```js run
alert(typeof {}); // object
alert(typeof []); // object（相同）
```

……但是数组经常被使用，因此有一种特殊的方法用于判断：[Array.isArray(value)](mdn:js/Array/isArray)。如果 `value` 是一个数组，则返回 `true`；否则返回 `false`。

```js run
alert(Array.isArray({})); // false
alert(Array.isArray([])); // true
```

#### 5.5.6 大多数方法都支持 "thisArg"
几乎所有调用函数的数组方法 —— 比如 `find`，`filter`，`map`，除了 `sort` 是一个特例，都接受一个可选的附加参数 `thisArg`。

以下是这些方法的完整语法：

```js
arr.find(func, thisArg);
arr.filter(func, thisArg);
arr.map(func, thisArg);
// ...
// thisArg 是可选的最后一个参数
```

`thisArg` 参数的值在 `func` 中变为 `this`。

例如，在这里我们使用 `army` 对象方法作为过滤器，`thisArg` 用于传递上下文（passes the context）：

```js {15}
let army = {
  minAge: 18,
  maxAge: 27,
  canJoin(user) {
    return user.age >= this.minAge && user.age < this.maxAge;
  }
};
let users = [
  {age: 16},
  {age: 20},
  {age: 23},
  {age: 30}
];
// 找到 army.canJoin 返回 true 的 user
let soldiers = users.filter(army.canJoin, army);
alert(soldiers.length); // 2
alert(soldiers[0].age); // 20
alert(soldiers[1].age); // 23
```

如果在上面的示例中我们使用了 `users.filter(army.canJoin)`，那么 `army.canJoin` 将被作为独立函数调用，并且这时 `this=undefined`，从而会导致即时错误。
