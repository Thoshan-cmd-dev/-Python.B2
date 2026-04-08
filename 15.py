from math import sqrt
myList = []
tot = 0
n = int(input("Enter the number of items :"))
print("enter", n ,"the items:")
for i in range(n):
    item = int(input())
    myList = myList + [item]
    tot += item
    mean = tot/n
    tot = 0
    for item in myList:
        tot +=(item - mean)*(item - mean)
    var = tot/n
    std = sqrt(var)
    print("Mean =",mean)
    print("Variance = ", var)
    print("standard Deviration =",std)

