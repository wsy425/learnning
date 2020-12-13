# CSS简介
1. 主要使用场景：优化网页页面
2. css层叠样式表，标记语言
3. 主要用于设置HTML的文本内容、图片外型、网页布局



# 语法规范
1. 规则由选择器和一条或多条声明构成
2. 选择器用于指定CSS样式的HTML标签，花括号是对该对象设置的具体样式
3. 属性和属性值以“键值对”的形式出现
```HTML
<html>
<head>
    <title>测试</title>
    <style>
        h4 {
            color: cornflowerblue;
        }
    </style>
</head>
<body>
    <h4>你喜欢的食物</h4>
</html>
```



# 代码风格

## 样式格式
1. 紧凑格式
2. 展开格式：一行只写一个属性

## 样式大小写
一般使用小写

## 空格规范
1. 属性值前，冒号后面写一个空格
2. 选择器和大括号前写一个空格



# 选择器

## 基础选择器 
### 标签选择器
1. HTML标签名作为选择器
2. 会对所有该标签下的内容进行设定
### 类选择器
1. 语法标准
```HTML
<style>
    .red {
        color = red；
    }
</style>
<div class=“red”>想要变红色的文字</div>
```
2. 用class属性进行选择
3. 可以选择一个或者某几个标签
4. 不能用标签的名字选为类名
5. 长类名用-连接
6. 一个标签可以使用多个类名，多个类名之间用空格隔开
### id选择器
1. 通过#定义id，以id属性选择
2. 语法标准
```HTML
<style>
    #red {
        color = red；
    }
</style>
<div id=“red”>想要变红色的文字</div>
```
3. 只能调用一次，具有唯一性
### 通配符选择器
1. 用*，表示选取页面所有标签
2. 语法标准
```HTML
<style>
    * {
        color = red；
    }
</style>
<div>想要变红色的文字</div>
```
3. 通配符选择器不需要调用

## 复合选择器
把基础选择器进行组合形成的
![复合选择器总结.jpg](https://i.loli.net/2020/11/30/ADSCtpy9XRWmGuv.jpg)
### 后代选择器
1. 又叫包含选择器，只能选择后代
2. 语法：父类 后代 {样式说明}
3. 后代和父类用空格分开
4. 最终选择的是子类
5. 后代可以是子类也可以是子类的子类
6. 两个都可以是任意的基础选择器
```HTML
<style>
    ul.nav li a {
        color: red;
    }
</style>
```
### 子选择器
1. 又称子元素选择器，只能选择某元素最近一级子代
2. 语法：父类>子类 {样式说明}
```HTML
<style>
    ul.nav>a {
        color: red;
    }
</style>
```
### 并集选择器
1. 选择多组标签，同时定义相同的样式，用于集体声明
2. 语法：用逗号分隔
3. 任何形式的选择器都可以作为并集选择器的一部分
### 伪类选择器
1. 像某些标签添加特殊效果：比如给连接添加特殊效果
2. 语法：用冒号表示
#### 链接伪类
1. `a:link` 选择所有未访问的连接
2. `a:visited` 选择所有已访问的连接
3. `a:hover` 选择鼠标指针位于其上的连接
4. `a:active` 选择活动连接（鼠标按下未弹起的连接）
5. 为了确保能够生效，必须使用LVHA的顺序写
6. 浏览器中a有固定样式，要改变必须用a来设定
#### ：focus伪类选择
1. 用于获取光标所在的表单元素
2. 语法`input:focus{样式说明}`


# 字体属性

## 字体系列
1. 语法标准
```HTML
<style>
    div {
        font-family = "Microsoft Yahei"；
    }
</style>
<div>想要变微软雅黑的文字</div>
```
2. 多个字体之间用空格隔开
3. 一个字体有空格时，最好用“”框起来
4. 多个字体的作用是前面的字体找不到的时候寻找下一个字体

## 字体大小
1. `{font-size: 20px}`
2. 标题标签比较特殊，需要单独指定文字大小

## 字体粗细
1. `{font-weight :normal/400}`
2. 正常=normal=400
3. 加粗=bold=700
4. 数字在100-900里选

## 文字样式
1. `{font-style: italic}`
2. italic:倾斜
2. normal：正常

## 字体复合属性
1. `{font: font-style font-weight font-size/line-height font-family}`
2. 顺序有要求，不需要的属性可以省略，但是必须保留font-size和font-family
![字体属性总结.png](https://i.loli.net/2020/11/27/EoWxsXwkpaSRbJm.png)



# 文本属性
定义文本的外观，比如文本的颜色、对齐文本、装饰文本、文本缩进、行间距等

## 文本颜色
1. 语法
```HTML
div{
    color: red;
}
```
2. 属性内容
    + 预设值（pink）
    + 16进制数：#+6个数字
    + rgb代码

## 对齐文本
1. text-align属性用于设置元素内文本内容的水平对齐方式
2. 语法
```HTML
div{
    text-align: center;
}
```

## 装饰文本
1. text-decoration属性规定添加到文本的修饰，可以给文本添加下划线、删除线、上划线等
2. 语法
```HTML
div{
    text-decoration: underline;
}
```
3. 属性内容
    + none：默认，没有装饰线
    + underline：下划线
    + overline：上划线
    + line-through：删除线

## 文本缩进
1. text-indent属性用来指定文本首行缩进
2. 语法
```HTML
div{
    text-indent: 2em;
}
```
3. em是一个相对尺寸，当前元素一个文字大小的距离

## 行间距
1. line-height属性由于设置行高
2. 语法
```HTML
div{
    line-height: 2em;
}
```
3. 行高=上间距+文本高度+下间距

![文本属性总结.jpg](https://i.loli.net/2020/11/29/VvieGfpDOP4wEAt.jpg)



# 引入方式

## 行内样式表（行内式）
1. 在标签内部写上style属性
2. 语法`<div style="color: red"></div>`
3. 一定要是双引号，写法要符合CSS

## 内部样式表（嵌入式）
1. css写入html内部，写在< style>标签里
2. 理论上< style>可以放在任何地方，但一般放在head里
3. 可以控制整个页面
4. 代码结构清晰，但并没有完全分离

## 外部样式表
1. 样式单独写到CSS文件中，HTML引用CSS文件
2. 在HTML页面中，使用link标签引入
3. 语法`<link rel="stylesheet" href="css文件路径">`



# Emmet语法

## 快速生成CSS
1. 简写+tab

## 快速格式化代码
1. shift+alt+f

# 元素显示模式
1. 元素显示模式：标签以什么方式显示
![元素显示模式总结.jpg](https://i.loli.net/2020/11/30/FujXR23vVxbSi9p.jpg)

## 块元素
1. 典型块元素：< div> < h1>
2. 独占一行
3. 宽度、高度、内外边距都可以控制
4. 宽度默认是父级的100%
5. 是一个容器及盒子，里面可以放行内元素或者块级元素
6. 文字类元素内不能使用块元素

## 行内元素
1. 典型行内元素：< a> < span>
2. 相邻行内元素在一行上，一行显示多个
3. 宽高设置是无效的
4. 宽度默认是本身内容的宽度
5. 行内元素不能放块元素
6. 链接里不能再放链接
7. 链接可以放块元素

## 行内块元素
1. 特殊标签： < img/> < input/> < td>
2. 相邻行内块元素在一行上，之间会有空白间隙，一行可以显示多个
3. 默认宽度是本身内容的宽度
4. 宽度、高度、内外边距都可以控制

## 元素显示模式的转换
1. 转换成块元素`display:block;`
2. 转换成行内元素`display:inline;`
2. 转换成行内块元素`display:inline-block;`



# 背景
通过CSS背景属性，可以给页面元素添加背景样式
![背景总结.jpg](https://i.loli.net/2020/12/08/oHEUbfjnd18iMYy.jpg)
## 背景颜色
1. 语法
`background-color: 颜色值;`
2. 默认值：transparent（透明）

## 背景图片
1. 实际开发常见于logo或者一些装饰性的小图片或者超大的背景图片
2. 优点是非常便于控制位置
3. 语法
`background-image : none/url();`

## 背景平铺
1. 语法
`background-repeat: repeat/no-repeat/repeat-x/repeat-y;`
2. 默认情况是repeat
3. 背景颜色和背景图片可以同时添加，背景颜色位于最下层

## 背景图片位置
1. 语法
`background-position: x y;`
2. x,y都可以使用方位名词和精确单位
3. 方位名词
    + top
    + center
    + bottom
    + left
    + right
4. 两者都是方位名词，两个名词的顺序无关
5. 只指定一个方位名词，另一个默认为center
6. 精确单位第一个是x坐标，第二个是y坐标，顺序不能替换
7. 如果只指定一个精确单位，一定是x，垂直默认居中
8. 参数可以是混合单位。第一个是x坐标，第二个是y坐标，顺序不能替换

## 背景附着
1. 设置背景图片是固定还是随着页面其余部分滚动
2. 语法
`background-attachment: scroll/fixed;`

## 背景复合写法
1. 约定顺序：颜色+地址+平铺+滚动+位置
2. 语法
`background: transparent url() repeat fixed top;`

## 背景色半透明
1. 语法
`background: rgba(0,0,0,0.3)`
2. alpha透明度，0-1之间
3. 习惯性把0.3中的0去掉
4. 只是设置背景色半透明，对盒子里的内容没有影响



# CSS三大特性

## 层叠性
1. 相同选择器设置相同的样式，后面的会覆盖前面的
2. 冲突，后者覆盖
3. 不冲突，不层叠

## 继承性
1. 子标签会集成父标签里的样式
2. 子元素可以集成父元素的样式（text-,font-,line-以及color属性）

## 优先级
1. 选择器相同，则执行层叠性
2. 选择器不同，按权重大小
![选择器权重一览.jpg](https://i.loli.net/2020/12/08/2D6LouejckKPaGz.jpg)
3. 权重是4组数字组成，不会进位
4. 复合选择器需要权重叠加



# 盒子模型

## border边框
1. 由边框宽度、边框样式、边框颜色组成
2. `border : border-width // border-style // border-color`
3. 边框样式
    + solid：实线边框
    + dashed：虚线边框
    + dotted：点线边框
4. 边框复合写法
`border: 1px solid red;`没有编写顺序要求
5. 边框分开编辑
`border-top`编辑上边框
6. 表格边框合并
`border-collapse:collapse;`  
相邻表格边框合并在一起  
只对table相关
7. 边框会影响盒子实际大小  
盒子的实际大小 = 盒子高/宽 + 2*边框宽度 + padding

## content内容
装文字、图片、盒子

## padding内边距
1. 设置盒子边框和内容之间的距离
2. `padding-top // padding-bottom // padding-left // padding-right`
3. 内边距复合写法
![内边距复合写法规律.jpg](https://i.loli.net/2020/12/09/OFIypx8LNCKAouR.jpg)
4. 内边距会影响盒子实际大小  
盒子的实际大小 = 盒子高/宽 + 2*边框宽度 + 各部分padding
5. 如果盒子没有指定宽度，是继承的父级的宽度，加padding值的时候不会撑大盒子

## margin外边距
1. 设置盒子之间的距离
2. `margin-top // margin-bottom // margin-left // margin-right`
3. 外边距复合写法  
与内边距一致
4. 块级盒子水平居中:盒子设置宽度，左右外边距设置为auto
`margin: 0 auto`
5. 行内元素、行内块元素居中：给父级添加`text-align: center;`
6. 嵌套关系中父子元素中的父元素会取两者最大外边距，解决方法：
    + 父元素定义上边框
    + 父元素定义上内边距
    + 父元素添加`overflow: hidden;`
7. 浏览器中会设置初始内外边距建议清除
```css
* {
    padding: 0;
    margin: 0;
}
```

## 圆角边框
1. 语法
`border-radius: 圆角半径;`
2. 参数可以用精确数和百分比
3. 参数可以写四个，从左上角顺时针旋转
4. 可以指定特定角`border-top-left-radius: 圆角半径`

## 盒子阴影
1. 语法格式
`box-shadow: h-shadow v-shadow blur spread color inset`
2. 参数含义
![参数含义.jpg](https://i.loli.net/2020/12/12/21DkEKJ5fuzeYsh.jpg)
3. 只要前两个参数是必须写的
4. 影子不占空间



# 浮动
1. 浮动可以改变标签默认的排列方式
2. 多个块级元素横向排列用浮动

## 浮动语法
`选择器 { float: none|left|right;}`

## 浮动特性
1. 脱标
    + 浮动的元素在标准流中不占据位置
    + 浮动元素和标准流的元素不在一个图层上
2. 一行显示并且顶部对齐
    + 浮动的元素互相贴在一起，不会有缝隙
    + 父级宽度装不下时，另起一行对齐
3. 具有行内块元素的特性