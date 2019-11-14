import sys
print(sys.argv)
print(len(sys.argv))
print(sys.argv[1:])
a = sys.argv[1]
b = sys.argv[2]
c = sys.argv[3]
print(int(a) + int(b) + int(c))