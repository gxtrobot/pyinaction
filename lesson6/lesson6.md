---
title:
- python in action
subtitle:
- Lesson 6 - 函数的进阶
author:
- 凤凰山 [github.com/gxtrobot/pyinaction](https://github.com/gxtrobot/pyinaction)
date:
- 2019-11
theme:
- Copenhagen
---

# Lesson 6 - 函数的进阶

## 课程内容
今天的课程将介绍Python的函数的更多进阶用法, 包括各种参数的使用, 函数作为普通值的使用

## 课程目标
- 了解并使用函数的位置参数和关键字参数
- 了解函数参数默认值的用法
- 了解函数的文档字符串用法
- 了解函数的不固定参数的用法
- 了解函数作为普通值的用法

# 函数的位置参数和关键字参数

## 按位置传参数
```python
def print_person(name, age, salary):
    print('name is {}, {} years old,\
    now make {} RMB a month'.format(
        name, age, salary))
```
- 可以按位置逐一传递参数
- 顺序是重要的, 不能搞错

## 按关键字传参数
- 按参数名关键字传参数
- 可以不按照顺序

# IDLE 玩一玩
在IDLE 试着使用不同方式调用以上函数
```python
print_person('jack', 40, 12000)

print_person('jack', salary= 12000, age=40)

print_person(salary= 12000, age=40, name='jack')

print_person(salary= 12000, 'jack', 40)
```

# 函数使用参数默认值
## 参数默认值
```python
def print_person(name, age, salary=6000):
    print('name is {}, {} years old,\
     now make {} RMB a month'.format(
        name, age, salary))
```

- 参数名后跟上`=`, 和一个默认值
- 这样在调用时如果没有传入该参数, 函数就使用默认值
- 如果有传入值则使用传入的值

# IDLE 玩一玩
在IDLE 试着使用不同方式调用以上函数
```python
print_person('jack', 40, 8000)

print_person('jack',  40)

print_person('jack', age=40)

print_person('jack', 40, salary=12000)


```

# 函数的文档字符串

## 文档字符串
```python
def getsum(score_list):
    '''
    该函数将计算一个分数列表的总和

    Args:
        score_list: a list of scores

    Returns:
        float: total score
    '''
```
- 在函数使用三引号字符串
- 该字符串会作为函数的说明文档使用
- 一般包含三项内容, 函数用途说明, 参数说明, 返回值说明
- 可以使用`help` 函数查看该文档
- 尽量在自己定义的每个函数使用文档字符串, 作为注释参考, 方便自己和他人


# 函数的不固定参数
## 使用不固定位置参数

```python
def getsum(a,b, *args):
    total = a + b
    for v in args:
        total = total + a
    return total
```

- 如果参数列表中出现`*`,后跟一个参数名, 这是不固定位置参数列表
- 可以接收任意个位置参数
- 在函数内可以将该参数作为一个list使用

# IDLE 玩一玩
测试传递不同个数参数给函数
```python
getsum(100,80)
getsum(100,90,50)
getsum(100,40, 79, 81, 90)

```
## 使用不固定关键字参数

```python
def print_person(name,age,salary, **kwargs):
    print('name is {}, {} years old, \
    now make {} RMB a month'.format(
        name, age, salary))
    print('\n *** other info***')
    for key in kwargs:
        print('{}:{}'.format(key, kwargs[key]))
```
- 如果参数列表中出现`**`,后跟一个参数名, 这是不固定关键字参数列表
- 可以接收任意个关键字参数
- 在函数内可以将该参数作为一个dict使用

# IDLE 玩一玩
测试传递不同关键字参数给函数

```python
print_person('jack', 30, 10000, height=175)

print_person('jack', 30, 10000, height=175, weight=180)

print_person('jack', 30, 10000, height=175, weight=180
        , home='beijing')
```

# 函数作为值使用
## 函数可以作为一个普通值操作
- 可以将函数赋给一个变量
- 可以将函数作为参数传给另一个函数
- 可以将函数作为值从另一个函数返回



# 一个小程序: 计算器
存为calc.py
```python
def mul(a,b):
    return  a * b

def add(a,b)
    return a + b

math_dict = {'*': mul,
    '+': add
}

op = sys.argv[1]
func = math_dict.get(op)
a = sys.argv[2]
b = sys.argv[3]

print(func(a,b))
```
# 课后练习

- 在calc.py程序增加div(除法), sub(减法)
- 编写一个函数report, 该函数接收任意个位置参数, 传入参数为int, 打印出参数个数, 总和, 平均值

# 问题

