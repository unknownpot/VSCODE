n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print(j+1, end=" ")
    for j in range(2*(n - i)-1):
        if j < 0:
            print("")
        else:
            print("*", end=" ")
    print("")
