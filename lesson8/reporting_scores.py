import sys
def report(*args):
    count = len(args)
    total  = 0
    avg = 0
    for v in args:
        value = int(v)
        if value < 0:
            raise ValueError('{} must above 0'.format(value))
        total += value
    avg = total / count
    print('count:', count)
    print('total:', total)
    print('avg:', avg)

if __name__ == "__main__":
    f_name = 'scores.txt'
    f = open(f_name)
    scores = f.readlines()
    report(*scores)
    f.close()
