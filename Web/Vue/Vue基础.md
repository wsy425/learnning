# Vue基础
## 官方实例
```HTML
<div id="app">
        <!-- 渲染Vue元素到页面 -->
        {{ message }}
</div>
<!-- 导入Vue -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    var app = new Vue({
        el: '#app',
        data: {
          message: '你好'
        }
      })   
    </script>
```
## el属性
1. el挂载点，通过css选择器设置Vue实例管理的元素
2. Vue会管理el选项命中的元素及其内部的后代元素
3. 可以使用所有的选择器，但建议使用ID选择器
4. 可以使用其他的双标签，但不能使用HTML和BODY

## data属性
1. data数据对象
2. Vue中用到的数据定义在data中
3. data中可以写复杂类型的数据
4. 渲染复杂类型数据时遵守js语法即可



# 本地应用
1. Vue指令是以v-开头的一组特殊语法

## v-text
1. 设置标签的内容（textContent）
2. 默认写法会替换全部内容
3. 差值表达式{{}}可以替换指定内容
4. 内部支持写表达式
5. 例子
```HTML
<div id="app">
        <!-- 替换全部内容且支持字符串拼接，但要注意引号的使用 -->
        <h2 v-text="message+'!'"></h2>
        <!-- 替换部分内容也支持字符串拼接，对引号使用没有限制 -->
        <h2>成都{{message+"!"}}</h2>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    var app = new Vue({
        el: '#app',
        data: {
          message: '你好'
        }
      })   
    </script>
```

## v-html
1. 设置标签的innerHTML
2. 内容中有html结构会被解析为标签
3. v-text指令无论内容是什么只会解析为文本
4. 解析文本使用v-text，解析html结构使用v-html
5. 例子
```HTML
<div id="app">
        <!-- 普通文本和v-text没区别 -->
        <p v-html="message"></p>
        <!-- 可以渲染html结构 -->
        <p v-html="content"></p>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
var app = new Vue({
    el: '#app',
    data: {
        message: '你好',
        content:"<a href='#'>你好</a>"
        }
    })   
</script>
```

## v-on
1. 为元素绑定事件
2. 语法`v-on:事件名="方法"`或者简写为`@事件名="方法"`
3. 事件名不需要写on
4. 绑定的方法定义在methods属性中
5. 方法内部通过this关键字可以访问定义在data中数据
6. 例子
```HTML
<div id="app">
    <!-- 一般写法 -->
    <input type="button" value="事件绑定" v-on:click="dolt">
    <!-- 简写写法 -->
    <input type="button" value="事件绑定" @click="dolt">
    <!-- Vue只考虑数值不考虑DOM -->
    <h2 @click="change">{{food}}</h2>
</div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script>
var app = new Vue({
    el: '#app',
    data:{
          food:"123"
        },
    // 和el一级
    methods:{
        dolt:function(){
            alert('你好')
            },
        change:function(){
            // this关键词获取元素，不用考虑DOM
            this.food+='12'
        }
    })   
</script>
```

## v-show
1. 根据表达式的真假切换元素的显示和隐藏
2. 原理是修改元素的display实现显示隐藏
3. 指令后面的内容都为解析为布尔值
4. 值为true显示；false隐藏
5. 数据改变后，对应元素显示状态同步更新
```HTML
    <div id="app">
      <input type="button" value="切换显示状态" @click="changeIsShow">
      <input type="button" value="累加年龄" @click="addAge">
      <!-- v-show输入数据 -->
      <img v-show="isShow" src="pic.png" alt="">
      <!-- v-show输入表达式 -->
      <img v-show="age>=18" src="pic.png" alt="">
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    var app = new Vue({
        el: '#app',
        data:{
          isShow: false,
          age: 17
        },
        methods:{
          changeIsShow:function(){
            this.isShow = !this.isShow;
          },
          addAge:function(){
            this.age++;
          }
        }
      })
```

## v-if
1. 根据表达值的真假切换元素的显示状态（操纵dom元素）
2. 本质是通过dom元素来切换显示状态
3. 值为true显示；false隐藏
4. 频繁切换使用v-show，反之使用v-if；前者切换消耗小
```HTML
    <div id="app">
      <input type="button" value="切换显示状态" @click="changeIsShow">
      <input type="button" value="累加年龄" @click="addAge">
      <!-- v-if输入数据 -->
      <img v-if="isShow" src="pic.png" alt="">
      <!-- v-if输入表达式 -->
      <img v-if="age>=18" src="pic.png" alt="">
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    var app = new Vue({
        el: '#app',
        data:{
          isShow: false,
          age: 17
        },
        methods:{
          changeIsShow:function(){
            this.isShow = !this.isShow;
          },
          addAge:function(){
            this.age++;
          }
        }
      })
```

## v-bind
1. 设置元素的属性
2. 语法`v-bind:属性名=表达式`
3. 简写语法`:属性名=表达式`
4. class属性建议使用对象的方式
```HTML
    <style>
      .active{
        border:1px solid red;
      }
    </style>

    <div id="app">
        <!-- 设置地址属性 -->
      <img v-bind:src="imgSrc" alt="">
      <br>
      <!-- 简写设置地址属性 -->
      <!-- 设置title属性，可以使用字符串拼接 -->
      <!-- 使用三元表达是设置class属性 -->
      <img :src="imgSrc" alt="" :title="imgTitle='!" :class="isActive?'active':''" @click="toggleActive">
      <br>
      <!-- 使用对象的方式设置class属性 -->
      <img :src="imgSrc" alt="" :title="imgTitle='!" :class="{active:isActive}" @click="toggleActive">
    </div>
    <!-- 开发环境版本，包含了有帮助的命令行警告 -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
    var app = new Vue({
        el: '#app',
        data:{
          imgSrc: "pro_07.jpg",
          imgTitle:"你不知道她的故事",
          isActive:false
        },
        methods: {
          toggleActive:function(){
            isActive = !isActive
          }
        }
      })   
    </script>
```

## v-for
1. 根据数据生成列表结构
2. 数组经常和v-for结合使用
3. 语法`v-for = "(item,index) in 数据"`
4. item和index可以结合其他指令一起使用 
5. 数组长度的更新会同步到页面上，是响应式的