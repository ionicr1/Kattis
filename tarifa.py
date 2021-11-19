from numpy.random import seed
from numpy.random import randint

startingMegs = int(input("Starting MBs: "))
months = int(input("How many months: "))
seed(9)
randMegs = randint(0, startingMegs)
for i in range(months):
    randMegs = randint(0, startingMegs)
    difference = startingMegs - randMegs
    startingMegs += difference
    print("Month {}, difference {} megabyte count {}".format(i + 1,difference,startingMegs))

startingMegs = int(input("Starting MBs: "))
while not startingMegs in range(1,101):
    startingMegs = int(input("Starting MBs: "))
months = int(input("How many months: "))
while not months in range(1,101):
    months = int(input("How many months: "))
used = int(input("Megs used?: "))
leftOver = startingMegs - used
for i in range(months - 1):
    numMonth = startingMegs + leftOver
    used = int(input("Megs used?: "))
    leftOver = numMonth - used
finalMegs = leftOver + startingMegs
print(finalMegs)

"""mb = int(input())
months = int(input())
print((mb * months) - sum([int(input()) for i in range(months)]) + mb)"""
