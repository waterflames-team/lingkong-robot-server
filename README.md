# lingkong-robot-server
----
**根据[lingkong-robot](https://gitee.com/lingkonggzs/lingkong-robot)所开发的在线版**

#### 有关灵空机器人的介绍

* 灵空机器人是一个由非凡小王开发、折腾调协助维护的灵活可配的中文语音对话机器人，并根据wukong-robot进行改编（改编部分较多，主要借鉴了悟空后台端）。
* 灵空机器人在线版可以做到正常的闲聊，以及查询天气等实用工具的文字对话使用。
* 这个版本只支持文字对话！！！语言对话请见[lingkong-robot](https://gitee.com/lingkonggzs/lingkong-robot)
#### 跳转
----
[灵空文档](http://docs.lingkong-robot.cn)(包括灵空在线和灵空本地的使用说明)/[灵空在线](http://server.lingkong.store:88/)（账号随意，密码12345）/[灵空主体](https://gitee.com/lingkonggzs/lingkong-robot)



# 联系作者
----

> 如果你有问题，请你通过以下方式联系非凡小王（作者）

* 作者钉钉：15392006285（加好友请说明来历）

* 作者qq：2822603942（加好友请说明来历）


# 运行环境
----
> * 1.使用者如是win平台，那么请去deepin官网和virtualbox官网下载deepin的镜像和virtualbox的安装包，然后进行安装、装载镜像
>> * 2.如果你刚安装好deepin，请执行
```shell
    sudo apt update
    sudo apt-get install git
```
安装git，然后自行确定你的deepin有没有python3环境（正常来说是有的）


* 使用者如是Mac平台，那么可以直接开始安装了

* 使用者如果是deepin平台，那么参考win平台的方法

* 使用者如是非deepin的linux平台，那你可以暂时参考一下debian的安装方法，如有问题，欢迎通过下面的联系方式，联系作者
# 安装环境（Mac）
---

* 首先你要下载好0.5.9.200321版的灵空机器人
```shell
git clone https://gitee.com/lingkonggzs/lingkong-robot-server.git
```

### 开始安装：
----
**首先你要保证你已经安装了python3和pip3，没安装的可以百度**

1.
```shell
cd lingkong-robot-server
```
2.
```shell
./install.sh
```
**并且中途如果出现Press RETURN to continue or any other key to abort需要按一下回车，如果出现password：需要输入密码**

* 到这里你的环境安装就完成了
* 如果你安装出现了问题，欢迎你去介绍页找到作者的联系方式以联系作者
----

# 安装环境（deepin）
----
* 此安装部分已在deepin、debian、rasbian上测试成功，如出现安装失败的情况，请联系非凡小王，qq:2822603942


1. 首先你要下载好0.5.9.200321版的灵空机器人
```shell
git clone https://gitee.com/lingkonggzs/lingkong-robot-server.git
```
2. 首先你要保证你已经安装了python3和pip3，没安装的可以百度


* 如果你想要换源可执行
```shell
sudo curl -L http://download.lingkong-robot.online/change.sh | sudo bash
```
3.
```shell
cd lingkong-robot-server
./install.sh
```

* 到这里你的环境安装就完成了

***（如果换源时长时间没有动静，那么是需要密码的，执行完一键命令后输入用户密码再按下回车就可以换源啦）***

***(如果换源时出现“need root”或者没有更换成功，那么请手动下载：***
```shell
wget http://download.lingkong-robot.online/change.sh
sudo sh change.sh
```
***注意：这两条是需要分别执行的！！！在执行第二句时可能需要密码！输入并按下回车即可！！！）***
### 如果你安装不成功，那么请去文档的介绍页联系作者



#### 在线版与本地版的区别
----
##### ①

在线版：所有都无调用限制

本地版：前期因紧急，所以用的都是有限制次数的，在线版完工后本地版也会做无调用限制

##### ②

在线版：支持win、安卓、ios、mac、linux等所有支持浏览器的平台，但体验到的东西比本地版少

本地版：仅支持mac、linux（目前只测试到了deepin，按常理debian也是相同道理，所以debian有可能也能用）平台，但是体验到的东西是最多的，作者的维护力度和更新力度也比在线版大

#### 在线版功能
----
基本与灵空机器人本地版的后台相同，只不过做了一些适配和加了一些在线版必须的一些功能

#### 一些问题
----
##### 手机端无左侧的菜单？

方案一：部分手机横屏就可以出现左侧菜单

方案二：记住路径（"/"为介绍页，"/ds"是打赏页,"/log"是日志页,"/study"是修改配置项教程页,"/dh"是对话页,"/list"是清单页，此路径适用于0.5.7.200316版及以上）

#### 