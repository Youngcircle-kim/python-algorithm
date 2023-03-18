import sys

lst = []
for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())

    lst.append([b, a])
lst = sorted(lst)

for i in range(len(lst)):
    print(f'{lst[i][1]} {lst[i][0]}')


