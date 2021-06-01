# Vue挂载
## creatAPP()
1. 创建Vue应用
2. 接收一个对象参数
## mount()
1. 将Vue应用挂载到指定的HTML的DOM节点上。
2. 接收一个字符串参数，参数使用CSS选择器，一般使用ID选择器
## 根元素
1. vm
## Vue设计模式
1. Vue的设计模式是mvvm
2. m：model，数据
3. v：view，视图
4. vm：viewModel，数据视图连接层

# 生命周期函数
1. 生命周期函数：在**某一时刻**会**自动执行**的函数
2. 自动执行：不需要触发事件就可以触发
![声明周期函数](https://newimg.jspang.com/Vuelifecycle.png)
3. 红色的都是生命周期函数
4. beforeCreate( ) ：在实例生成之前会自动执行的函数
5. created( ) : 在实例生成之后会自动执行的函数
6. beforeMount( ) : 在应用挂载、模板渲染完成之前执行的函数
7. mounted( ) : 在应用挂载、模板渲染完成之后执行的函数
8. beforeUpdate()：当data中的数据变化时， 会立即自动执行的函数
9. updated()：当data中的数据发生变化，页面重新渲染完后，会自动执行的函数
10. beforeUnmount( ) :当Vue应用失效时，会自动执行的函数
11. unmounted() : 当Vue应用失效时，且DOM完全销毁之后，会自动执行

# 模板语法
## 插值表达式
1. 字面量，使用`{{message}}`格式将data中的变量展示在模板里
2. 这样的插值表达式是双向绑定的，随着data值变化
3. 可以使用JS表达式，最常用的是三元运算符`<div>{{count>2?'大':'小'}}</div>`

## v-html
1. 插值表达式输出变量的html标签效果
2. 语法
```
template:`<h2 v-html="message"> </h2>`
```
3. 要注意template需要使用``而不是""

## v-once
1. 只有在第一次渲染去data中的值，而以后不再跟随data变化
```
template: `<h2 
                v-on:click="handleItemClick" 
                v-html="message"
                v-once
            > </h2>`
```

## v-bind
1. 对属性绑定data里的值，防止被当作字符串直接读取
```
v-bind:title="message"
```
2. 简写`:`

## v-on
1. 用来绑定响应事件的`<h2 @click="hanldClick">{{message}}</h2>`
2. 简写`@`

## v-if与v-else
1. v-if在符合要求时显示
```
template: `
<h2 @click="handleItemClick" v-if="message=='jspang.com'" class="one" > {{message}} </h2>
<h2 @click="handleItemClick" v-if="message=='技术胖'" class="two"> {{message}} </h2>
<h2 @click="handleItemClick" v-if="message=='bilibili'"  class="three"> {{message}} </h2>
    `
```
2. v-else不满足要求时显示
```
template: `
<h2 @click="handleItemClick" v-if="message=='jspang.com'" class="one" > {{message}} </h2>
<h2 @click="handleItemClick" v-else  class="three"> {{message}} </h2>
    `
```
3. 三元运算符进行判断DOM都存在，只是控制class
4. v-if时DOM只存在一个

## 模板动态参数
1. 通过[]将data里的变量括起来就可以将其绑定到属性名上
```
const app=Vue.createApp({ 
    data(){
        return{
            message:'jspang.com' ,
            name:'title',
            event:'click'
        }
    },
    //.........
    template:`
        <h2 
            @[event]="hanldClick"
            :[name]="message"
        >
        {{message}}
        </h2>
    `
})
```

## 阻止默认事件
1. 通过对事件添加e.preventDefault，和阻止冒泡事件类似
```
methods:{
    hanldeClick(){
        alert('欢迎光临红浪漫')
    },
    hanldeButton(e){
        e.preventDefault()
    }
},
//...
template:`
      //....
<form action="https://jspang.com" @click="hanldeButton">
    <button type="submit">默认提交</button>
</form>
`
```
2. 简化方法：模板修饰符
```
<form action="https://jspang.com" @click.prevent="hanldeButton">
    <button type="submit">默认提交</button>
</form>
```
3. prevent就是阻止默认事件的修饰符



# 计算属性
1. 计算属性的特性：当计算属性依赖的内容发生改变时才会重新执行计算
2. methods里的内容只要页面中一个变量重新渲染，其他的会一起重新执行一边
3. 语法
```Vue
computed:{
    方法名(){
    }
}
```

# 侦听器
1. watch侦听器的作用就是侦听一个data中的值的变化，变化后可以写一个方法，让其进行一些操作（业务逻辑的编写）
2. 语法
```
watch:{
    侦听data中值的名称(current,prev){
    }
},
```
3. 侦听器中的方法还可以接收两个参数，一个是现在的值（current），一个是变化之前的值（prev）
4. 计算属性computed必须要返回一个值，而且在页面渲染的同时就会执行里边的业务逻辑，也就是会先执行一遍你写的业务逻辑，而watch只有发生变化时才会执行，也就是说值没有变化，它是不执行里边业务逻辑的。
5. computed 和 method都能实现的功能，建议使用computed,因为有缓存，不用渲染页面就刷新。
6. computed 和 watch 都能实现的功能，建议使用 computed，因为更加简洁。