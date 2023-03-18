import sys
lst = []

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    lst.append([a,b])
lst = sorted(lst)
for i in range(len(lst)):
    for j in range(2):
        print(lst[i][j], end=" ")
    print()
