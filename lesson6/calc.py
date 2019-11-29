import sys

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

op_dict = {
    '+': add,
    '*': mul,
    '-': sub,
    '/': div
}

op = sys.argv[1]
a = sys.argv[2]
b = sys.argv[3]

func = op_dict.get(op)
result = func(int(a),int(b))
print('result:', result)