n = 100


def double_it():
    print('double it: ', n)
    # n = 2 * n


def double_it_global():
    global n
    print('double it global: ', n)
    n = 2 * n


double_it()
print('n:', n)
double_it_global()
print('n:', n)
