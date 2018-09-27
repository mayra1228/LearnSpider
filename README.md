### GitLab的安装及使用教程

------

>  **参考文档**
>
> * http://www.hjqjk.com/2017/GitLab-install-config.html
>
> * https://yq.aliyun.com/articles/74395
>
> * https://www.gitlab.com.cn/installation/#centos-6
>
> * https://github.com/xirong/my-git/blob/master/git-workflow-tutorial.md
> * http://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html  (命令集)
> * http://www.ruanyifeng.com/blog/2014/06/git_remote.html (远程命令)
> * http://www.ruanyifeng.com/blog/2015/08/git-use-process.html (使用规范)

#### <u>Git的家族成员</u>

* **Git** : 是一种版本控制系统,是一个命令,是一种工具
* **Gitlib** :是用于实现Git功能的开发库 
* **Github**: 是一个基于Git实现的在线代码管理仓库,包含一个网站界面,向互联网开放
* **GitLab**: 是一个基于Git实现的在线代码仓库托管软件, 你可以用gitlab自己搭建一个类似于Github一样的系统, 一般用于在企业、学校等内部网络搭建git私服.

#### <u>Gitlab的服务构成</u>

* Nginx : 静态web服务器
* gitlab-shell : 用于处理git命令和修改authorized keys列表
* gitlab-workhorse : 轻量级的反向代理服务器
* logrotate : 日志文件管理工具
* postgresql : 数据库
* redis : 缓存数据库
* sidekiq :用于在后台执行队列任务
* unicorn : An HTTP Server for Rack applications, GitLab Rails 应用是托管在这个服务器上面的.

#### <u>GitLab的工作流程</u>

![GitLabçå®è£åä½¿ç¨æç¨](http://docs-aliyun.cn-hangzhou.oss.aliyun-inc.com/assets/pic/52857/cn_zh/1492756915645/%E5%9B%BE%E7%89%878.png)

- Gitflow工作流是经典模型,处于核心位置
- Forking工作流是分布式协作

#### <u>Gitlab的安装</u>

##### 1. 配置yum源

```shell
# vim /etc/yum.repos.d/gitlab-ce.repo
[gitlab-ce]
name=gitlab-ce
baseurl=http://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el6
gpgcheck=0
Enabled=1
```

##### 2.更新本地yum缓存

```shell
# yum makechache
```

##### **3.安装gitlab社区版**

```shell
# yum intall gitlab-ce        #自动安装最新版
# yum install gitlab-ce-x.x.x    #安装指定版本
```

##### 4.Gitlab安装细节

```
主配置文件: /etc/gitlab/gitlab.rb
GitLab 文档根目录: /opt/gitlab
默认存储库位置: /var/opt/gitlab/git-data/repositories
GitLab Nginx 配置文件路径:  /var/opt/gitlab/nginx/conf/gitlab-http.conf
Postgresql 数据目录: /var/opt/gitlab/postgresql/data
```

##### **5.GitLab常用命令**

```shell
sudo gitlab-ctl start    	# 启动所有 gitlab 组件；
sudo gitlab-ctl stop        # 停止所有 gitlab 组件；
sudo gitlab-ctl restart     # 重启所有 gitlab 组件；
sudo gitlab-ctl status      # 查看服务状态；
sudo gitlab-ctl reconfigure # 启动服务；
sudo vim /etc/gitlab/gitlab.rb   # 修改默认的配置文件；
gitlab-rake gitlab:check SANITIZE=true --trace    # 检查gitlab；
sudo gitlab-ctl tail        # 查看日志；
```

### 

------

### GitLab 工作流

#### <u>1 集中式工作流</u>

![git-workflow-svn-managingconflicts](https://github.com/xirong/my-git/raw/master/images/git-workflow-svn-managingconflicts.png)

##### A 初始化中央仓库

> Bare repository: 裸仓库,即没有工作目录的仓库

```shell
# git init --bare /path/to/repo.git
```

##### B 将项目拷贝到本地机器

```shell
# git clone ssh://git@ec2-52-82-35-48.cn-northwest-1.compute.amazonaws.com.cn:40022/root/FirstProject.git
```

##### C 在本地进行编辑、暂存、提交

```shell
# git status # 查看本地仓库的修改状态
# git add # 暂存文件
# git commit # 提交文件
```

##### D 发布本地提交到中央仓库

```shell
# git push origin master
```

##### E 冲突解决

如果在编辑过程中中央仓库和之前本地克隆是有差别,例如原本中央仓库中只有1.txt文件,但是在你编辑过程中有人已经push了2.txt文件到中央仓库, 在你提交3.txt文件时就会产生冲突. gitlab会给你手动解决冲突的机会,即合并上游的修改到自己的仓库中,--rebase选项告诉Git把提交同步到中央仓库修改后的master分支的顶部,即将当前的修改覆盖到其他修改之上.

```shell
# git pull --rebase origin master
# git push origin master
```

![img](https://github.com/xirong/my-git/raw/master/images/git-workflow-svn-6.png)

##### F 冲突回滚

如果碰到了冲突搞不定,可以通过执行下面这条命令, 就可以回到你执行git pull —rebase之前的样子

```shell
# git rebase --abort
```

#### <u>2 功能分支工作流</u>

功能分支工作流以集中式工作流为基础, 不同的是为各个新功能分配一个专门的分支来开发. 这样可以把新功能集成到正式项目前,用Pull request 的方式讨论变更.

功能分支工作流仍然用中央仓库，并且`master`分支还是代表了正式项目的历史。 但不是直接提交本地历史到各自的本地`master`分支，开发者每次在开始新功能前先创建一个新分支。 功能分支应该有个有描述性的名字，比如`animated-menu-items`或`issue-#1061`，这样可以让分支有个清楚且高聚焦的用途。

![img](https://github.com/xirong/my-git/raw/master/images/git-workflow-feature-branch-1.png)

* Pull Request作为code review的方式.

##### A 创建分支 (如下命令创建了一个基于master的marys-feature的分支, -b选项表示如果该分支还不存在则新建)

```shell
# git checkout -b marys-feature master
```

##### B 编辑、暂存和提交修改

```shell
# git status
# git add <some-file>
# git commit
```

##### C push Marys-feature分支到中央仓库( origin ).

```shell
# git push -u origin marys-feature
```

-u : 设置本地分支去跟中远程对应分支,设置后跟踪的分支后, 就可以使用git push命令省去指定推送分支的参数.

D 完成功能开发

```shell
# git push
```

然后可以在Git UI客户端发起Pull Request, 请求合并marys-features到master, 团队成员会自动收到通知. Pull Request 很酷的是可以在相关的提交旁边显示评注,其他人可以对某个变更集提问.

##### E 其他人也可以拉取这个分支做修改,修改完成后push到中央仓库

```shell
# git checkout master             # 检出master分支并确认是它是最新的
# git pull                        
# git pull origin marys-feature   # 合并marys-feature分支到和已经和远程一致的本地master分支
# git push                        # 最后更新的master分支要重新push回到origin
```

![image-20180921192007439](/var/folders/29/z_fk0qxn5t12y6f3tpmydmyr0000gn/T/abnerworks.Typora/image-20180921192007439.png)

#### <u>3 Gitflow工作流</u>

![Git Workflows: Gitflow Cycle](https://github.com/xirong/my-git/raw/master/images/git-workflows-gitflow.png)

> Gitflow工作流定义了一个围绕项目发布的严格分支模型,虽然比功能分支工作流复杂,但是提供了用于一个健壮的用于管理大型项目的框架.

##### <u>历史分支</u>

相对于使用仅有一个master分支, Gitflow工作流使用两个分支来记录项目的历史. master分支存储了正式发布的历史, 而developer分支作为功能的集成分支. 这样方便master分支上的所有提交分配一个版本号.

![img](https://github.com/xirong/my-git/raw/master/images/git-workflow-release-cycle-1historical.png)

##### <u>功能分支</u>

每个新功能位于一个自己的分支,但功能分支不是从master分支上拉出新分支, 而是使用develope分支作为副分支.当新功能完成时, 合并回develop分支. 新功能分支不直接与developer分支交互.

![img](https://github.com/xirong/my-git/raw/master/images/git-workflow-release-cycle-2feature.png)

##### <u>发布分支</u>

一旦develop上做了一次发布的足够功能, 就从develop分支上checkout一个发布分支. 新建的分支用于开始发布循环,所以从这个时间点之后的新功能不能再加到这个分支上 —— 这个分支只应该做Bug修复、文档生成和其他面向发布任务.

常用的分支约定:

```
用于新建发布分支的分支: develop
用于合并的分支: master
分支命名: release-* 或 release/*
```

##### <u>维护分支</u>

维护分支或说是热修复（`hotfix`）分支用于给产品发布版本（`production releases`）快速生成补丁，这是唯一可以直接从`master`分支`fork`出来的分支。 修复完成，修改应该马上合并回`master`分支和`develop`分支（当前的发布分支），`master`分支应该用新的版本号打好`Tag`。

![img](https://github.com/xirong/my-git/raw/master/images/git-workflow-release-cycle-4maintenance.png)

##### <u>示例</u>

* 创建develop分支,并push到服务器

```shell
git branch develop
git push -u origin develop
```

master --> master

                          |

                         developer

其他开发者克隆中央仓库,建好develop分支的**跟踪分支**:

```
git clone ssh://user@host/path/to/repo.git
git checkout -b develop origin/develop
```

* 开始开发新功能, 在develop分支下创建不同的功能分支,开发不同的功能

```
git checkout -b some-feature develop  #基于develop分支创建新的功能分支,注意新分支不是基于master分支的
# 用老套路添加提交到各自功能分支上：编辑、暂存、提交
git status
git add <some-file>
git commit
```

master --> master

                          |

                         developer

                         |

                         some-feature

* 完成功能开发, 将some-feature合并到develop分支后push到中央仓库

```shell
git pull origin develop         #在合并功能前确保develop分支是最新的
# 将some-featue分支合并到develop分支上
git checkout develop            
git merge some-feature
git push                        # push到中央仓库  
git branch -d some-feature      # 删除some-feature分支
```

* 准备发布, 创建发布分支release-0.1, 并合并到master分支和develop分支. (发布分支相当于develop分支到mater分支的缓冲).  

> 合并回`develop`分支很重要，因为在发布分支中已经提交的更新需要在后面的新功能中也要是可用的。

master --> master

                        |

                       Release-0.1

                          |

                         developer             ---         developer

                         |                                                 |

                         some-feature        ——        some-feature



```shell
# 合并到master分支
git checkout master
git merge release-0.1
git push
# 合并到develop分支
git checkout develop
git merge release-0.1
git push
# 删除发布分支
git branch -d release-0.1
```

* 打好Tag方便追踪

```shell
git tag -a 0.1 -m "Initial public release" master
git push --tags
```

### 附录

------

Git Global setup

```shell
git config --global user.name "Administrator"
git config --global user.email "admin@example.com"
```

Create a new repository

```shell
git clone git@ec2-52-82-35-48.cn-northwest-1.compute.amazonaws.com.cn:root/SecondProject.git
cd SecondProject
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

Existing folder

```shell
cd existing_folder
git init
git remote add origin git@ec2-52-82-35-48.cn-northwest-1.compute.amazonaws.com.cn:root/SecondProject.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

Existing Git Repository

```shell
cd existing_repo
git remote rename origin old-origin
git remote add origin git@ec2-52-82-35-48.cn-northwest-1.compute.amazonaws.com.cn:root/SecondProject.git
git push -u origin --all
git push -u origin --tags
```
