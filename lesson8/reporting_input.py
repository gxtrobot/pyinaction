import sys
def report(*args):
    count = len(args)
    total  = 0
    avg = 0
    for v in args:
        total += int(v)
    avg = total / count
    print('count:', count)
    print('total:', total)
    print('avg:', avg)


if __name__ == "__main__":
    while True:
        args = input('enter number list: ')
        if args == '':
            break
        args_list = args.split()
        report(*args_list)
