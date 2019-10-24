---
title:
- python in action
subtitle:
- Lesson 1 - 准备环境
author:
- 凤凰山 [github.com/gxtrobot/pyinaction](https://github.com/gxtrobot/pyinaction)
date:
- 2019-10
theme:
- Copenhagen
---

# Lesson1 - Python 开发环境准备

## 课程内容
今天的课程将演示如何在windows10上从头准备一个python开发环境, 包括软件的安装以及一些设置. 环境准备好以后, 为以后学习python 搭建一个好的基础, 方便写代码, 运行python程序等.


## 课程目标
- 成功安装Python, vscode
- 可以运行Python 解释器, IDLE程序
- 可以在命令行运行Python 程序
- 可以使用IDLE完成一些简单的开发工作
- 使用vscode创建一个项目, 虚拟环境的创建
- 使用pip安装包
- 使用douban源加速包安装

# 安装 Python

安装Python 的 3.7以上版本, 这里演示使用的是最新3.7.5版

下载地址: [python.org](python.org)

# 安装 vscode

安装vscode 最新版本, 这里使用的是1.39版

下载地址: [https://code.visualstudio.com/](https://code.visualstudio.com/)


# 确认Python 安装成功

- 运行Python 解释器
- 在命令行运行Python 解释器
- 运行IDLE

# 使用IDLE 开发 helloworld 程序

创建一个程序目录 `c:\dev\pyinaction`

代码: 存为 helloworld.py
```python
print("Hello World")
```

# 使用Python 运行 helloworld 程序

打开cmd程序, 进入程序目录

运行命令:
```shell
python helloworld.py
```

# 玩玩IDLE

- 使用IDLE 练习简单代码
- 使用IDLE 运行pyhton 程序

# vscode创建项目

- 使用vscode 打开目录 `c:\dev\pyinaction`

- python虚拟环境的创建

   运行命令 `python -m venv venv`{.python}

- 激活虚拟环境

   运行命令 `venv\Scripts\activate.bat `

- 运行helloworld程序

# 使用pip管理包

- pip 安装一个包, requests

   运行命令 `pip install requests `

- 列出当前环境安装的包

   运行命令 `pip list `

- douban源的使用, pip.ini文件

   放在 `C:\Users\<username>\pip\pip.ini`

pip.ini 内容
```
[global]
timeout = 60
index-url = https://pypi.doubanio.com/simple
```

# 课后练习

- cmd命令行使用python 解释器, 执行简单算术运算, 例如 1+2
- 修改 helloworld.py, 打印其他内容, 使用vscode运行

# 问题

- powershell 激活 虚拟环境失败, 提示没有权限?

   因为PowerShell默认不允许执行*.ps1脚本文件，所以首先需要开启权限。

   解决方法: 以管理员身份启动PowerShell，并执行`Set-ExecutionPolicy RemoteSigned`

   具体可以看 https://blog.csdn.net/yannanxiu/article/details/78703888