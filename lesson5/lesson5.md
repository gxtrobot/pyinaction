---
title:
- python in action
subtitle:
- Lesson 5 - 分支控制和函数初步
author:
- 凤凰山 [github.com/gxtrobot/pyinaction](https://github.com/gxtrobot/pyinaction)
date:
- 2019-11
theme:
- Copenhagen
---

# Lesson5 - 分支控制和函数初步

## 课程内容
今天的课程将介绍Python的逻辑操作符, 以及分支控制语句if的用法, 包括if, else, elif的几种形式. 然后介绍函数的初步知识, 如何定义函数.

## 课程目标
- 了解并使用Python的逻辑操作符
- 了解使用if语句
- 了解使用if...else...语句
- 了解使用if...elif...else语句
- 了解如何定义函数
- 编写一个函数来对一个列表的所有值求和

# 逻辑操作符

## 用来组合条件(bool值)的操作符
-  `and , or, not`
- 接收一个或2个bool值, 返回一个bool值
- `A and B, 两个条件须同时成立, 结果为真, 否则为假`
- `A or B, 两个条件有一个成立, 结果为真, 否则为假`
- `not A, A 为真返回假, A为假返回真`
- `and, or具有短路特性, 意思就是如果只看第一个值就能确定最终结果的时候直接返回, 不会看第二个值`

# IDLE 玩一玩
在IDLE 试着使用逻辑操作符, 并查看结果
```python
a = 5
b = 3
c = 10

a > b and c > b
a > b or b > c
not a > b

b > a and print(1)
b < a and print(1)

c > a or print(1)
c < a or print(1)
```

# 使用if语句
## 单独使用if
可能执行一个语句块或跳过
```python
score = 70
if score >= 60:
    print('passed')
```

- if 后接一个条件判断 bool值表达式
- 当条件为真时, 语句块就执行, 继续执行语句块后语句
- 当条件为假时, 跳过语句块, 继续执行语句块后语句
- if语句第一行以':' 结束, 后面跟缩进语句块

# 使用if语句

## 使用if...else...
两个语句块, 二选一执行

```python
score = 70
if score >= 60:
    print('passed')
else:
    print('not passed')
```

- if后跟一个条件判断bool值表达式, 然后接一个语句块
- else后直接跟一个语句块
- if后条件为真, 执行if语句块, 条件为假, 执行else语句块
- 两个语句块必然有一个会执行

# 使用if语句
## 使用if...elif...else
多个语句块, N选一执行

```python
score = 80
if score >= 90:
    print('very good ')
elif score >= 60:
    print('passed')
else:
    print('not passed')
```

- if后跟一个条件判断bool值表达式, 然后接一个语句块
- 然后可以跟若干个elif 语句, 每个都接一个bool表达式和一个语句块
- 最后可以接一个else语句, 没有bool值表达式, 直接跟一个语句块
- 从最开始的if开始, 按顺序判断每个bool表达式, 如果为真就执行相应语句块, 然后结束整个
  if控制语句, 继续后面语句执行
- 如果没有一个条件为真, 则执行else对应语句块

# IDLE 玩一玩
```
测试以上的各种if语句
```

# 定义函数

```python
def getsum(score_list):
    pass
```
- `def` 语句定义一个函数
- def后 接函数名, 函数名需要满足python的命名规则, 且不能和系统函数同名, 否则会覆盖系   统函数
- 函数名后用(), 圆括号内为逗号分隔的参数列表
- 下面跟一个缩进语句块, 代表函数具体执行内容
- `pass` 可以代表一个空语句块, 可以用来临时占位使用, 不会报错
- 如果需要返回值, 可以用return语句后接返回的值, return执行后立即结束函数并返回值
- 如果没有return语句, 函数默认返回 `None` 值
- 调用函数使用函数名(), 圆括号内用逗号分隔要传输的参数列表

# IDLE 玩一玩
```python
a = [1,2,3,4]
def getsum(score_list):
    total = 0
    for score in score_list:
        total = total + score
    return total

total = getsum(a)
print(total)

def print_list(score_list):
    for score in score_list:
        print('score:', score)

res = print_list(a)
print('res:', res)
```

# 课后练习

- 编写一个函数, getavg(score_list), 求列表的平均值
- 编写一个函数, getrate(score), 求分数的分级(>=90 为A, 75到90为B, 60到75为C, 低于60 为D)

# 问题

