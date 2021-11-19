numStones = int(input())
while True:
    if (numStones == 1):
        print("Alice")
    elif (numStones % 2) == 0:
        print("Bob")
    else:
        print("Alice")
