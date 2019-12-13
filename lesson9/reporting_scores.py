import sys
def report(*args):
    count = len(args)
    total  = 0
    avg = 0
    for v in args:
        value = int(v)
        if value < 0:
            raise ValueError('{} must above 0'.format(value))
        if value > 100:
            raise ValueError('{} must less than 100'.format(value))
        total += value
    avg = total / count

    lines = []
    lines.append('count:{}\n'.format(count))
    lines.append('total:{}\n'.format(total))
    lines.append('avg:{}\n'.format(avg))
    return lines

if __name__ == "__main__":
    f_name = 'scores.txt'
    f = open(f_name)
    scores = f.readlines()
    f.close()
    lines = report(*scores)
    f_name = 'scores_report.txt'
    f = open(f_name, 'w')
    f.writelines(lines)
    f.close()
