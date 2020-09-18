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

## 标题

### 基础设置：`plt.title('标题')`

### 子图设置标题

```python
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.set_title('line')
ax2.set_title('logistic')
plt.subplots_adjust(hspace=0.5) #调节子图之间的间隙
ax1.plot(rang(10))
ax2.plot(x,y)
plt.show()
```

### 标题参数

1. fontsize字体大小
   * 数字代表字体大小，默认为12
   * 字符串确定字体大小：'xx-small', 'x-small', 'small', 'medium', 'large','x-large', 'xx-large'
2. fontweight字体粗细：常用的选项有：['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black'] 。bold就是加粗，semibold是半加粗，heavy是重加粗，black就是全黑了
3. verticalalignment竖直对齐方式：'center' , 'top' , 'bottom' ,'baseline' 
4. horizontalalignment水平对齐方式：[left,right,center]
5. rotation旋转角度：输入数字代表旋转角度
6. alpha透明度，参数在0到1之间
7. backgroundcolor背景颜色
8. bbox背景框：facecolor背景颜色，edgecolor线条颜色，boxstyle方框外形，edgewidth线条粗细

## 轴名称

`plt.xlabel('x轴名称')`

多个子图与标题一样

## 标签

调用legend方法，在绘图后加上laber参数

```python
plt.plot(x,x,laber = 'linear')
plt.plot(x,x**2,laber = 'quadratic')
plt.legend()
plt.show()
```

legend参数：常用的是loc，标签位置。

上中下为upper、center、lower；左中右为left、center、right，两两组合得到9中方位，再还有一种best，自适配最佳放置位置

# 图表设置

## xlim、ylim

设置坐标轴范围`plt.xlim(-5,5)`，不常用

## xticks、ytixks

既可以设置范围也可以设置每个刻度之间的间距，还可以设置坐标轴刻度及旋转角度

```python
#x从-10到10每隔5画一个点，标签为labers且旋转30°
plt.plot(x,x**2,label='quadratic')
plt.xlaber('x laber')
plt.ylaber('y laber')
labers = ['10 , 5 , 0 , 5 , 10']
plt.xicks(range(-10,15,5),laber=labers,rotation=30) #range前闭后开
```

在月报表等刻度为汉字的时候很有用