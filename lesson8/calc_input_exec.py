
def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):

    try:
        return a / b
    except Exception as ex:
        print('error', ex.__class__)
        print('error', ex)


op_dict = {
    '+': add,
    '*': mul,
    '-': sub,
    '/': div
}

if __name__ == "__main__":
    while True:
        s = input('please enter(+ 1 2): ')
        s_list = s.split()
        func = op_dict.get(s_list[0])
        result = func(int(s_list[1]), int(s_list[2]))
        print('result:', result)
