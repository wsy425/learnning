# 1 Vue原理
## 1.1 Vue介绍与描述
Vue是一套用来动态*构建用户界面*的*渐进式*JavaScript框架
* 构建用户界面：把数据通过某种办法变成用户界面
* 渐进式：Vue可以自底向上逐层的应用，简单应用只需要一个轻量小巧的核心库，复杂应用可以引入各式各样的Vue插件

## 1.2 Vue特点
1. 遵循*MVVM*模式 
2. 编码简洁，体积小，运行效率高，适合移动/PC端开发 
3. 它本身只关注 UI，可以引入其它第三方库开发项目
4. 采用*组件化*模式，提高代码复用率、且让代码更好维护
5. *声明式编码*，让编码人员无需直接操作DOM，提高开发效率
6. 使用*虚拟DOM*和*Diff算法*，尽量复用DOM节点

## 1.3 与其他JS框架对比
1. 借鉴*angular*的*模板*和*数据绑定*技术
2. 借鉴*react*的*组件化*和*虚拟DOM*技术

## 1.4 MVVM模型
![Vue的MVVM模型图](https://cdn.nlark.com/yuque/0/2022/jpeg/1379492/1643097677438-36b4834c-18e8-4cd0-aa8e-c5f154e6bde0.jpeg?x-oss-process=image%2Fresize%2Cw_697%2Climit_0)
1. M：模型*Model*，data中的数据
2. V：视图*View*，模板代码
3. VM：视图模型*ViewModel*，Vue实例
4. data中所有的属性，最后都出现在了vm身上
5. *vm*身上所有的属性 及*Vue原型*身上所有的属性，在 Vue模板中都可以直接使用

## 1.5 Vue基础使用
1. 需要一个*root容器*，root容器里的代码被称为*Vue模板*
2. 就必须创建一个*Vue实例*，且要传入一个*配置对象*
3. Vue 实例与容器是*一一对应*的
4. {{xxx}}中的 xxx 要写*js表达式*，且 xxx 可以自动读取到data中的所有属性
5. 一旦*data*中的数据发生变化，那么模板中用到该数据的地方也会自动更新
```HTML
<body>
    <!-- root容器 -->
    <div id="demo">
        <h1>Hello，{{ name.toUpperCase() }}，{{ address }}</h1>
    </div>
</body>

<script>
    // 创建Vue实例
    new Vue ({
        el:'#demo' //el用于指定当前Vue实例为哪个容器服务，值通常为css选择器字符串
        data: {       // data中用于存储数据，数据供el所指定的容器去使用，值暂时先写成一个对象
            name: 'cess',
            address: '成都'
        }
    })
</script>
```
### 1.5.1 Vue实例挂载
1. 创建Vue实例对象的时候配置el属性
2. 先创建Vue实例，随后再通过`vm.$mount('#XXX')`挂载
### 1.5.2 Vue实例data
1. 对象式：`data:{ }`
2. 函数式：`data(){return {}}`
3. 使用组件的时候必须使用函数形式
4. 不能使用箭头函数，会导致this不再是Vue实例了

## 1.5 数据监视
### 1.5.1 Vue2数据监视
1. vue会监视data中所有层次的数据
2. 如何监测对象中的数据？
   1. 通过setter实现监视，且要在new Vue()时就传入要监测的数据 
   2. 对象创建后追加的属性，Vue默认不做响应式处理
   3. 如需给后添加的属性做响应式，请使用如下API
      1. `Vue.set(target,propertyName/index,value)`
      2. `vm.$set(target,propertyName/index,value)`
3. 如何监测数组中的数据？
   1. 通过包裹数组更新元素的方法实现，本质就是做了两件事
      1. 调用原生对应的方法对数组进行更新
      2. 重新解析模板，进而更新页面
4. 在Vue修改数组中的某个元素一定要用如下方法   
   1. push()pop()unshift()shift()splice()sort()reverse()这几个方法被Vue重写了
   2. Vue.set()或vm.$set()
5. Vue.set() 和 vm.$set() **不能**给vm或vm的根数据对象（data等）添加属性
6. 数据劫持：将写的data加工后添加getter和setter的过程，将数据劫持在getter和setter里了

## 1.6 生命周期
1. 又名生命周期回调函数、生命周期函数、生命周期钩子
2. 生命周期函数是Vue在关键时刻帮我们调用的一些特殊名称的函数
3. 生命周期函数的名字不可更改，但函数的具体内容是程序员根据需求编写的
4. 生命周期函数中的 this 指向是vm或组件实例对象
### 1.6.1 VUE2生命周期
![VUE2生命周期](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643297176928-5d5ac765-237c-462d-9188-84935e6c3c69.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)
```JavaScript
beforeCreate() {console.log('初始化但没有数据代理')},
created() {console.log('初始化且完成数据监测和数据代理')},
beforeMount() {console.log('虚拟DOM已经生成，但还没有转换为真实DOM')},
mounted() {console.log('VUE解析并把真实DOM挂载到页面上')},
beforeUpdate() {console.log('数据已经更新，但页面还未更新')},
updated() {console.log('页面和数据都更新完毕')},
beforeDestroy() {console.log('马上要销毁VUE实例')},
destroyed() {console.log('destroyed')},
```
1. 常用的生命周期钩子
   1. mounted发送ajax请求、启动定时器、绑定自定义事件、订阅消息等初始化操作
   2. beforeDestroy清除定时器、解绑自定义事件、取消订阅消息等收尾工作
2. 关于销毁Vue实例
   1. 销毁后借助Vue开发者工具看不到任何信息
   2. 销毁后自定义事件会失效，但原生DOM事件依然有效
   3. 一般不会在beforeDestroy操作数据，因为即便操作数据，也不会再触发更新流程了
### 1.6.2 VUE3生命周期
![VUE3生命周期](https://v3.cn.vuejs.org/images/lifecycle.svg)
1. Vue3.0中可以继续使用Vue2.x中的生命周期钩子，但有有两个被更名
   1.  `beforeDestroy`改名为 `beforeUnmount`
   2.  `destroyed`改名为 `unmounted`
2. Vue3.0也提供了 Composition API 形式的生命周期钩子，与Vue2.x中钩子对应关系如下
   1. `beforeCreate`===>`setup()`
   2. `created`=======>`setup()`
   3. `beforeMount` ===>`onBeforeMount`
   4. `mounted`=======>`onMounted`
   5. `beforeUpdate`===>`onBeforeUpdate`
   6. `updated` =======>`onUpdated`
   7. `beforeUnmount` ==>`onBeforeUnmount`
   8. `unmounted` =====>`onUnmounted`

---


# 2. Vue核心
## 2.1 模板语法
Vue模板语法包括两大类
### 2.1.1 插值语法
1. 功能：用于解析标签体内容
2. 写法：`{{xxx}}`，xxx 是 js 表达式，可以直接读取到 data 中的所有区域
### 2.1.2 指令语法
1. 功能：用于解析标签（包括：标签属性、标签体内容、绑定事件…）  
2. 写法：通过vue的指令将数据绑定到模板上，例如`v-bind:`可以给标签里的属性绑定数据

## 2.2 数据绑定
Vue中有2种数据绑定方法
### 2.2.1 单向数据绑定
1. `v-bind`数据只能从data流入页面
2. 可以简化为`:`
### 2.2.2 双向数据绑定
1. `v-model`数据不仅能从 data 流向页面，还可以从页面流向 data
2. `v-model:value`可以简写为`v-model`，因为v-model默认收集的就是value值
3. 双向绑定一般都应用在*表单类元素*上，如< input>< select>< textarea>等
### 2.2.3 收集表单数据
1. 若`<input type="text"/>`，则v-model收集的是value值，用户输入的内容就是value值
2. 若`<input type="radio"/>`，则v-model收集的是value值，且要给标签配置value属性
3. 若`<input type="checkbox"/>`
   1. 没有配置value属性，那么收集的是checked属性（勾选 or 未勾选，是布尔值）
   2. 配置了value属性
      1. v-model的初始值是非数组，那么收集的就是checked（勾选 or 未勾选，是布尔值）
      2. v-model的初始值是数组，那么收集的就是value组成的数组
4. v-model修饰符
   1. lazy	失去焦点后再收集数据
   2. number输入字符串转为有效的数字
   3. trim	输入首尾空格过滤

## 2.3 数据代理
数据代理：通过一个对象代理对另一个对象中属性的操作（读写）
### 2.3.1 Vue数据代理原理
![Vue数据代理流程](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643033436297-5d2d61ec-ed69-4706-a98d-afdbd53b383d.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)

1. Vue中的数据代理通过vm对象来代理data对象中属性的操作（读/写）
2. Vue中数据代理的好处：更加方便的操作data中的数据
3. 基本原理
   * 通过`Object.defineProperty()`把data对象中所有属性添加到vm上
   * 为每一个添加到vm上的属性，都指定一个 getter setter
   * 在getter setter内部去操作（读/写）data中对应属性的值
   * 其中涉及到Vue将model里的data拷贝到vm的_data属性中，这是为了通过_data对data进行数据劫持，实现页面的响应式展示
### 2.3.2 数据代理原理
使用`Object.defineProperty()`方法在代理的对象中添加被代理对象需要被代理的属性
```JavaScript
let obj = {x:100} //被代理的对象
let propertyObj = {} //代理的对象
Object.defineProperty(propertyObj, 'x', {
    //读取propertyObj的x属性时触发
    get(){
        return obj.x
    }
    //修改propertyObj的x属性时触发
    set(value){
        obj.x = value
    }
})
```
### 2.3.3 Object.defineProperty()
```JavaScript
let person = {
    name:'张三',
    sex:'男',
}
let age = 18
// 为person对象添加属性,可以对添加的属性进行高级操作
Object.defineProperty(person, 'age', {
    value:18,  //属性赋值
    enumerable:true,   // 控制属性是否可以枚举，默认值是false
    writable:true,     // 控制属性是否可以被修改，默认值是false
    configurable:true  // 控制属性是否可以被删除，默认值是false
    //当有人读取person的age属性时，get函数(getter)就会被调用，且返回值就是age的值
    get(){
        return age
    }
    //当有人修改person的age属性时，set函数(setter)就会被调用，且会收到修改的具体值
    set(value){
        age = value
    }
})
```
## 2.4 事件处理
### 2.4.1 事件的基本用法
1. 使用`v-on:XXX`或`@XXX`绑定事件，其中XXX是事件名
2. 事件的回调需要配置到在methods对象中，最终会在vm上
3. methods中配置的函数，不要用箭头函数，否则 this 就不是vm了
4. methods中配置的函数，都是被 Vue所管理的函数，this 的指向是vm或组件实例对象
5. `@click="demo"`和`@click="demo($event)"`效果一致，但后者可以传参
### 2.4.2 事件修饰符
1. Vue中的事件修饰符
   1. prevent	阻止默认事件（常用）
   2. stop		阻止事件冒泡（常用）
   3. once		事件只触发一次（常用）
   4. capture	使用事件的捕获模式
   5. self		只有event.target是当前操作的元素时才触发事件
   6. passive	事件的默认行为立即执行，无需等待事件回调执行完毕
2. 修饰符可以连续写，比如可以这么用：`@click.prevent.stop="showInfo"`
### 2.4.3 键盘事件
1. 键盘上的每个按键都有自己的名称和编码，例如：Enter（13）。而Vue还对一些常用按键起了别名方便使用
2. Vue别名使用`@keyup.enter="XXX"`
3. . Vue中常用的按键别名
   1. 回车enter
   2. 删除delete捕获“删除”和“退格”键
   3. 退出esc
   4. 空格space
   5. 换行tab特殊，必须配合keydown去使用
   6. 上up；下down ；左left；右right
4. Vue未提供别名的按键，可以使用按键原始的key值去绑定，但注意要转为kebab-case（多单词小写短横线写法）
5. 系统修饰键（用法特殊）ctrlaltshiftmeta（meta就是win键）
   1. 配合keyup使用：按下修饰键的同时，再按下其他键，随后释放其他键，事件才被触发
   2. 指定 ctr+y 使用 @keyup.ctr.y
   3. 配合keydown使用：正常触发事件
6. 也可以使用keyCode去指定具体的按键（不推荐）
7. `Vue.config.keyCodes.自定义键名 = 键码`，可以去定制按键别名

## 2.5 计算属性computed
1. 定义：要用的属性不存在，需要通过已有属性计算得来
2. 原理：底层借助了`Objcet.defineproperty()`方法提供的getter和setter
3. `get`函数什么时候执行？
   1. 初次读取时会执行一次
   2. 当依赖的数据发生改变时会被再次调用
4. 优势：与methods实现相比，**内部有缓存机制**（复用），效率更高，调试方便 
5. 计算属性最终会出现在vm上，直接读取使用即可
6. 如果计算属性要被修改，那必须写set函数去响应修改，且set中要引起计算时依赖的数据发生改变
7. 如果计算属性确定不考虑修改，可以使用计算属性的简写形式
```JavaScript
const vm = new Vue({
  el: '#root',
  data: {
    firstName:'张',
    lastName:'三',
  },
  computed: {
  //   完整写法
    fullName: {
    	get() {
    		return this.firstName + '-' + this.lastName
    	},
    	set(value) {
    		const arr = value.split('-')
    		this.firstName = arr[0]
    		this.lastName = arr[1]
    	}
    }
    // 简写
    Name() {
      return this.firstName + '-' + this.lastName
    }
  }
})
```

## 2.6监视属性watch
### 2.6.1侦听属性基本用法
1. 当被监视的属性变化时，回调函数自动调用，进行相关操作
2. 监视的属性必须存在，才能进行监视，既可以监视data，也可以监视计算属性
3. 配置项属性`immediate:false`，改为 true，则初始化时调用一次`handler(newValue,oldValue)`
4. 监视有两种写法
   1. 创建Vue时传入`watch: {}`配置
   2. 通过`vm.$watch()`监视
```JavaScript
const vm = new Vue({
    el: '#root',
    data: {
      isHot: true,
    },
    // 方式一
    watch:{
        isHot:{
            immediate:true,
            handler(newValue,oldValue){
                console.log('isHot被修改了',newValue,oldValue)
            }
        }
    },
    methods:{
        changeWeather(){
            this.isHot = !isHot
        }
    },
    computed: {
        info(){
            return this.isHot ? '炎热' : '凉爽'
        }
    }
})
// 方式二
vm.$watch('isHot',{
    immediate:true,
    handler(newValue,oldValue){
        console.log('isHot被修改了',newValue,oldValue)
    }
})
```
### 2.6.2 深度监视
1. Vue中的watch默认不监测对象内部值的改变（一层）
2. 在watch中配置`deep:true`可以监测对象内部值的改变（多层）
3. Vue自身可以监测对象内部值的改变，但Vue提供的watch默认不可以
4. 使用watch时根据监视数据的具体结构，决定是否采用深度监视
5. 只监视多级结构中某个属性的变化`watch(){'numbers.a':{}'}`，key需要手动加''包裹
### 2.6.3 监视属性简写
如果监视属性除了handler没有其他配置项的话，可以进行简写
```JavaScript
watch:{
    isHot(newValue,oldValue){
    }
}
vm.$watch('isHot',(newValue,oldValue){
    console.log('isHot被修改了', newValue, oldValue, this)
})
```
### 2.6.4 computed与watch的区别
1. computed能完成的功能，watch都可以完成
2. watch能完成的功能，computed不一定能完成，例如watch可以进行异步操作
3. 所有被Vue管理的函数，最好写成普通函数，这样 this 的指向才是vm或组件实例对象
4. 所有不被Vue所管理的函数（定时器的回调函数、ajax 的回调函数等、Promise 的回调函数），最好写成箭头函数，这样 this 的指向才是vm或组件实例对象

## 2.7 样式绑定
### 2.7.1 绑定class样式
1. 写法：`:class="xxx"`，xxx 可以是字符串、数组、对象
2. 三种写法区别
   1. 字符串写法适用于：类名不确定，要动态获取 
   2. 数组写法适用于：要绑定多个样式，个数不确定，名字也不确定 
   3. 对象写法适用于：要绑定多个样式，个数确定，名字也确定，但不确定用不用 
### 2.7.2 绑定style样式
1. `:style="[a,b]"`其中a、b是样式对象
2. `:style="{fontSize: xxx}"`其中 xxx 是动态值

## 2.8 条件渲染
### 2.8.1 v-if
1. 写法 跟 if else 语法类似
   1. `v-if="表达式"`
   2. `v-else-if="表达式"`
   3. `v-else
2. 适用于：切换频率较低的场景，因为不展示的DOM元素直接被移除
3. 注意：`v-if`可以和`v-else-if` `v-else`一起使用，但要求结构不能被打断
### 2.8.2 v-show
1. 写法：`v-show="表达式"`
2. 适用于：切换频率较高的场景
3. 特点：不展示的DOM元素未被移除，仅仅是使用样式隐藏掉display: none
4. 使用v-if的时，元素可能无法获取到，而使用v-show一定可以获取到template标签不影响结构，页面html中不会有此标签，但只能配合v-if，不能配合v-sho

## 2.9 列表渲染
### 2.9.1 v-for指令
1. 用于展示列表数据
2. 语法：`<li v-for="(item, index) of items" :key="index">`，这里key可以是index，更好的是遍历对象的唯一标识
3. 可遍历：数组、对象、字符串（用的少）、指定次数（用的少）
### 2.9.2 key的作用与原理
![index做key的作用](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643033767087-2558e992-b48b-4b54-a9b8-86eb8534bd98.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)
![id做key的作用](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643033764359-6a37a493-bb51-4b3b-8b14-822a3df68d6e.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)
1. 虚拟DOM中key的作用：key是虚拟DOM中对象的标识，当数据发生变化时，Vue会根据新数据生成新的虚拟DOM，随后Vue进行新虚拟DOM与旧虚拟DOM的**差异比较**
2. 对比规则
   1. 旧虚拟DOM中找到了与新虚拟DOM相同的key
      1. 若虚拟DOM中内容没变, 直接使用之前的真实DOM
      2. 若虚拟DOM中内容变了, 则生成新的真实DOM，随后替换掉页面中之前的真实DOM
   2. 旧虚拟DOM中未找到与新虚拟DOM相同的key
创建新的真实DOM，随后渲染到到页面
3. 用index作为key可能会引发的问题
   1. 若对数据进行逆序添加、逆序删除等**破坏顺序操作**，会产生没有必要的真实DOM更新 ==> 界面效果没问题，但效率低
   2. 若结构中还包含**输入类的DOM**：会产生错误DOM更新 ==> 界面有问题
4. 开发中如何选择key
   1. 最好使用每条数据的**唯一标识作为key**，比如 id、手机号、身份证号、学号等唯一值
   2. 如果不存在对数据的逆序添加、逆序删除等破坏顺序的操作，仅用于渲染列表，使用index作为key是没有问题的
5. 如果代码没写key，vue就会自动把遍历的index作为key输入
### 2.9.2 列表过滤
1. `v-model`来双向绑定用户过滤的信息
2. watch实现
   1. 需要一个新的数组存储过滤后的内容，否则数据越来越少
   2. `immediate: true`上来就执行一次，这样过滤后的数组不需要初始给值。其核心原理是`任意字符串.indexOf(空字符串) = 0`
   3. `Array.filter((p)=>{ return p.indexOf(val)})`filter返回一个数组不改变原数组
3. computed实现
```JavaScript
computed:{
    filPersons(){
        return this.persons.filter((p)=>{
            return p.name.indexOf(this.keyword) !== -1
        })
    }
}
```
### 2.9.3 列表排序
1. 先过滤再排序，在同时存在过滤和排序需求的时候，排序还是维护过滤后的数据
```JavaScript
computed:{
    filPersons(){
        const arr =  this.persons.filter((p)=>{
            return p.name.indexOf(this.keyword) !== -1
        })
        if(this.sortType){
            arr.sort((p1,p2)=>{
                return this.sortType === 1 ? p2.age-p1.age : p1.age-p2.age
            })
        }
        return arr
    }
}
```

## 2.10 内置指令
### 2.10.1之前用过的
1. v-bind：单向绑定解析表达式，可简写为`:`
2. v-model:双向数据绑定
3. v-for:遍历数组 / 对象 / 字符串
4. v-on:绑定事件监听，可简写为@
5. v-show:条件渲染 (动态控制节点是否展示)
6. v-if:条件渲染（动态控制节点是否存存在）
7. v-else-if:条件渲染（动态控制节点是否存存在）
8. v-else:条件渲染（动态控制节点是否存存在）
### 2.10.2 v-text
1. 作用：向其所在的节点中渲染文本内容 
2. 与插值语法的区别：v-text会替换掉节点中的内容，{{xxx}}则不会
3. 不会解析数据里的html标签
### 2.10.3 v-html
1. 作用：向指定节点中渲染包含html结构的内容 
2. 与插值语法的区别： 
   1. v-html会替换掉节点中所有的内容，{{xxx}}则不会
   2. v-html可以识别html结构
3. 严重注意v-html有安全性问题！！！ 
   1. 在网站上动态渲染任意html是非常危险的，容易导致 XSS 攻击
   2. 一定要在可信的内容上使用v-html，永远不要用在用户提交的内容上！！！
### 2.10.4 v-cloak
1. 没有值
2. 本质是一个特殊属性，Vue实例创建完毕并接管容器后，会删掉v-cloak属性
3. 使用css配合v-cloak可以解决网速慢时页面展示出{{xxx}}的问题
### 2.10.5 v-once
1. v-once所在节点在初次动态渲染后，就视为静态内容了 
2. 以后数据的改变不会引起v-once所在结构的更新，可以用于优化性能
### 2.10.6 v-pre
1. 跳过v-pre所在节点的编译过程
2. 可利用它跳过：没有使用指令语法、没有使用插值语法的节点，会加快编译

## 2.11 自定义指令
1. directives配置项
```JavaScript
// 局部指令
new Vue({															
  directives:{ 
    指令名:配置对象 
  }   
})
new Vue({															
  directives:{ 
    指令名:(element,binding){} 
  }   
})
// 全局指令
Vue.directive(指令名, 配置对象)
Vue.directive(指令名, 回调函数)
```
2. element就是DOM元素
3. binding就是要绑定的对象，它包含以下属性：name、value、oldValue、expression、arg、modifiers
4. 用函数的形式定义时指令执行时间
   1. 指令与元素成功绑定时
   2. 指令所在的模板被重新解析时
5. 配置对象中常用的三个回调函数
   1. `bind(element, binding)`指令与元素成功绑定时调用
   2. `inserted(element, binding)`指令所在元素被插入页面时调用
   3. `update(element, binding)`指令所在模板结构被重新解析时调用
6. 指令定义时不加v-，但使用时要加v-
7. 指令名如果是多个单词，要使用kebab-case命名方式，不要用camelCase命名
8. 指令回调函数里的this都是window

## 2.12 ~~过滤器~~（Vue3已移除）
1. 定义：对要显示的数据进行特定格式化后再显示（适用于一些简单逻辑的处理）
2. 注册过滤器：
   1. Vue.filter(name, callback)全局过滤器
   2. new Vue {filters: {}} 局部过滤器
3. 使用过滤器：{{ xxx | 过滤器名}} 或 v-bind:属性 = "xxx | 过滤器名" 
4. 过滤器可以接收额外参数，多个过滤器也可以串联
5. 并没有改变原本的数据，而是产生新的对应的数据

## 2.13 $nextTick
1. 这是一个生命周期钩子
2. `this.$nextTick(回调函数)`在下一次DOM更新结束后执行其指定的回调
3. 什么时候用：当改变数据后，要基于更新后的新DOM进行某些操作时，要在nextTick所指定的回调函数中执行

## 过渡与动画
1. Vue封装的过度与动画：在插入、更新或移除DOM元素时，在合适的时候给元素添加样式类名
![Vue封装动画图示](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643034414605-e2a3f595-ac72-4c74-9f11-12e7578592c9.png)
2. 写法
   1. 准备好样式
      1. 元素进入的样式
         1. `v-enter`		 	进入的起点
         2. `v-enter-active`	进入过程中
         3. `v-enter-to`	 	进入的终点
      2. 元素离开的样式
         1. `v-leave`			离开的起点
         2. `v-leave-active`	离开过程中
         3. `v-leave-to`		离开的终点
   2. 使用`<transition>`包裹要过度的元素，并配置name属性，此时需要将上面样式名的v换为name 
   3. 要让页面一开始就显示动画，需要添加appear属性
3. 备注：若有多个元素需要过度，则需要使用`<transition-group>`，且每个元素都要指定key值



---

# 3 Vue组件化
## 3.1 组件化编程原理
### 3.1.1 模块
1. 理解：向外提供特定功能的 js 程序，一般就是一个 js 文件
2. 为什么：js 文件很多很复杂
3. 作用：复用、简化 js 的编写，提高 js 运行效率
4. 模块化：当应用中的 js 都以模块来编写的，那这个应用就是一个模块化的应用
### 3.1.2 组件
1. 定义：用来实现局部功能的代码和资源的集合（html/css/js/image…）
2. 为什么：一个界面的功能很复杂
3. 作用：复用编码，简化项目编码，提高运行效率
4. 组件化：当应用中的功能都是多组件的方式来编写的，那这个应用就是一个组件化的应用

## 3.2 非单文件组件
非单文件组件：一个文件中包含有 n 个组件
### 3.2.1 基本使用
1. 定义组件
使用Vue.extend(options)创建，其中options和new Vue(options)时传入的options几乎一样，但也有点区别
   1. el不要写，因为最终所有的组件都要经过一个vm的管理，由vm中的el才决定服务哪个容器
   2. data必须写成函数，避免组件被复用时，数据存在引用关系
2. 注册组件
   1. 局部注册：new Vue()的时候options传入components选项
   2. 全局注册：Vue.component('组件名',组件)
3. 使用组件：编写组件标签如`<school></school>`
### 3.2.3 组件注意事项
#### 关于组件名
1. 一个单词组成
   1. 第一种写法（首字母小写）：school
   2. 第二种写法（首字母大写）：School
2. 多个单词组成
   1. 第一种写法（kebab-case 命名）：my-school
   2. 第二种写法（CamelCase 命名）：MySchool（需要Vue脚手架支持）
3. 其他
   1. 组件名尽可能回避HTML中已有的元素名称，例如：h2、H2都不行
   2. 可以使用name配置项指定组件在开发者工具中呈现的名字
#### 关于组件标签
1. 第一种写法：`<school></school>`
2. 第二种写法：`<school/>`（需要Vue脚手架支持）
3. 备注：不使用脚手架时，`<school/>`会导致后续组件不能渲染
4. 一个简写方式：const school = Vue.extend(options)可简写为const school = options，因为父组件components引入的时候会自动创建
### 3.2.4 VueComponent
1. school 组件本质是一个名为VueComponent的构造函数，且不是程序员定义的，而是`Vue.extend()`生成的 
2. 我们只需要写`<school/>`或`<school></school>`，Vue 解析时会帮我们创建 school 组件的实例对象，即Vue帮我们执行的`new VueComponent(options)`
3. 每次调用Vue.extend，返回的都是一个全新的VueComponent，即不同组件是不同的对象
4. 关于 this 指向
   1. 组件配置中data函数、methods中的函数、watch中的函数、computed中的函数 它们的 this 均是 VueComponent实例对象
   2. new Vue(options)配置中：data函数、methods中的函数、watch中的函数、computed中的函数 它们的 this 均是 Vue实例对象
5. VueComponent的实例对象，以后简称vc（组件实例对象）Vue的实例对象，以后简称vm
6. 一个重要的内置关系：`VueComponent.prototype.__proto__ === Vue.prototype`,让组件实例对象vc可以访问到 Vue原型上的属性、方法
![vm与vc的关系](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643034116880-0c7ffd4b-f0ed-47b2-9638-3bb71344c4f1.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)

## 3.3 单文件组件
### 3.3.1 vue文件组成
```Vue
// 模板页面
<template>
    <div id='Demo'>
        <h2>学校名称：{{name}}</h2>
        <h2>学校地址：{{address}}</h2>
        <button @click="showName">点我提示学校名</button>
    </div>
</template>
// JS模块对象
<script>
    export default {
        name:'School',
        data() {
            return {
                name:'UESTC',
                address:'成都'
            }
        },
        methods: {
            showName(){
                alert(this.name)
            }
        },
    }
</script>
// 样式
<style>
    #Demo{
        background: orange;
    }
</style>
```
### 3.3.2 基本使用
1. 引入组件
2. 映射成标签
3. 使用组件标签
```Vue
<template>
    <div>
        <!--使用组件标签-->
        <School></School>
        <Student></Student>
    </div>
</template>

<script>
    // 引入组件
    import School from './School.vue'
    import Student from './Student.vue'

    export default {
        name:'App',
        // 映射成标签
        components:{
            School,
            Student
        }
    }
</script>
```

## 3.4 ref属性
1. ref被用来给元素或子组件注册引用信息（id的替代者）
2. 应用在html标签上获取的是真实DOM元素，应用在组件标签上获取的是组件实例对象vc
3. 使用方式
   1. 打标识：`<h1 ref="xxx"></h1>`或`<School ref="xxx"></School>`
   2. 获取：`this.$refs.xxx`

## 3.5 props 配置项
1. props让组件接收外部传过来的数据 
2. 传递数据`<Demo name="xxx" :age="18"/>`这里age前加:，通过v-bind使得里面的18是数字
3. 接收数据
   1. 第一种方式（只接收）props:['name', 'age'] 
   2. 第二种方式（限制类型）props:{name:String, age:Number}
   3. 第三种方式（限制类型、限制必要性、指定默认值
```JavaScript
props: {
    name: {
        type: String,	 // 类型
        required: true,// 必要性
        default: 'cess'// 默认值
    }
}
```
4. props是只读的，Vue底层会监测你对props的修改，如果进行了修改，就会发出警告，若业务需求确实需要修改，那么请复制props的内容到data中，然后去修改data中的数据

## 3.6 mixin 混入
1. 功能：可以把多个组件共用的配置提取成一个混入对象 
2. 使用方式
   1.  定义混入
   2.  使用混入
       1.  全局混入`Vue.mixin(xxx)`
       2.  局部混入`mixins:['xxx']`
```JavaScript
const mixin = {
    data() {....},
    methods: {....}
    ....
}
```
3. 组件和混入对象含有同名选项时，这些选项将以恰当的方式进行“合并”，在发生冲突时以组件优先，但生命周期全都执行

## 3.7 plugin 插件
1. 功能：用于增强Vue
2. 本质：包含install方法的一个对象，install的第一个参数是Vue，第二个以后的参数是插件使用者传递的数据
3. 定义插件（见下 src/plugin.js）
```JavaScript

```
4. 使用插件：`Vue.use()`

## 3.8 组件化编组流程
1. 拆分静态组件：组件要按照功能点拆分，命名不要与html元素冲突
2. 实现动态组件：考虑好数据的存放位置，数据是一个组件在用，还是一些组件在用
   1. 一个组件在用：放在组件自身即可
   2. 一些组件在用：放在他们共同的父组件上（状态提升）
3. 实现交互：从绑定事件开始

## 3.9 组件间通信
### 3.9.1 props父子组件间通信
1. 父组件向子组件通信
   1. 父组件`<Son :msg:"msg"/>`
   2. 子组件`props:[msg]`
2. 子组件向父组件通信
   1. 父组件`<Son :receive:"receive>`,给子组件传递函数
   2. 子组件`props:[receive]`,`this.receive(msg)`通过调用函数将数据传给父组件
### 3.9.2 组件自定义事件子父通信
1. 一种组件间通信的方式，适用于：子组件 ===> 父组件
2. 使用场景：子组件想给父组件传数据，那么就要在父组件中给子组件绑定自定义事件（事件的回调在父组件中）
3. 绑定自定义事件
   1. 第一种方式，在父组件中`<Demo @事件名="方法"/>`或`<Demo v-on:事件名="方法"/>`
   2. 第二种方式，在父组件中`this.$refs.demo.$on('事件名',方法)`
   3. 若想让自定义事件只能触发一次，可以使用once修饰符，或$once方法 
4. 触发自定义事件`this.$emit('事件名',数据)` 
5. 解绑自定义事件`this.$off('事件名') `
6. 组件上也可以绑定原生DOM事件，需要使用native修饰符`@click.native="show"`上面绑定自定义事件，即使绑定的是原生事件也会被认为是自定义的，需要加native，加了后就将此事件给组件的根元素
7. 注意：通过`this.$refs.xxx.$on('事件名',回调函数)`绑定自定义事件时，回调函数要么配置在methods中，要么用箭头函数，否则 this 指向会出问题
### 3.9.3 全局事件总线任意组件间通信
1. 一种可以在任意组件间通信的方式，本质上就是一个对象，它必须满足以下条件
   1. 所有的组件对象都必须能看见他 
   2. 这个对象必须能够使用`$on``$emit``$off`方法去绑定、触发和解绑事件
2. 使用步骤
   1. 定义全局事件总线
```JavaScript
new Vue({
   	beforeCreate() {
   		Vue.prototype.$bus = this // 安装全局事件总线，$bus 就是当前应用的 vm
   	},
})
```
   2. 使用事件总线 
      1. 接收数据：A组件想接收数据，则在A组件中给$bus绑定自定义事件，事件的回调留在A组件自身
      2. 提供数据：`this.$bus.$emit('xxx',data)`
```JavaScript
// 接收数据
export default {
    methods(){
        demo(data){...}
    }
    mounted() {
        this.$bus.$on('xxx',this.demo)
    }
} 
```  
   3. 最好在beforeDestroy钩子中，用`$off()`去解绑当前组件所用到的事件
### 3.9.4 消息的订阅与发布(基本不用)
1. 消息订阅与发布（pubsub）消息订阅与发布是一种组件间通信的方式，适用于任意组件间通信 
2. 使用步骤
   1. 安装pubsub：`npm i pubsub-js`
   2. 引入：`import pubsub from 'pubsub-js'`
   3. 接收数据：A组件想接收数据，则在A组件中订阅消息，订阅的回调留在A组件自身
   4. 提供数据：`pubsub.publish('xxx',data) `
   5. 最好在beforeDestroy钩子中，使用pubsub.unsubscribe(pid)取消订阅
```JavaScript
// 接收数据方
export default {
    methods: {
        demo(msgName, data) {...}
    },
    mounted() {
		this.pid = pubsub.subscribe('xxx',this.demo)
    },
    beforeDestroy() {
        pubsub.unsubscribe(this.pid) // 取消订阅
    }
}
```

## 3.10 slot 插槽
1. `<slot>`插槽：让父组件可以向子组件指定位置插入html结构，也是一种组件间通信的方式，适用于 父组件 ===> 子组件
2. 分类：默认插槽、具名插槽、作用域插槽
### 3.10.1 默认插槽
```VUE
// 父组件中：
<template>
    <Category>
        <div>html结构1</div>
    </Category>
</template>
// 子组件中：Category
<template>
    <div>
       <!-- 定义插槽 -->
       <slot>插槽默认内容...</slot>
    </div>
</template>
```
### 3.10.2 具名插槽
父组件指明放入子组件的哪个插槽`slot="footer"`，如果是template可以写成`v-slot:footer`
```VUE
// 父组件中：
<template>
    <Category>
        <template slot="center">
          <div>html结构1</div>
        </template> 
        <template v-slot:footer>
           <div>html结构2</div>
        </template>
    </Category>
</template>
// 子组件中：
<template>
    <div>
       <!-- 定义插槽 -->
       <slot name="center">插槽默认内容...</slot>
       <slot name="footer">插槽默认内容...</slot>
    </div>
</template>
```
### 3.10.3 作用域插槽
1. scope用于父组件往子组件插槽放的html结构接收子组件的数据
2. 理解：数据在组件的自身，但根据数据生成的结构需要组件的使用者来决定
3. （games数据在Category组件中，但使用数据所遍历出来的结构由App组件决定） 
```Vue
父组件中：
<template>
    <Category>
        <template scope="scopeData">
            <!-- 生成的是ul列表 -->
            <ul>
              <li v-for="g in scopeData.games" :key="g">{{g}}</li>
            </ul>
        </template>
    </Category>

    <Category>
        <template slot-scope="scopeData">
            <!-- 生成的是h4标题 -->
            <h4 v-for="g in scopeData.games" :key="g">{{g}}</h4>
        </template>
    </Category>
</template>
子组件中：
<template>
    <div>
        <slot :games="games"></slot>
    </div>
</template>

<script>
    export default {
        name:'Category',
        props:['title'],
        //数据在子组件自身
        data() {
            return {
                games:['红色警戒','穿越火线','劲舞团','超级玛丽']
            }
        },
    }
        </script>
```

---

# 4 Vue CLI
## 4.1 脚手架文件结构
.文件目录
├── node_modules 
├── public
│   ├── favicon.ico: 页签图标
│   └── index.html: 主页面
├── src
│   ├── assets: 存放静态资源
│   │   └── logo.png
│   │── component: 存放组件
│   │   └── HelloWorld.vue
│   │── App.vue: 汇总所有组件
│   └── main.js: 入口文件
├── .gitignore: git版本管制忽略的配置
├── babel.config.js: babel的配置文件
├── package.json: 应用包配置文件 
├── README.md: 应用描述文件
└── package-lock.json: 包版本控制文件

## 4.2 render函数
因为 vue.runtime.xxx.js 没有模板解析器，所以不能使用template配置项，需要使用render函数接收到的createElement函数去指定具体内容
```JavaScript
import Vue from 'vue'
import App from './App.vue'                 
Vue.config.productionTip = false
new Vue({
  el:'#app',
  // render函数功能：将App组件放入容器中
  // 简写形式
  render: h => h(App),
  // 完整形式
  render(createElement){
    return createElement(App)
  }
})
```

## 4.3 vue.config.js 配置文件
使用vue.config.js可以对脚手架进行个性化定制，和package.json同级目录

## 4.4 scoped样式
1. 作用：让样式在局部生效，防止冲突
2. 写法：`<style scoped>`

## 4.5 Vue脚手架配置代理
vue.config.js 是一个可选的配置文件，如果项目的 (和 package.json 同级的) 根目录中存在这个文件，那么它会被 @vue/cli-service 自动加载。你也可以使用 package.json 中的 vue 字段，但是注意这种写法需要你严格遵照 JSON 的格式来写
### 4.5.1 方法一
```JavaScript
module.exports = {
  devServer:{
    proxy:"http://localhost:5000"
  }
}
```
1. 优点：配置简单，请求资源时直接发给前端（8080）即可
2. 缺点：不能配置多个代理，不能灵活的控制请求是否走代理
3. 工作方式：若按照上述配置代理，当请求了前端不存在的资源时，才会将请求会转发给服务器 （优先匹配前端资源）
### 4.5.2 方法二
```JavaScript
module.exports = {
	devServer: {
      proxy: {
      '/api1': {							// 匹配所有以 '/api1'开头的请求路径
        target: 'http://localhost:5000',	// 代理目标的基础路径
        pathRewrite: {'^/api1':''},			// 代理往后端服务器的请求去掉 /api1 前缀
        ws: true,							// WebSocket
        changeOrigin: true,
      }
    }
  }
}
/*
   changeOrigin设置为true时，服务器收到的请求头中的host为：localhost:5000
   changeOrigin设置为false时，服务器收到的请求头中的host为：localhost:8080
   changeOrigin默认值为true
*/
```
1. 优点：可以配置多个代理，且可以灵活的控制请求是否走代理
2. 缺点：配置略微繁琐，请求资源时必须加前缀



# 5 Vuex

## 5.1 Vuex概述
### 5.1.1 Vuex概念
1. 概念：专门在Vue中实现*集中式***状态（数据）**管理的一个Vue*插件*，对Vue应用中多个组件的共享状态进行集中式的管理（读/写），也是一种组件间通信的方式，且适用于任意组件间通信
![Vuex共享数据数据流](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643034632949-1f50dc65-b44d-4b00-bed1-10222a2e87e5.png?x-oss-process=image%2Fresize%2Cw_750%2Climit_0)
### 5.1.2 Vuex使用场景
1. 多个组件依赖于同一状态
2. 来自不同组件的行为需要变更同一状态
### 5.1.3 Vuex工作原理
![Vuex工作原理](https://cdn.nlark.com/yuque/0/2022/png/1379492/1643034632508-417c8676-569a-41e1-b7db-223fafbedfd7.png)

## 5.2 搭建Vuex环境
1. 下载安装Vuex `npm i vuex`
2. 创建`src/store/index.js`该文件用于创建Vuex中最为核心的store
```javascript
import Vue from 'vue'
import Vuex from 'vuex'	// 引入Vuex

Vue.use(Vuex)	// 应用Vuex插件

const actions = {}		// 准备actions——用于响应组件中的动作
const mutations = {}	// 准备mutations——用于操作数据（state）
const state = {}			// 准备state——用于存储数据

// 创建并暴露store
export default new Vuex.Store({
	actions,
	mutations,
	state,
})
```
3. 在`src/main.js`中创建vm时传入store配置项
```javascript
import Vue from 'vue'
import App from './App.vue'
import store from './store'	// 引入store

Vue.config.productionTip = false

new Vue({
	el: '#app',
	render: h => h(App),
	store,										// 配置项添加store
	beforeCreate() {
		Vue.prototype.$bus = this
	}
})
```

## 5.3 Vuex基本使用
1. 初始化数据state，配置actions、mutations，操作文件store.js
2. 组件中读取vuex中的数据`$store.state.数据`
3. 组件中修改vuex中的数据`$store.dispatch('action中的方法名',数据)` 或`$store.commit('mutations中的方法名',数据)`
4. 若没有网络请求或其他业务逻辑，组件中也可越过actions，即不写dispatch，直接编写commit
5. actions一般写小写，mutations一般大写
```javascript
//src/components/Count.vue
// 数据使用
$store.state.sum
// 修改数据
methods: {
    increment(){
        this.$store.commit('JIA',this.n)
    },
    decrement(){
        this.$store.commit('JIAN',this.n)
    },
    incrementOdd(){
        this.$store.dispatch('jiaOdd',this.n)
    },
    incrementWait(){
        this.$store.dispatch('jiaWait',this.n)
    },
}
//`src/store/index.js`内容
const actions = {
	jiaOdd(context,value){	// context 相当于精简版的 $store，是一种上下文对象
		console.log('actions中的jiaOdd被调用了')
		if(context.state.sum % 2){
			context.commit('JIA',value)
		}
	},
	jiaWait(context,value){
		console.log('actions中的jiaWait被调用了')
		setTimeout(()=>{
			context.commit('JIA',value)
		},500)
	}
}
// 一般都大写
const mutations = {
	JIA(state,value){
		console.log('mutations中的JIA被调用了')
		state.sum += value
	},
	JIAN(state,value){
		console.log('mutations中的JIAN被调用了')
		state.sum -= value
	}
}
const state = {
	sum:0 //当前的和
}

// 创建并暴露store
export default new Vuex.Store({
	actions,
	mutations,
	state,
})
```

## 5.4 getters 配置项
1. 概念：当`state`中的数据需要经过加工后再使用时，可以使用`getters`加工，相当于*全局计算属性*
2. 在`store.js`中追加`getters`配置
3. 组件中读取数据`$store.getters.bigSum`
```javascript
......
const getters = {
	bigSum(state){
		return state.sum * 10
	}
}

// 创建并暴露store
export default new Vuex.Store({
	......
	getters
})
```

## 5.5 四个map方法
### 5.5.1 mapState
1. 用于帮助映射state中的数据为计算属性
```javascript
computed: {
  	// 借助mapState生成计算属性：sum、school、subject（对象写法一）
  	...mapState({sum:'sum',school:'school',subject:'subject'}),

  	// 借助mapState生成计算属性：sum、school、subject（数组写法二）
  	...mapState(['sum','school','subject']),
},
```
### 5.5.2 mapGetters
1. 用于帮助映射getters中的数据为计算属性
```javascript
computed: {
    //借助mapGetters生成计算属性：bigSum（对象写法一）
    ...mapGetters({bigSum:'bigSum'}),

    //借助mapGetters生成计算属性：bigSum（数组写法二）
    ...mapGetters(['bigSum'])
},
```
### 5.5.3 mapActions
1. 用于帮助生成与actions对话的方法，即包含`$store.dispatch(xxx)`的函数  
```javascript
methods:{
    //靠mapActions生成：incrementOdd、incrementWait（对象形式）
    ...mapActions({incrementOdd:'jiaOdd',incrementWait:'jiaWait'})

    //靠mapActions生成：incrementOdd、incrementWait（数组形式）
    ...mapActions(['jiaOdd','jiaWait'])
}
```
### 5.5.4 mapMutations
1. 用于帮助生成与mutations对话的方法，即包含`$store.commit(xxx)`的函数 
```javascript
methods:{
    //靠mapActions生成：increment、decrement（对象形式）
    ...mapMutations({increment:'JIA',decrement:'JIAN'}),
    
    //靠mapMutations生成：JIA、JIAN（对象形式）
    ...mapMutations(['JIA','JIAN']),
}
```
2. 注意：mapActions与mapMutations使用时，若需要传递参数需要：在模板中绑定事件时传递好参数，否则参数是事件对象

## 5.6 Vuex模块化
1. 目的：让代码更好维护，让多种数据分类更加明确
2. 修改`store.js`：为了解决不同模块命名冲突的问题，将不同模块的namespaced: true，之后在不同页面中引入`getter``actions``mutations`时，需要加上所属的模块名
```javascript
const countAbout = {
  namespaced: true,	// 开启命名空间
  state: {x:1},
  mutations: { ... },
  actions: { ... },
  getters: {
    bigSum(state){ return state.sum * 10 }
  }
}

const personAbout = {
  namespaced: true,	// 开启命名空间
  state: { ... },
  mutations: { ... },
  actions: { ... }
}

const store = new Vuex.Store({
  modules: {
    countAbout,
    personAbout
  }
})
```
3. 开启命名空间后，组件中读取state数据
```javascript
// 方式一：自己直接读取
this.$store.state.personAbout.list
// 方式二：借助mapState读取：
...mapState('countAbout',['sum','school','subject']),
```
4. 开启命名空间后，组件中读取getters数据
```javascript
//方式一：自己直接读取
this.$store.getters['personAbout/firstPersonName']
//方式二：借助mapGetters读取：
...mapGetters('countAbout',['bigSum'])
```
5. 开启命名空间后，组件中调用dispatch
```javascript
//方式一：自己直接dispatch
this.$store.dispatch('personAbout/addPersonWang',person)
//方式二：借助mapActions：
...mapActions('countAbout',{incrementOdd:'jiaOdd',incrementWait:'jiaWait'})
```
6. 开启命名空间后，组件中调用commit
```javascript
//方式一：自己直接commit
this.$store.commit('personAbout/ADD_PERSON',person)
//方式二：借助mapMutations：
...mapMutations('countAbout',{increment:'JIA',decrement:'JIAN'}),
```



# 6 Vue Router
## 6.1 相关概念
### 6.1.1 路由
1. 路由概念
   1. 一个路由就是一组映射关系（key - value）
   2. key为路径，value可能是function或componen
2. 路由分类
   1. 后端路由
      1. 理解：value是function，用于处理客户端提交的请求
      2. 工作过程：服务器接收到一个请求时，根据请求路径找到匹配的函数来处理请求，返回响应数据
   2. 前端路由
      1. 理解：value是component，用于展示页面内容
      2. 工作过程：当浏览器的路径改变时，对应的组件就会显示
### 6.1.2 SPA应用
1. 单页Web应用（single page web application，SPA）
2. 整个应用只有一个完整的页面
3. 点击页面中的导航链接不会刷新页面，只会做页面的局部更新
4. 数据需要通过ajax请求获取

## 6.2 基本路由
### 6.2.1 基本路由使用
1. 安装vue-router，命令`npm i vue-router`
2. 应用插件`Vue.use(VueRouter)`
3. 编写router配置项
```javascript
import VueRouter from 'vue-router'			// 引入VueRouter
import About from '../components/About'	// 路由组件
import Home from '../components/Home'		// 路由组件

// 创建router实例对象，去管理一组一组的路由规则
const router = new VueRouter({
	routes:[
		{
			path:'/about',
			component:About
		},
		{
			path:'/home',
			component:Home
		}
	]
})

//暴露router
export default router
```
4. 实现切换`<router-link></router-link>`浏览器会被替换为a标签,`active-class`可配置高亮样式
```html
<router-link active-class="active" to="/about">About</router-link>
```
5. 指定展示位`<router-view></router-view>`
### 6.2.2 注意事项
1. 路由组件通常存放在pages文件夹，一般组件通常存放在components文件夹
2. 通过切换，“隐藏”了的路由组件，默认是被销毁掉的，需要的时候再去挂载
3. 每个组件都有自己的`$route`属性，里面存储着自己的路由信息
4. 整个应用只有一个router，可以通过组件的`$router`属性获取到

## 6.3 多级路由
1. 配置路由规则，使用children配置项
```javascript
routes:[
	{
		path:'/about',
		component:About,
	},
	{
		path:'/home',
		component:Home,
		children:[ 					// 通过children配置子级路由
			{
				path:'news', 		// 此处一定不要带斜杠，写成 /news
				component:News
			},
			{
				path:'message',	// 此处一定不要写成 /message
				component:Message
			}
		]
	}
]
```
2. 跳转（要写完整路径）`<router-link to="/home/news">News</router-link>`

## 6.4 路由传参
### 6.4.1 query参数
1. 传递query参数
```html
<!-- 跳转并携带query参数，to的字符串写法 -->
<router-link :to="`/home/message/detail?id=${m.id}&title=${m.title}`">跳转</router-link>
				
<!-- 跳转并携带query参数，to的对象写法（推荐） -->
<router-link 
	:to="{
		path:'/home/message/detail',
		query:{
		    id: m.id,
            title: m.title
		}
	}"
>跳转</router-link>
```
2. 接收query参数`$route.query.id`,`$route.query.title`
### 6.4.2 params参数
1. 配置路由，声明接收params参数
```javascript
{
	path:'/home',
	component:Home,
	children:[
		{
			path:'news',
			component:News
		},
		{
			component:Message,
			children:[
				{
					name:'xiangqing',
					path:'detail/:id/:title', // 🔴使用占位符声明接收params参数
					component:Detail
				}
			]
		}
	]
}
```
2. 传递参数：**特别注意**：路由携带params参数时，若使用to的对象写法，则不能使用path配置项，必须使用name配置！
```html
<!-- 跳转并携带params参数，to的字符串写法 -->
<router-link :to="/home/message/detail/666/你好">跳转</router-link>
				
<!-- 跳转并携带params参数，to的对象写法 -->
<router-link 
	:to="{
		name:'xiangqing',
		params:{
		    id:666,
            title:'你好'
		}
	}"
>跳转</router-link>
```
3. 接收参数`$route.params.id``$route.params.title`
### 6.4.3 路由props配置
1. props作用：让路由组件更方便的收到参数
2. 在`router/index.js`里增加props配置
```javascript
{
	name:'xiangqing',
	path:'detail/:id',
	component:Detail,

	//第一种写法：props值为对象，该对象中所有的key-value的组合最终都会通过props传给Detail组件
	props:{a:900},

	//第二种写法：props值为布尔值，为true时，则把路由收到的所有params参数通过props传给Detail组件
	props:true,
	
	//第三种写法：props值为函数，该函数返回的对象中每一组key-value都会通过props传给Detail组件
	props($route){
		return {
			id: $route.query.id,
			title: $route.query.title
		}
	}
}
```

## 6.5 命名路由
1. 作用：可以简化路由的跳转
### 6.5.1 命名路由使用
1. 给路由命名 
```javascript
{
	path:'/demo',
	component:Demo,
	children:[
		{
			path:'test',
			component:Test,
			children:[
				{
          name:'hello' // 给路由命名
					path:'welcome',
					component:Hello,
				}
			]
		}
	]
}
```
2. 简化跳转
```html
<!--简化前，需要写完整的路径 -->
<router-link to="/demo/test/welcome">跳转</router-link>

<!--简化后，直接通过名字跳转 -->
<router-link :to="{name:'hello'}">跳转</router-link>

<!--简化写法配合传递参数 -->
<router-link 
	:to="{
		name:'hello',
		query:{
		    id:666,
            title:'你好'
		}
	}"
>跳转</router-link>
```

## 6.6 路由跳转replace模式
1. 作用：控制路由跳转时操作浏览器历史记录的模式
2. 浏览器的历史记录有两种写入方式：push和replace
   1. push是追加历史记录
   2. replace是替换当前记录，路由跳转时候默认为push方式
3. 开启replace模式`<router-link :replace="true" ...>News</router-link>`
4. 简写`<router-link replace ...>News</router-link>`
5. 总结：浏览记录本质是一个栈，默认push，点开新页面就会在栈顶追加一个地址，后退，栈顶指针向下移动，改为replace就是不追加，而将栈顶地址替换

## 6.7 编程式路由导航
1. 作用：不借助<router-link>实现路由跳转，让路由跳转更加灵活
2. `this.$router.push({})`内传的对象与`<router-link>`中的to相同
3. `this.$router.replace({})`	
4. `this.$router.forward()`前进
5. `this.$router.back()`后退
6. `this.$router.go(n)`可前进也可后退，n为正数前进n，为负数后退

## 6.8 缓存路由组件
1. 作用：让不展示的路由组件保持挂载，不被销毁
2. `<keep-alive include="News"><router-view></router-view></keep-alive>`
3. `<keep-alive :include="['News', 'Message']"><router-view></router-view></keep-alive>`

## 6.9 路由相关生命钩子
1. activated和deactivated是路由组件所独有的两个钩子，用于捕获路由组件的激活状态
2. activated路由组件被激活时触发
3. deactivated路由组件失活时触发

## 6.10 路由守卫
1. 作用：对路由进行权限控制 
2. 分类：全局守卫、独享守卫、组件内守卫 
### 6.10.1 全局前置守卫
1. 每次路由切换之前和初始化时被调用
2. `router.beforeEach((to,from,next) => {})`
3. `to`是路由去往的信息，`from`是跳转路由前的信息，`next()`放行
4. `meta`路由元信息，是可以自定义的信息
```javascript
router.beforeEach((to,from,next) => {
	console.log('beforeEach',to,from)
	if(to.meta.isAuth){ // 判断当前路由是否需要进行权限控制
		if(localStorage.getItem('school') === 'atguigu'){ // 权限控制的具体规则
			next()	// 放行
		}else{
			alert('暂无权限查看')
		}
	}else{
		next()	// 放行
	}
})
```
### 6.10.2 全局后置守卫
1. 每次路由切换后和初始化时被调用，没有`next()`方法
2. 用来切换标签页名字
```javascript
router.afterEach((to,from) => {
	console.log('afterEach',to,from)
	if(to.meta.title){ 
		document.title = to.meta.title //修改网页的title
	}else{
		document.title = 'vue_test'
	}
})
```
### 6.10.3 独享守卫
1. 是routes的一个配置项
2. 没有独享后置路由守卫
```javascript
beforeEnter(to,from,next){
	console.log('beforeEnter',to,from)
    if(localStorage.getItem('school') === 'atguigu'){
        next()
    }else{
        alert('暂无权限查看')
    }
}
```
### 6.10.4 组件内守卫
1. 类似于生命周期
2. 是通过路由进入离开组件才会触发，直接放在页面上的是不触发的
```javascript
//进入守卫：通过路由规则，进入该组件时被调用
beforeRouteEnter (to, from, next) {... next()},

//离开守卫：通过路由规则，离开该组件时被调用
beforeRouteLeave (to, from, next) {... next()},
```

## 6.11 路由器的工作模式
1. 对于一个url来说，#及其后面的内容就是hash值
2. hash值不会包含在HTTP请求中，即：hash值不会带给服务器 
### 6.11.1 hash模式 
1. 地址中永远带着#号，不美观
2. 若以后将地址通过第三方手机app分享，若app校验严格，则地址会被标记为不合法
3. 兼容性较好
### 6.11.2 history模式
1. 地址干净，美观
2. 兼容性和hash模式相比略差
3. 应用部署上线时需要后端人员支持，解决刷新页面服务端404的问题
```javascript
const router =  new VueRouter({
	mode:'history',
	routes:[...]
})

export default router
```



# 7 VUE3
## 7.1 创建VUE3工程
### 7.1.1 vue-cli创建
```bash
## 查看@vue/cli版本，确保@vue/cli版本在4.5.0以上
vue --version
## 安装或者升级你的@vue/cli
npm install -g @vue/cli
## 创建
vue create vue_test
## 启动
cd vue_test
npm run serve
```
### 7.1.2 vite创建
1. 优势
   1. 开发环境中，无需打包操作，可快速的冷启动。
   2. 轻量快速的热重载（HMR）。
   3. 真正的按需编译，不再等待整个应用编译完成。
2. 传统构建与vite构建对比图
![传统工具构建原理](https://cn.vitejs.dev/assets/bundler.37740380.png)
![vite构建原理](https://cn.vitejs.dev/assets/esm.3070012d.png)
```bash
## 创建工程
npm init vite-app <project-name>
## 进入工程目录
cd <project-name>
## 安装依赖
npm install
## 运行
npm run dev
```

## 7.2 响应式原理
### 7.2.1 VUE2响应式
1. 实现原理：
   1. 对象类型：通过```Object.defineProperty()```对属性的读取、修改进行拦截（数据劫持）。
   2. 数组类型：通过重写更新数组的一系列方法来实现拦截。（对数组的变更方法进行了包裹）。
    ```js
    Object.defineProperty(data, 'count', {
        get () {}, 
        set () {}
    })
    ```
2. 存在问题：
   1. 新增属性、删除属性, 界面不会更新。
   2. 直接通过下标修改数组, 界面不会自动更新。
### 7.2.2 VUE3响应式
1. 实现原理: 
   1. 通过Proxy（代理）:  拦截对象中任意属性的变化, 包括：属性值的读写、属性的添加、属性的删除等。
   2. 通过Reflect（反射）:  对源对象的属性进行操作。
   3. MDN文档中描述的Proxy与Reflect：
      1. [Proxy](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
      2. [Reflect](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Reflect)
      ```js
      new Proxy(data, {
      	// 拦截读取属性值
          get (target, prop) {
          	return Reflect.get(target, prop)
          },
          // 拦截设置属性值或添加新属性
          set (target, prop, value) {
          	return Reflect.set(target, prop, value)
          },
          // 拦截删除属性
          deleteProperty (target, prop) {
          	return Reflect.deleteProperty(target, prop)
          }
      })
      
      proxy.name = 'tom'   
      ```

## 7.3 常见Composition API
### 7.3.1 setup
1. 理解：Vue3.0中一个新的配置项，值为一个函数。
2. setup是所有**Composition API（组合API）**“ 表演的舞台 ”。
3. 组件中所用到的：数据、方法等等，均要配置在setup中。
4. setup函数的两种返回值：
   1. 若返回一个对象，则对象中的属性、方法, 在模板中均可以直接使用。（重点关注！）
   2. 若返回一个渲染函数：则可以自定义渲染内容。（了解）
5. setup执行的时机：在beforeCreate之前执行一次，this是undefined。
6. setup的参数
  - props：值为对象，包含：组件外部传递过来，且组件内部声明接收了的属性。
  - context：上下文对象
    - attrs: 值为对象，包含：组件外部传递过来，但没有在props配置中声明的属性, 相当于 ```this.$attrs```。
    - slots: 收到的插槽内容, 相当于 ```this.$slots```。
    - emit: 分发自定义事件的函数, 相当于 ```this.$emit```。
7. 注意点：
   1. 尽量不要与Vue2.x配置混用
      - Vue2.x配置（data、methos、computed...）中*可以访问*到setup中的属性、方法。
      - 但在setup中*不能访问*到Vue2.x配置（data、methos、computed...）。
      - 如果有重名, setup优先。
   2. setup不能是一个async函数，因为返回值不再是return的对象, 而是promise, 模板看不到return对象中的属性。（后期也可以返回一个Promise实例，但需要Suspense和异步组件的配合）
### 7.3.2 ref函数
1. 作用: 定义一个响应式的数据
2. 语法: ```const xxx = ref(initValue)``` 
   1. 创建一个包含响应式数据的引用对象（reference对象，简称ref对象）
   2. JS中操作数据： ```xxx.value```
   3. 模板中读取数据: 不需要.value，直接：```<div>{{xxx}}</div>```
3. 备注：
   1. 接收的数据可以是：基本类型、也可以是对象类型。
   2. 基本类型的数据：响应式依然是靠``Object.defineProperty()``的```get```与```set```完成的。
   3. 对象类型的数据：内部“ 求助 ”了Vue3.0中的一个新函数—— ```reactive```函数。
### 7.3.3 reactive函数
1. 作用: 定义一个对象类型的响应式数据（基本类型不要用它，要用```ref```函数）
2. 语法：```const 代理对象= reactive(源对象)```接收一个对象（或数组），返回一个代理对象（Proxy的实例对象，简称proxy对象）
3. reactive定义的响应式数据是“深层次的”。
4. 内部基于 ES6 的 Proxy 实现，通过代理对象操作源对象内部数据进行操作。
5. 与ref的对比
   1. 从定义数据角度对比：
      1. ref用来定义：基本类型数据。
      2. reactive用来定义：对象（或数组）类型数据。
      3. 备注：ref也可以用来定义对象（或数组）类型数据, 它内部会自动通过```reactive```转为代理对象。
   2. 从原理角度对比：
      1. ref通过``Object.defineProperty()``的```get```与```set```来实现响应式（数据劫持）。
      2. reactive通过使用Proxy来实现响应式（数据劫持）, 并通过Reflect操作对象内部的数据。
   3. 从使用角度对比：
      1. ref定义的数据：操作数据需要```.value```，读取数据时模板中直接读取不需要```.value```。
      2. reactive定义的数据：操作数据与读取数据：均不需要```.value```。
### 7.3.4 computed函数
1. 与Vue2.x中computed配置功能一致
```javascript
import {computed} from 'vue'

setup(){
    ...
	//计算属性——简写
    let fullName = computed(()=>{
        return person.firstName + '-' + person.lastName
    })
    //计算属性——完整
    let fullName = computed({
        get(){
            return person.firstName + '-' + person.lastName
        },
        set(value){
            const nameArr = value.split('-')
            person.firstName = nameArr[0]
            person.lastName = nameArr[1]
        }
    })
}
```
### 7.3.5 watch函数
1. 与Vue2.x中watch配置功能一致
2. 监视reactive定义的响应式数据时：oldValue无法正确获取、强制开启了深度监视（deep配置失效）。
3. 监视reactive定义的响应式数据中某个属性时：deep配置有效。
```javascript
//情况一：监视ref定义的响应式数据
watch(sum,(newValue,oldValue)=>{
	console.log('sum变化了',newValue,oldValue)
},{immediate:true})

//情况二：监视多个ref定义的响应式数据
watch([sum,msg],(newValue,oldValue)=>{
	console.log('sum或msg变化了',newValue,oldValue)
}) 

/* 情况三：监视reactive定义的响应式数据
	若watch监视的是reactive定义的响应式数据，则无法正确获得oldValue！！
	若watch监视的是reactive定义的响应式数据，则强制开启了深度监视 
*/
watch(person,(newValue,oldValue)=>{
	console.log('person变化了',newValue,oldValue)
},{immediate:true,deep:false}) //此处的deep配置不再奏效

//情况四：监视reactive定义的响应式数据中的某个属性
watch(()=>person.job,(newValue,oldValue)=>{
	console.log('person的job变化了',newValue,oldValue)
},{immediate:true,deep:true}) 

//情况五：监视reactive定义的响应式数据中的某些属性
watch([()=>person.job,()=>person.name],(newValue,oldValue)=>{
	console.log('person的job变化了',newValue,oldValue)
},{immediate:true,deep:true})

//特殊情况
watch(()=>person.job,(newValue,oldValue)=>{
    console.log('person的job变化了',newValue,oldValue)
},{deep:true}) //此处由于监视的是reactive素定义的对象中的某个属性，所以deep配置有效
```
### 7.3.6 watchEffect函数
1. watch的套路是：既要指明监视的属性，也要指明监视的回调。
2. watchEffect的套路是：不用指明监视哪个属性，监视的回调中用到哪个属性，那就监视哪个属性。
3. watchEffect有点像computed：
   1. 但computed注重的计算出来的值（回调函数的返回值），所以必须要写返回值。
   2. 而watchEffect更注重的是过程（回调函数的函数体），所以不用写返回值。
```javascript
//watchEffect所指定的回调中用到的数据只要发生变化，则直接重新执行回调。
watchEffect(()=>{
    const x1 = sum.value
    const x2 = person.age
    console.log('watchEffect配置的回调执行了')
})
```
### 7.3.7 自定义hook函数
1. hook本质是一个函数，把setup函数中使用的Composition API进行了封装。
2. 类似于vue2.x中的mixin。
3. 自定义hook的优势: 复用代码, 让setup中的逻辑更清楚易懂。
### 7.3.8 toRef
1. 作用：创建一个 ref 对象，其value值指向另一个对象中的某个属性。
2. 语法：```const name = toRef(person,'name')```
3. 应用:   要将响应式对象中的某个属性单独提供给外部使用时。
4. 扩展：```toRefs``` 与```toRef```功能一致，但可以批量创建多个 ref 对象，语法：```toRefs(person)```

## 7.4 其它 Composition API
### 7.4.1 shallowReactive 与 shallowRef
1. shallowReactive：只处理对象最外层属性的响应式（浅响应式）。
2. shallowRef：只处理基本数据类型的响应式, 不进行对象的响应式处理。
3. 什么时候使用?
   1. 如果有一个对象数据，结构比较深, 但变化时只是外层属性变化 ===> shallowReactive。
   2. 如果有一个对象数据，后续功能不会修改该对象中的属性，而是生新的对象来替换 ===> shallowRef。
### 7.4.2 readonly 与 shallowReadonly
1. readonly: 让一个响应式数据变为只读的（深只读）。
2. shallowReadonly：让一个响应式数据变为只读的（浅只读）。
3. 应用场景: 不希望数据被修改时。
### 7.4.3 toRaw 与 markRaw
1. toRaw：
   1. 作用：将一个由```reactive```生成的响应式对象转为普通对象
   2. 使用场景：用于读取响应式对象对应的普通对象，对这个普通对象的所有操作，不会引起页面更新。
2. markRaw：
   1. 作用：标记一个对象，使其永远不会再成为响应式对象。
   2. 应用场景:
      1. 有些值不应被设置为响应式的，例如复杂的第三方类库等。
      2. 当渲染具有不可变数据源的大列表时，跳过响应式转换可以提高性能。
### 7.4.4 customRef
1. 作用：创建一个自定义的 ref，并对其依赖项跟踪和更新触发进行显式控制。
2. 实现防抖效果：
```vue
<template>
	<input type="text" v-model="keyword">
	<h3>{{keyword}}</h3>
</template>

<script>
	import {ref,customRef} from 'vue'
	export default {
		name:'Demo',
		setup(){
			// let keyword = ref('hello') //使用Vue准备好的内置ref
			//自定义一个myRef
			function myRef(value,delay){
				let timer
				//通过customRef去实现自定义
				return customRef((track,trigger)=>{
					return{
						get(){
							track() //告诉Vue这个value值是需要被“追踪”的
							return value
						},
						set(newValue){
							clearTimeout(timer)
							timer = setTimeout(()=>{
								value = newValue
								trigger() //告诉Vue去更新界面
							},delay)
						}
					}
				})
			}
			let keyword = myRef('hello',500) //使用程序员自定义的ref
			return {
				keyword
			}
		}
	}
</script>
```
### 7.4.5 provide 与 inject
![原理图](https://v3.cn.vuejs.org/images/components_provide.png)
1. 作用：实现祖与后代组件间通信
2. 套路：父组件有一个 `provide` 选项来提供数据，后代组件有一个 `inject` 选项来开始使用这些数据
3. 具体写法：
   1. 祖组件中：

     ```js
     setup(){
     	......
         let car = reactive({name:'奔驰',price:'40万'})
         provide('car',car)
         ......
     }
     ```
   2. 后代组件中：

     ```js
     setup(props,context){
     	......
         const car = inject('car')
         return {car}
     	......
     }
     ```

### 7.4.6.响应式数据的判断
1. isRef: 检查一个值是否为一个 ref 对象
2. isReactive: 检查一个对象是否是由 `reactive` 创建的响应式代理
3. isReadonly: 检查一个对象是否是由 `readonly` 创建的只读代理
4. isProxy: 检查一个对象是否是由 `reactive` 或者 `readonly` 方法创建的代理

## 7.5 Composition API 的优势
### 7.5.1 Options API 存在的问题
使用传统OptionsAPI中，新增或者修改一个需求，就需要分别在data，methods，computed里修改 。
![Options API](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f84e4e2c02424d9a99862ade0a2e4114~tplv-k3u1fbpfcp-watermark.image)
![Composition API](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5ac7e20d1784887a826f6360768a368~tplv-k3u1fbpfcp-watermark.image)
### 7.5.2 Composition API 的优势
我们可以更加优雅的组织我们的代码，函数。让相关功能的代码更加有序的组织在一起。
![Options API](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc0be8211fc54b6c941c036791ba4efe~tplv-k3u1fbpfcp-watermark.image)
![Composition API](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cc55165c0e34069a75fe36f8712eb80~tplv-k3u1fbpfcp-watermark.image)

## 7.6 Vue3新组件
### 7.6.1 Fragment
1. 在Vue2中: 组件必须有一个根标签
2. 在Vue3中: 组件可以没有根标签, 内部会将多个标签包含在一个Fragment虚拟元素中
3. 好处: 减少标签层级, 减小内存占用
### 7.6.2 Teleport
什么是Teleport？—— `Teleport` 是一种能够将我们的组件html结构移动到指定位置的技术
```html
<teleport to="移动位置">
	<div v-if="isShow" class="mask">
		<div class="dialog">
			<h3>我是一个弹窗</h3>
			<button @click="isShow = false">关闭弹窗</button>
		</div>
	</div>
</teleport>
```
### 7.6.3 Suspense
1. 等待异步组件时渲染一些额外内容，让应用有更好的用户体验
2. 使用步骤：
   1. 异步引入组件

    ```js
    import {defineAsyncComponent} from 'vue'
    const Child = defineAsyncComponent(()=>import('./components/Child.vue'))
    ```

   2. 使用```Suspense```包裹组件，并配置好```default``` 与 ```fallback```

    ```vue
    <template>
    	<div class="app">
    		<h3>我是App组件</h3>
    		<Suspense>
    			<template v-slot:default>
    				<Child/>
    			</template>
    			<template v-slot:fallback>
    				<h3>加载中.....</h3>
    			</template>
    		</Suspense>
    	</div>
    </template>
    ```

## 7.7 Vue3其他
### 7.7.1 全局API的转移
1. Vue 2.x 有许多全局 API 和配置。
2. 例如：注册全局组件、注册全局指令等。

    ```js
    //注册全局组件
    Vue.component('MyButton', {
      data: () => ({
        count: 0
      }),
      template: '<button @click="count++">Clicked {{ count }} times.</button>'
    })
    
    //注册全局指令
    Vue.directive('focus', {
      inserted: el => el.focus()
    })
    ```
3. Vue3.0中对这些API做出了调整：

  - 将全局的API，即：```Vue.xxx```调整到应用实例（```app```）上

    | 2.x 全局 API（```Vue```） | 3.x 实例 API (`app`)                        |
    | ------------------------- | ------------------------------------------- |
    | Vue.config.xxxx           | app.config.xxxx                             |
    | Vue.config.productionTip  | <strong style="color:#DD5145">移除</strong> |
    | Vue.component             | app.component                               |
    | Vue.directive             | app.directive                               |
    | Vue.mixin                 | app.mixin                                   |
    | Vue.use                   | app.use                                     |
    | Vue.prototype             | app.config.globalProperties                 |

### 7.7.2 data选项
data选项应始终被声明为一个函数。

### 7.7.3 过度类名的更改：

  - Vue2.x写法

    ```css
    .v-enter,
    .v-leave-to {
      opacity: 0;
    }
    .v-leave,
    .v-enter-to {
      opacity: 1;
    }
    ```

  - Vue3.x写法

    ```css
    .v-enter-from,
    .v-leave-to {
      opacity: 0;
    }
    
    .v-leave-from,
    .v-enter-to {
      opacity: 1;
    }
    ```

### 7.7.4 v-on 的修饰符
1. 移除keyCode作为 v-on 的修饰符，同时也不再支持```config.keyCodes```
2. 移除``v-on.native```修饰符

### 7.7.5 父组件中绑定事件

    ```html
    <my-component
      v-on:close="handleComponentEvent"
      v-on:click="handleNativeClickEvent"
    />
    ```

  - 子组件中声明自定义事件

    ```vue
    <script>
      export default {
        emits: ['close']
      }
    </script>
    ```
### 7.7.5 移除过滤器
过滤器虽然这看起来很方便，但它需要一个自定义语法，打破大括号内表达式是 “只是 JavaScript” 的假设，这不仅有学习成本，而且有实现成本！建议用方法调用或计算属性去替换过滤器。