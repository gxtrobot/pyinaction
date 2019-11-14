import sys
print(sys.argv)
print(len(sys.argv))
print(sys.argv[1:])

total = 0
for i in sys.argv[1:]:
    total = total + int(i)

print('total=', total)