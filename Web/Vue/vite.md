和我们以前使用Vue-cli的作用基本相同，都是项目初始化构建工具

# 特性
## 冷服务启动
冷服务的意思是，在开发预览中，它是不进行打包的
## 开发中热更新
也就是说在你开发的时候，只要一保存，结果就会更新
## 按需进行编译
不会刷新全部DOM节点

# 初始化项目
## npm
`
npm init vite-app <project-name>
cd <project-name>
npm install
npm run dev
`
## yarn
`
yarn create vite-app <project-name>
cd <project-name>
yarn
yarn dev
`

# 项目结构
## node_modules
项目依赖包目录
## public
项目共用文件
## src
原文件目录
### assets
静态文件目录，存放图片
### component
自动以组件目录
### App.vue
项目根组件，单页应用都需要
### index.css
项目通用css样式，main.js引入
### main.js
项目入口文件
## .gitignore
git的管理配置文件，设置那些目录或文件不管理
## index.htm
项目的默认首页，Vue的组件需要挂载到这个文件上
## package.json
项目配置文件，包管理、项目名称、版本和命令
