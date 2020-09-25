# Git原理
## snapshot
直接将发生变更的文件记录一个快照
## 可撤销s
几乎所有提交快照的操作都是可撤销的
## 本地操作
大多数的操作可以本地进行

# git clone和git push
## git clone
git clone + SSH协议（+你想定义的下载文件夹名字）
## git push
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
2. [] 表示方括号中任何一个字符，`[0-9]`表示匹配0-9中任意一个数字
3. ？表示匹配任何一个字符

# git diff
查看当前工作区与暂存区的差别
## git diff +文件路径
加上文件名，查看一下某一个文件具体的改动
## git diff --cached
查看暂存区和本地git仓库的差别
## 其他不常用用法
1. git diff <commitid>
比较工作区和某一个提交的差别
2. git diff <commitid> <filepath>
比较工作区和某一个提交某一个文件的差别
3. git diff --cached <commitid>
比较暂存区和某一个提交的差别
4. git diff --cached <commitid> <filepath>
比较暂存区和某一个提交某一个文件的差别

# git log
查看之前的提交记录
1. commit id
git log后commit后面跟着的一长串
git对commit id有自动补全功能，赋值前几位就可以了
2. 提交信息
每次commit -m之后后面输入的字符串，是比较关键的提示信息
## git log -p
展示出每一个commit中的改动，相当于同时做git diff
git log -p -n：查最近几条的提交记录及commit改动
## git log --start
在查看提交记录的基础上查看每次commit有多少改动量
## git log --pretty
pretty支持让我们自己DIY想看到的log展示
官方提供了oneline、short、full、fuller几种模板
可以自己定义，例如定义log日志当中应该包含commitid，提交时间，作者以及comment。那么定义出一种格式：%h - %ad - %an - %s命令行则为
`git log --pretty=format:"%h - %ad - %an - %s"`
官方提供了pretty参数表格
![微信图片_20200921094811.jpg](https://i.loli.net/2020/09/21/vfGtcBTqO7rmVnQ.jpg)

# git恢复相关
## git中删除文件
`git rm`
将文件从git以及文件系统当中一起移除（本地仓库、暂存、本地都删）
提交后从下一个提交开始这个文件就不会被存储一份了
留下添加文件和删除文件两条记录
## git中删除记录
`git commit --amend`
在删除文件后使用该指令在当前commit上修补而不是提交新的commit，这样就不会留下记录了
* 如果记录已经push到远程，使用该指令会导致和远程记录不吻合，需要使用`git push -f`强行push，但这会覆盖远程commit，可能会导致其他人代码紊乱
## 删除暂存区文件
`git rm --cached`
尚未commit的文件仅删除暂存区，保留本地文件
## 回滚commit版本
`git reset --soft HEAD^`
所有文件状态返回某一个commit的版本
## 回滚文件版本
`git checkout -- filename`
将文件恢复到之前提交的状态（本地和暂存都是）

# git分支(branch)
## git结构
在git当中我们使用的分支其实是一个一个在commit当中切换的指针
例子：
![QQ图片20200924103419.png](https://i.loli.net/2020/09/24/djGq2kYrOavHoCm.png)
## 创建分支
`git branch XXX`
`git checkout -b XXX`
## HEAD指针
指向当前代码仓库的位置
可以移动到任意结点上
移动HEAD指针
`git checkout (commit id/分支名)`
## 分支合并
`git checkout master`
`git merge test`
将test合并到master上
### 快速合并(fast-forward)
test分支是从master分支当中切出去的，后来master分支就再也没有进行过改动
合并的时候，其实只需要移动master指针到test分支上即可
### 创建新commit
test分支是从master分支当中切出去后来master分支有改动
由于不是直接上下游关系了，所以git创建了一个新的commit用来合并两个分支的代码
合并之后应该删除没用的分支
`git branch -d test`
## 合并分支冲突
### 查看冲突
`git diff`
### 手动解决
把提示行去掉
留下想要的代码，重新add、commit
### 放弃合并
`git merge --abort`
### git合并工具
git merge tool
不好用，一般不用
### IDE工具