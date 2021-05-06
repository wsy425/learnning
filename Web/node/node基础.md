# 概述
## node.js组成
1. ECMAScript
2. node环境提供的一些附加API
## node.js基础语法
1. 所有ECMAScript语法在node环境中都可以使用

# 模块化开发
1. JavaScript在使用时存在文件依赖和命名冲突两大问题
2. 一个功能就是一个模块，多个模块可以组成完整应用，抽离一个模块不会影响其他功能的运行

## 模块化开发规范
1. node.js规定一个JavaScript文件就是一个模块。模块内部定义的变量和函数默认情况下在外部无法得到
2. 模块内部可以使用exports对象进行成员导出，使用require方法导入其他模块