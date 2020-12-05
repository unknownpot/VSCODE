n = int(input())
myList = []

myList = list(map(int, input().split()))

def quicksort(list):
    if len(list) <= 1:
        return list

    mid = list[len(list) // 2]
    left = [x for x in list if x < mid]
    middle = [x for x in list if x == mid]
    right = [x for x in list if x > mid]
    return quicksort(left) + middle + quicksort(right)

newList = quicksort(myList)
for i in newList:
    print(i, end=' ')
