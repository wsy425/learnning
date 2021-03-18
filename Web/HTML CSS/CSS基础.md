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

## 浮动布局注意点
1. 浮动和标准流的父元素一起使用
2. 一个元素浮动了，理论上兄弟元素也都应该浮动
3. 浮动的盒子只会影响浮动盒子后面的标准流，不会影响前面的标准流

## 清除浮动
1. 父盒子无法设置高度的时候需要清除浮动
2. 语法
`选择器 {clear: left|right|both}`
3. 清除浮动的方法
    + 额外标签法：在最后一个浮动元素后写一个空标签，设置清除浮动  
    新标签必须是块级元素
    + 父元素添加overflow：属性设置hidden|auto|scroll  
    无法显示溢出的部分
    + :after伪元素法：  
    ```css
    .clearfix:after {
        content: "";
        display: block;
        height: 0;
        clear: both;
        visibility: hidden;
    }
    ```
    + 双微元素清除浮动
    ```css
    .clearfix:before,.clearfix:after {
        content: "";
        display: table;
        height: 0;
    }
    .clearfix:after {
        clear: both;
    }
    .clearfix {
        *zoom: 1;
    }
    ```



# 书写顺序
1. 布局定位属性：display|position|float|clear|visibility|overflow
2. 自身属性：width|height|margin|padding|border|background
3. 文本属性：color|font|text-decoration|text-align|vertical-align|white-space|break-word
4. 其他属性（CSS3）：content|cursor|border-radius|box-shadow|background



# 定位

## 定位组成
1. 定位：将盒子定在某一个位置，所以定位也是在摆放盒子，按照定位的方式移动盒子
2. 定位 =  定位模式 + 边偏移
3. 定位模式：用于指定一个元素在文档中的定位方式
4. 边偏移：决定该元素的最终位置

## 定位模式
通过CSS的position属性来设置
### static静态定位
*仅作了解*
1. 默认定位方式，无定位的意思
2. 静态定位按照标准流摆放位置，没有边偏移
### relative相对定位
1. 相对定位是元素在移动位置的时候，是相对于它原来的位置来说的
2. 语法`选择器 { position: relative;}`
3. 原来在标准流的位置继续占有，后面的盒子仍然以标准流的方式对待
4. 不脱标，继续保持原来位置
5. 主要的作用是限制绝对定位
### absolute绝对定位
*重要*
1. 绝对定位是元素在移动位置的时候，是相对于它祖先元素来说的
2. 语法`选择器 { position: absolute;}`
3. 如果没有祖先元素或者祖先元素没有定位，则以浏览器为准定位
4. 如果祖先有定位，则以最近一级的有定位祖先元素为参考点移动位置
5. 绝对定位不再占有原来的位置，脱离标准流
### fixed固定定位
*重要*
1. 元素固定到浏览器可视区的某个位置
2. 语法`选择器 { position: fixed;}`
3. 以浏览器的可视窗口为参照点移动，与父级和滚动条没有关系
4. 固定定位不占有原先的位置
5. 技巧：固定在版心右侧位置`选择器 { position: fixed;left:50%;margin-left:版心宽度的一半}`
### sticky粘性定位
*仅作了解*
1. 某些情况是固定定位，某些情况是相对定位
2. 语法`选择器 { position: sticky;}`
3. 以浏览器可视窗口为参照点移动元素
4. 占有原先的位置
3. 必须添加边偏移中的一个，否则则为相对定位

## 边偏移
边偏移就是定位盒子移动到最终位置
1. top：顶端偏移量
2. bottom：底部偏移量
3. left：左侧偏移量
4. right：右侧偏移量

## 子绝父相
1. 子级使用绝对定位，父级则需要使用相对定位
2. 子级使用绝对定位，可以放在父级任何地方，不会影响兄弟
3. 父级需要加定位限制子级位置，且需要占有位置

## 定位叠放次序
1. 语法`选择器 { z-index: 1;}`
2. 数值可以是正整数、负整数或者0，默认auto，数值越大，盒子越靠上
3. 如果数值相同，按照书写顺序，后来者居上
4. 数字后面不能加单位
5. 只有定位的盒子才有z-size属性

## 定位的扩展
1. 绝对定位的盒子居中
`选择器 { position: absolute;left:50%;margin-left:-盒子宽度的一半}`
`选择器 { position: absolute;top:50%;margin-top:-盒子高度度的一半}`
2. 定位特殊特性
    + 行内元素添加绝对或者固定定位，可以直接设置高度和宽度
    + 块级元素添加绝对或者固定定位，默认是内容大小
    + 脱标的盒子不会除法外边距塌陷
3. 绝对定位会完全压住盒子
    + 浮动会压住标准流盒子，但不会压住标准流的文字
    + 绝对或者固定定位会压住标准流的文字



# 元素的显示与隐藏

## display
1. display属性用于设置一个元素如何显示
2. `display:none;`隐藏对象，隐藏后元素不占有原先的位置
3. `display:block;`显示对象；转换为块级元素
4. 搭配JS可以做很多网页特效

## visibility
1. visibility属性用于指定一个元素可见还是隐藏
2. `visibility:visible;`元素可见
3. `visibility:hidden;`元素隐藏，隐藏后元素占有原先的位置

## overflow
1. overflow属性指定了内容溢出的元素框时的状态
2. `overflow:hidden;`溢出内容隐藏
3. `overflow:scroll;`溢出内容显示滚动条，不溢出的时候也显示滚动条
4. `overflow:auto;`需要的时候添加滚动条
5. 对于定位的盒子要慎用，会切掉框架外的内容



# 精灵图
1. 精灵技术：将网页中的一些小背景图像整合到一张大图中，减少服务器的接受和发送请求的次数

## 精灵图使用
1. 主要针对背景图片使用，把多个小的背景图片整合到一张大图中
2. sprite：精灵图或者雪碧图，集成的大图
3. 通过移动背景图片的方式选择精灵图中的小图，`background-position`
4. 往上往左移动为负值



# 字体图标
1. 主要用于显示网页中通用、常用的一些小图标
2. 展示的是一个图标，但本质是文字

## 字体图标优点
1. 轻量级：一旦加载了，图标会马上渲染出来，减少服务器请求
2. 灵活性
3. 兼容性：支持所有浏览器

## 字体图标下载
1. [icomoon字体库](https://icomoon.io/)
2. [iconfont字体库](https://www.iconfont.cn/)

## 字体图标引入
1. 把下载包里面的fonts文件夹放在CSS文件的根目录下
2. 字体声明
```CSS
@font-face {
  font-family: 'icomoon';
  src:  url('fonts/icomoon.eot?p4ssmb');
  src:  url('fonts/icomoon.eot?p4ssmb#iefix') format('embedded-opentype'),
    url('fonts/icomoon.ttf?p4ssmb') format('truetype'),
    url('fonts/icomoon.woff?p4ssmb') format('woff'),
    url('fonts/icomoon.svg?p4ssmb#icomoon') format('svg');
  font-weight: normal;
  font-style: normal;
  font-display: block;
}
```

## 字体图标追加
1. 把压缩包里的selection.json重新上传，再下载压缩包替代原文件



# CSS三角

## 原理
1. 在宽高都为0的盒子设置border时会产生三角形

## 代码
```CSS
div {
    width: 0;
    height: 0;
    border: 50px solid transparent;
    border-left-color: pink;
}
```

## 定位
1. 子绝父相
2. 要移动border的两倍



# 用户界面样式
1. 界面样式：更改用户操作样式

## 鼠标样式
1. 设置鼠标在对象上时的光标形状
2. 语法`选择器 {cursor: pointer}`
![常见鼠标样式.jpg](https://i.loli.net/2021/03/06/l8j6G5TQZaEtXWb.jpg)

## 表单轮廓线
1. 取消表单轮廓线 `outline: none;`

## 固定文本域
2. 防止拖动文本域`resize: none;`



# vertical-align
1. 图片和表单的垂直居中
2. 设置元素的垂直对齐方式，只针对行内元素或者行内块元素有效
3. 语法`vertical-align : 参数`
4. baseline：默认，元素放置在父元素的基线上
5. top：顶线对齐
6. middle：中线对齐
7. bottom：底线对齐

## 图片底侧空白间隙
1. vertical-align不选择基线对齐
2. 把图片转换成块级元素



# 溢出文字省略号显示

## 单行文本溢出
1. 强制一行内显示文本`white-space: nowrap;`
2. 超出部分隐藏`overflow: hidden;`
3. 文字用省略号替代超出的部分`text-overflow: ellipsis;`

## 多行文本溢出
1. 有比较大兼容性问题，适合webKit浏览器或移动端
```CSS
{
    overflow: hidden;
    text-overflow: ellipsis;
    /* 弹性伸缩盒子模型显示 */
    display: -webkit-box;
    /* 限制在一个块元素显示的文本行数 */
    -webkit-line-clamp:2;
    /* 设置或检索伸缩盒对象的子元素排列方式 */
    -webkit-box-orient: vertical;    
}
```



# 布局技巧

## margin负值运用
1. 解决盒子边框变粗的问题：向左移动使右边的盒子边框压住左边盒子边框
2. `margin-left: -1px;`
3. 在使用这个技巧时，添加hover属性变化，左边的盒子有边框不能展示
4. 添加相对定位
5. `position: relative;`
6. 如果盒子里有定位，则提高盒子的层级
7. `z-index: 1`

## 文字围绕浮动元素
1. 巧妙应用浮动元素不会压住文字的技巧
2. 图片添加浮动，文字为标准流



# CSS初始化

## 标签内外边距清零
```CSS
* {
    margin: 0;
    padding: 0;
}
```

## 斜体文字不倾斜
```CSS
em,
i {
    margin: 0;
    padding: 0;
}
```

## 去掉列表格式
```CSS
li {
    list-style: none;
}
```

## 图片初始化
```CSS
img {
    border: 0;
    vertical-align: middle;
}
```

## 按钮鼠标样式手
```CSS
button {
    cursor: pointer;
}
```

## 链接初始化
```CSS
a {
    color: #666;
    text-decoration: none;
}
a:hover {
    color:#c81623
}
```

## 主页面初始化
```CSS
body {
    /* 文字抗锯齿 */
    -webkit-font-smoothing: antialiased;
    background-color: #fff;
    font: 12px/1.5 Microsoft YaHei
    color: #666;
}
```

## 清除浮动
```CSS
.clearfix:after {
    visibility: hidden;
    clear: both;
    display: block;
    content: ".";
    height: 0;
}
```



# CSS3新特性
1. 有兼容性问题，ie9+才支持
2. 移动端支持优于PC端

## CSS3新增选择器
### 属性选择器
1. 根据元素特定的属性选择元素
![属性选择器.jpg](https://i.loli.net/2021/03/15/hxsZJpR3SmcyNr8.jpg)
2. 语法`标签名[att]`
### 结构伪类选择器
1. 根据文档结构来选择元素，常用于根据父级选择器里面的子元素
![结构伪类选择器.jpg](https://i.loli.net/2021/03/15/KHjrG7fevaTNsnM.jpg)
2. nth-child(n)可以选择某个父元素的一个或多个特定的子元素
    + n可以是数字，关键字和公式
    + n如果是数字，就是选择第n个子元素，序号从1开始
    + n可以是关键字：even偶数；odd奇数`父类选择器 子类选择器:nth-chile(even/odd)`
    + n可以是公式，n是一个从0开始每次+1往后计算的；此处必须是n不能是其他字母
    + 会把父类的所有孩子都标上序号，执行时先看nth-child(n)，再看子类选择器是否匹配
3. nth-of-type(n)会把指定了元素的孩子标上序号，先看子类选择器，再看后面的n
### 伪元素选择器
1. 利用CSS创建新标签元素，不需要HTML标签，简化HTML结构
![常见伪元素选择器.jpg](https://i.loli.net/2021/03/16/XIuNozyJB2fRZmt.jpg)
2. before和after创建一个元素，但属于行内元素
3. 新创建的这个元素在文档树中是找不到的，所以我们称为伪元素
4. 语法`element::before{}`
5. 里面必须写content属性，里面写文字内容
6. before在父元素内容的前面创建元素，after在父元素内容的后面插入元素
7. 伪元素选择器和标签选择器一样，权重为1
8. 可以用来清除浮动

## CSS3盒子模型
1. CSS3中可以通过box-sizing来指定盒子模型，有两个值：content-box;border-box
2. box-sizing默认是content-box，盒子大小=width+padding——border
3. box-sizing为border-box时，盒子最终大小为width；但有前提：padding+border< width

## CSS3滤镜filter
1. filter CSS属性将模糊或颜色偏移等图形效果应用于元素
2. 语法`filter 函数();`
3. blur()函数模糊处理，数值越大越模糊

## CSS3 calc函数
1. calc()函数让声明一些CSS属性值时执行一些计算

## CSS3过渡
1. 过渡动画:从一个状态渐渐得过渡到另一个状态
2. 语法`transition: 要过渡的属性 花费时间 运动曲线 何时开始`
3. 属性：想要变化的css属性，宽度高度 背景颜色 内外边距 要想所有属性直接写all
4. 花费时间：单位是秒，必须写单位
5. 运动曲线：默认是ease
6. 何时开始：单位是秒（必须写单位）可以设置延迟触发时间，默认是0s
7. 谁来变换给谁加transition，不写在:hover里
8. 如果需要多个属性，用逗号分隔

## CSS3转换transform
### 2D转换
1. 2D转换是改变标签在二维平面上的位置和形状的一种技术
2. 同时写的时候要把位移先写
#### 移动：translate
1. 改变元素在页面中的位置
2. 语法`transform: translate(x,y) |transform: translateX(n)`
3. 定义2D转换中的移动，沿着X和Y轴移动元素
4. 最大优点：不会影响其他元素的位置
5. 百分比单位是相对于自身元素的
6. 对行内标签没有效果
#### 旋转：rotate
1. 让元素在2维平面内顺时针旋转或者逆时针旋转
2. 语法`transform: rotate(度数)`
3. rotate里面写度数，单位是deg，且不能省略
4. 角度为正，顺时针旋转
5. 默认旋转中心是元素的中心点
#### 设置元素转换中心点
1. 语法`transform-origin: x y;`
2. 后面的参数x、y要用空格隔开
3. x y默认转换的中心点是元素的中心点（50% 50%）
4. 还可以给x y设置像素或者方位名词
#### 缩放：scale
1. 控制元素的放大还是缩小
2. 语法`transform: scale(x,y)`
3. x、y用逗号隔开
4. `transform: scale(1,1)`不变，`transform: scale(2,2)`放大一倍
5. 如果只写一个参数则默认两个参数一致
6. 优势：可以设置转换中心点，默认以中心点缩放。而且不影响其他盒子