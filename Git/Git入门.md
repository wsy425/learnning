# Git原理

## snapshot

直接将发生变更的文件记录一个快照

## 可撤销

几乎所有提交快照的操作都是可撤销的

## 本地操作

大多数的操作可以本地进行

# git clone和git push

## git clone

git clone + SSH协议（+你想定义的下载文件夹名字）

# git push

在push之前一定要先git pull使本地文件夹与远程仓库同步

# Git文件四大状态

## untrack 未记录

1. 新创建的没有记录名称的文件
2. 用 `git add`来记录，使文件变为staged状态

## modified 修改过

1. 已经记录单最近发生了修改的文件
2. 用`git add`来记录，使文件变为staged状态
3. 用`git restore`来取消文件登记信息，使文件变为untrack状态

## staged 暂存

1. 文件在git系统中记录的是最新状态
2. 用`git commit`来提交，是文件变为committed状态

## committed 已提交

1. 文件提交到本地git仓库中
2. 用`git push`将文件推送至远程仓库中

## 总结

1. `git status`查看文件状态
2. ![状态关系图](https://images2017.cnblogs.com/blog/63651/201709/63651-20170909091456335-1787774607.jpg)

# gitignore

## 作用

使用`git add .`的时候避开一些不上传的文件

## 使用方法

1. 在git目录下创建一个.gitignore文件
2. 参考gitignore[文件模板](https://github.com/github/gitignore)，修改成为自己的文件

## gitignore文件语法

### #表示注释

### /忽略整个文件夹

`scr/build/`忽略了整个scr/build的内容

### ！表示取反

`！main.go`保留main.go文件，与上一条搭配使用

### glob模式匹配

1. *表示一切字符串，` *.txt`表示过滤一切txt文件
2. []表示方括号中任何一个字符，`[0-9]`表示匹配0-9中任意一个数字
3. ？表示匹配任何一个字符



