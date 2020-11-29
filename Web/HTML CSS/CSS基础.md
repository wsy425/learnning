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

# 文本缩进
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