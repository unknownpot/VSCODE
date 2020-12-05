numString = str(input())
myList = numString.split()
sum = 0

for i in myList:
    sum += int(i)
    if sum >= 0:
        print(i)
    else:
        break
