width = int(input())
pieces = int(input())
area = 0
for i in range(pieces):
    line = input()
    a, b = line.split()
    a = int(a)
    b = int(b)
    area += a * b
print(int(area / width))
