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

## v-show
1. 语法
```
data(){
    return{
        show:true,
    }
},
template:`
    <h2 v-show="show">JSPang.com</h2>  
`
```
2. 与v-if之间的区别
   + v-if更加灵活，可以增加多个判断，比如v-else-if和else，而v-show不具备这样的灵活性
   + v-show控制DOM元素显示，其实控制的是css样式，也就是display:noe。现在你可以把data的值修改为false，然后刷新浏览器，打开浏览器调试器的Elements选项卡，就可以清楚的看到，这时候<h2>标签上的style样式就是display:none

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

# 模板样式绑定
## 普通字符串绑定样式
```
<h2 v-bind:class="classString">JSPang.com</h2>
<h2 :class="classString">JSPang.com</h2>
```
## 对象形式绑定样式
```
data(){
    return {
        classObject:{red:true,background:true}
    }
},
template:`
    <h2 :class="classObject">JSPang.com</h2>  
`
```
## 数组的绑定方式
```
data(){
    return {
        classArray:['green','background'],
    }
},
template:`
    <h2 :class="classArray">JSPang.com</h2>  
`
```
2. 数组中还可以嵌套对象`classArray:['green','background',{red:true}],`
## 行内样式绑定方式
```
data(){
    return{
       //.....
        styleString:'color:orange;',
        styleObject:{
            color:'red',
            background:'yellow'
        }
    }
},
template:`
    <h2 :style="styleString">JSPang.com</h2>
`
```
## 子组件样式绑定
1. 定义子组件
```
app.component('sonCom',{
    template:`
        <div>SonCom</div>
    `
})
```
2. 父组件调用子组件
```
template:`
    <h2 :class="classArray">JSPang.com</h2>
    <sonCom />
`
```
3. 子组件添加样式
   + 子组件加上class
```
app.component('sonCom',{
    template:`
        <div class="green">SonCom</div>
    `
})
```
   + 把class写在调用子组件的地方
```
template:`
    <h2 :class="classArray">JSPang.com</h2>
    <sonCom class='green' />
`
```
如果子组件有多个根元素就不起作用了


# v-for循环
## 语法
1. 循环列表
```
template:`
    <ul>
        <li v-for="(item,index)  in listArray">[{{index}}]{{item}}</li>
    </ul>
`
```
2. 循环对象
```
<ul>
    <li v-for="(value,key,index)  in listObject" :key="key">
        [{{index}}]{{value}}-{{key}}
    </li>
</ul>
```
3. 循环数字
```
<span v-for="count in 99">{{count}},</span>
```

## 循环key值
为了提高循环时性能，在数组其中一项变化后，整个数组不进行全部重新渲染，Vue提供了绑定key值的使用方法，目的就是增加渲染性能，避免重复渲染。
```
<ul>
    <li v-for="(item,index)  in listArray" :key="index+item">
        [{{index}}]{{item}}
    </li>
</ul>
```
官方不建议使用索引index为key值，但此时又为了保持唯一性，所以这里使用了index+item进行绑定key值

## v-for使用判断
1. 直接在v-for中使用v-if时没有效果，因为v-for循环的优先级要高于v-if判断的优先级，所以判断失效。
2. 语法
```
<ul>
    <div
        v-for="(item,index) in listArray"
        :key="index+item"
    >
    <li v-if="item != '谢大脚'">
        [{{index}}]{{item}}
    </li>
    </div>
</ul>
```
但这种渲染方法会造成多个div标签
3. template标签
```
<ul>
    <template
        v-for="(item,index) in listArray"
        :key="index+item"
    >
    <li v-if="item != '谢大脚'">
        [{{index}}]{{item}}
    </li>
    </template>
</ul>
```



# 绑定事件
## 绑定事件的方法和参数
`<button @click="响应方法名">增加一位佳丽</button>`
1. 在方法需要多个参数的时候需要用逗号隔开，这时候你还想使用event参数，那需要如何编写那，方法是参数增加$event
2. 一个按钮也可以调用多个方法，方法名之间用逗号隔开。不传递任何参数也要写括号

## 事件修饰符
### stop修饰符
在Vue中要停止冒泡是非常简单的，只要加加一个事件修饰符stop就可以了。
`<button @click.stop=" addCountClick()">增加一位佳丽</button>`
### self修饰符
只有点击自己的时候才会被执行。 只不过加的位置要在家外层DOM元素的事件上。
```
template:`
        <div @click.self="handleBtnClick1">
            <div>目前已点佳丽数量{{count}}.</div>
            <button @click=" addCountClick()">增加一位佳丽</button>
       </div>
        `
```
### prevent修饰符
阻止默然行为的修饰符
### capture修饰符
改成捕获模式，默认的模式都是冒泡模式，也就是从下到上，但是你用capture后，是从上到下的
### once修饰符
事件只执行一次
### passive修饰符
解决滚动时性能的修饰符

## 绑定按键
### 语法
```
template:`
    <div">
        <input @keydown="handleKeyDown"/>
    </div>
    `
```
### 按键修饰符
#### 单个响应按键修饰符
```
template:`
    <div">
        <input @keydown.enter="handleKeyDown"/>
    </div>
    ` 
    })
```
类似这样只响应单个按键的修饰符有很多
enter 、tab、delete、esc、up 、down、left、right

## 鼠标修饰符
```
<div @click.right="handleClick">JSPang.com</div>
```
最常用的就是: left、right、middle



# 表单双向绑定 v-model
## input数据双向绑定
```HTML
<script>
    const app=Vue.createApp({ 
    data(){
        return{
            name:''
        }
    },
    template:`
        <div>
            <div>{{name}}</div>
            <input v-model="name" />
        </div>
        ` 
    }) 
    const vm=app.mount("#app")
</script>
```

## textarea数据双向绑定
```HTML
<script>
    const app=Vue.createApp({ 
    data(){
        return{
            name:''
        }
    },
    template:`
        <div>
            <div>{{name}}</div>
            <div><textarea v-model="name" /></div> 
        </div>
        ` 
    }) 
    const vm=app.mount("#app")
</script>
```

## checkbox数据双向绑定
```HTML
<script>
    const app=Vue.createApp({ 
    data(){
        return{
            girls:[]
        }
    },
    template:`
        <div>
            {{girls}}
            大脚<input type="checkbox" v-model="girls" value="大脚" />
            刘英<input type="checkbox" v-model="girls" value="刘英" />
            晓红<input type="checkbox" v-model="girls" value="晓红" />
        </div>
        ` 
    }) 
    const vm=app.mount("#app")
</script>
```
### true-value和false-value
```HTML
<script>
    const app=Vue.createApp({ 
    data(){
        return{
            girls:[]
        }
    },
    template: `
        <div>{{name}}
        <input type="checkbox" v-model="name"  true-value="JSPang.com"false-value="技术胖"/>
        </div>
`
    }) 
    const vm=app.mount("#app")
</script>
```
## Radio数据双向绑定
```HTML
<script>
    const app=Vue.createApp({ 
    data(){
        return{
            girl:''
        }
    },
    template:`
        <div>
            {{girl}}
            大脚<input type="radio" v-model="girl" value="大脚" />
            刘英<input type="radio" v-model="girl" value="刘英" />
            晓红<input type="radio" v-model="girl" value="晓红" />
        </div>
        ` 
    }) 
    const vm=app.mount("#app")
</script>
```
## v-model修饰符
### lazy修饰符
不马上显示，输入失去焦点后双向绑定的数据再改变
`<div>{{message}}<input v-model.lazy="message" /></div>`
### number修饰符
你输入的值只要是数字，就变成了number类型
如果你输入的是字母，它还会是字符串类型
`<div>{{typeof message}}<input v-model.number="message" /></div>`
### trim修饰
自动给我们去除前后的空格
`<div>{{message1}}<input v-model.trim="message1" /></div>`