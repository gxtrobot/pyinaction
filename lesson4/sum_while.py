import sys
print(sys.argv)
print(len(sys.argv))
print(sys.argv[1:])
nums = sys.argv[1:]
total = 0
i = 0 
while i < len(nums):
    total = total + int(nums[i])
    i = i + 1

print('total=', total)