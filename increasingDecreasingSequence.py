increasing = False

n = int(input())
mylist = []
for i in range(n):
    num = int(input())
    mylist.append(num)

def incdec(list):
    global increasing
    global n

    for i in range(n):
        if list[i] <=0:
            return False

    for i in range(n-1):
        if list[i+1] > list[i]:
            increasing = True
            
        if increasing == True and list[i] >= list[i+1]:
            return False

    return True

if incdec(mylist) == True:
    print('true')
else:
    print('false')