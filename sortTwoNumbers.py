line = input()
a, b = line.split()
a = int(a)
b = int(b)
if a < b:
    print(a, b)
else:
    print(b, a)
    
"""nums = [int(i) for i in input().split()]
print(f"{min(nums)} {max(nums)}")"""
