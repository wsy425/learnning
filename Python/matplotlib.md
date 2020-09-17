# 基础绘图

## 曲线图

原理：描点呈现，只要输入x、y的两个list就可以了

`plt.plot(x,y)`呈现x、y的映射

## 直方图

用hist绘制直方图，需要串入一个数组和分类数量参数bins

`plt.hist(x,bins= 30) #将x数据分成30组` 

## 散点图

scatter函数传入x、y数组

`plt.scatter(x,y)`

## 饼状图

将一个list传入pie函数，plot会根据list中各数字占list数据和的比例绘制饼状图

`plt.pie(a)`

# 绘图标注

## 颜色

`plt.plot(x,y,color = 'green')`加入color参数即可设定绘图颜色

颜色的表示有以下几种

1. 常见颜色缩写：绿色（g）、红色（r）、蓝色（b）、黄色（y）
2. 查阅[相关文档](https://www.cnblogs.com/I-AM-DUMBASS/p/13229898.html)
3. 16进制RGB表示颜色

## 标记

给数据位置特定图形

`plt.plot(x,y,marker='o')`

[具体标记符号见](https://stackoverflow.com/questions/8409095/set-markers-for-individual-points-on-a-line-in-matplotlib)

## 线条

`plt.plot(x,y,linestyle='--')`虚线

## 上述三种合一

`plt.plot(x,y,'og--')`o型标记、绿色、虚线



