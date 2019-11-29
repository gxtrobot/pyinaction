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


args = sys.argv[1:]
report(*args)