---
title:
- python in action
subtitle:
- Lesson 10 - 如何进一步学习
author:
- 凤凰山 [github.com/gxtrobot/pyinaction](https://github.com/gxtrobot/pyinaction)
date:
- 2019-12
theme:
- Copenhagen
---

# Lesson 10 - 如何进一步学习

## 课程内容
今天的课程将介绍快速总结下学过的内容, 并谈谈如何进一步学习Python, 并开发自己的项目

## 课程目标
- 快速通过IDLE回顾下学过的内容
- 谈下如何获取帮助
- 一些进一步学习资料书籍
- Python的用途介绍, 以及相关类库
- 最后一个程序(完成考试分数报告程序最终版)

# 基础快速回顾
## IDLE 玩一玩
```python
# 基本数据类型
type(1)
type(3.14)
type('a')
type(True)
type(None)

# 容器数据类型
type([1,2,3])
type(('jack', 30))
type({'name':'jack', 'age':30})
type({1,2,3})
```
# 基础快速回顾
## IDLE 玩一玩
```python
# 基本计算
1 + 2
3 - 1
3 * 4
4 / 2
4 // 3
2 ** 3
10 % 3
# 字符串
'hello'
"Hello"
'''Hello'''
'hello' + 'world'
'hello' * 3
'hello world'.split()
len('hello')
```
# 基础快速回顾
## IDLE 玩一玩
```python
# 数据转换
int(3.14)
float(3)
int('3.14')
str(3.14)
int('a')

# 变量
a = 1
b = 2
a + b
c = a + b
```
# 基础快速回顾
## IDLE 玩一玩
```python
# list 操作
a = [1,2,3,4,5]
a[0]
a[-1]
a[:3]
a[1:3]
len(a)
a + [5,6]

# dict 操作
a = {'name':'jack', 'age';30}
a['name']
a.get('name')
a['job'] = 'teacher'
'age' in a
```
# 基础快速回顾
## IDLE 玩一玩
```python
# set 操作
a = {1,2,3,4,5}
b = {2,4,6,7}
a & b
a | b
a - b
b - a

# tuple 操作同list
a = (1,2,3,4)
a[1]
a[:2]
a[0]=10
```

# 基础快速回顾
## IDLE 玩一玩
```python
# 逻辑运算符
True and False
True or False
1 or False
bool(1)
bool('a')
bool(0)
a = 80
a > 0 and  a < 100
```
# 基础快速回顾
## IDLE 玩一玩
```python
# 条件判断
a = 80
b = 60
if a > b:
    print('a is bigger')
elif b > a:
    print('b is bigger')
else:
    print('a, b are equal')

# 循环
for i in range(5):
    print(i)
```

# 基础快速回顾
## IDLE 玩一玩
```python
i = 0
while i < 5:
    print(i)
    i += 1
# 函数
def add(a,b):
    print(a + b)
add(1,2)
def add(*args):
    s = 0
    for n in args:
        s += n
    print(s)

add(1,2,3,4)
```

# 基础快速回顾
## IDLE 玩一玩
```python
# 异常处理
1/0
try:
    1/0
except Exception as ex:
    print(ex)

try:
    raise ValueError('value is wrong')
except Exception as ex:
    print(ex)
```



# 如何获取帮助
## 开发文档获取帮助
- help(obj), 可以传入任意函数名, 类名, 模块名
- dir(obj), 列出对象里的所有属性, 包括数据, 函数方法等
- `builtins` 默认导入模块, 可以看看里面所有内容`dir(builtins)`
- 官网帮助, 有中文版 `https://docs.python.org/3/`

## 程序错误获取帮助
- google 查询错误信息
- stackoverflow.com 查询或发帖子
- github, 某具体类库的issues里面可以看问题, 或提问

# Python 相关资料和书
- 官网Python tutorial, 有中文
  - 内容: 初级
  - `https://docs.python.org/3/tutorial/index.html`
- Python 学习手册第五版(Learning Python)
  - 内容: 初中级
  - `https://item.jd.com/12452929.html`
- 流畅的Python (Fluent Python)
  - 内容: 中高级
  - `https://item.jd.com/12186192.html`
- Python Cookbook（第3版)
  - 内容: 中高级, 偏重技巧, 实例
  - `https://item.jd.com/11681561.html`

# Python的用途介绍, 以及相关类库
## 用途及类库

完成基础语法学习后, 应该选定一个进一步学习的方向, 以开发项目为目标学习, 效果更好

- web开发
  - Bottle (超级小)
  - Flask (小而精)
  - Django (大而全)

- 爬虫开发
  - Scrapy (大而全)
  - aspider(小, 本人开发)

- 数据库
  - sqlalchemy (大而全)
  - peewee (小而精)

- 数据分析
- 自动化测试
- 机器学习

# 写一个小程序
```
学号,姓名,语文,数学,英语
1,王小明,100,88,90
2,李思思,90,70,85
3,刘畅,88,78,92
```
完成reporting_scores_final.py , 分数处理程序最终版


# 课后练习
- 重写reporting_scores_final.py, 不用类的方式
- 使用数据库存取数据
- 编写一个web界面, 可以多人使用, 在线提交数据查看报告

# 感谢

总算结束了我的第一套教程, 由于水平有限, 如有错误问题, 请大家及时提出,
我后面也会制作其他的教程, 谢谢!

不论如何, 编程总是有很多困难和问题的, 最终只能靠你自己去探索并解决你的问题, 但
如果坚持下来, 肯定是值得的, 祝大家学习顺利.