import sys
name = 'world'

print('module name', __name__)
if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    print('hello', name)