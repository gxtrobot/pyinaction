---
title:
- python in action
subtitle:
- Lesson 2 - 基本数据类型与操作符
author:
- 凤凰山 [github.com/gxtrobot/pyinaction](https://github.com/gxtrobot/pyinaction)
date:
- 2019-10
theme:
- Copenhagen
---

# Lesson2 - 变量, 基本数据类型与操作符

## 课程内容
今天的课程将介绍Python的基本数据类型(int, float, str, bool, None), 以及相关的操作符.
并且知道如何创建一个变量, 并用来保存一个数据.

## 课程目标
- 了解并使用Python基本数据类型
- 对每一种类型知道有哪些对应的操作符可以使用
- 可以使用操作符和数据进行一些计算
- 创建一个变量来保存数据
- 了解常用操作符对数据的要求, 以及可能的错误

# 基本数据类型
- 数字类型
  - 表示一个数字, 可以是整数或小数
  - 整数(int) - 1, 2, 100
  - 浮点数(float) - 0.5, 3.14
  - 操作符(+, -, *, /, //, %, **)

- 字符串(str)
  - 表示一个字符的序列
  - 使用单引号(`'hello'`)
  - 使用双引号(`"hello"`)
  - 使用三引号
    ```python
    '''
    hello
    '''
    ```
  - 操作符(+, *)

  **注意** python 没有单个字符类型, 单个字符也是字符串

- 布尔型(bool)
  - 表示条件满足与否
  - 真(True)
  - 假(False)
  - 操作符(and, or, not)

- 空类型(None)
  - 表示没有值
  - 操作符(is)

# IDLE 玩一玩
在IDLE 试着用每种数据类型, 以及相应操作符进行计算, 并观察结果
```python
10 + 100
10 + 1.1
1.1 + 10.1
10 / 3
10 // 3
10 % 3
10 ** 3
"hello" + "world"
"*" 10
True and False
True or False
not True
10 is None
```

# 定义一个变量

- 使用 “=” , 左边为变量名, 右边为变量值或另一个变量
- 变量名要求: 字母开头, 后面跟字母, 数字, “_“
- 命名习惯: 全小写, 多单词用 ”_“ 分隔

```python
a = 1
a = "hello"
b = a
user_name = 'jack'
```

# 不同类型数值计算
## 可以混合计算的情况
- 可以互相转化的类型可以混合使用计算
- 整数和浮点数计算结果为浮点数
```python
10 + 1.1
1 * 3 - 0.5
```
## 不可以混合计算的情况
- 系统会报错并抛出异常(Exception)
```python
"a" + 1
1 + "a"
```


# IDLE 玩一玩
试试不同数据类型计算可能产生的结果和错误
```python
10 + 1.1
"a" + 1
True + 1
None + 1
```

# 常见函数学习
## type
- 使用type可以检查任意数据类型
```python
type(1)
type(3.14)
type('a')
type(True)
type(None)
```

# 课后练习

- 定义两个变量, 如 a=10, b=1, 使用各种操作符进行计算
- 定义一个字符串, 使用+, *计算
- 测试不同类型数据计算, 并观察结果和错误
- 使用type检查各种数据类型

# 问题

