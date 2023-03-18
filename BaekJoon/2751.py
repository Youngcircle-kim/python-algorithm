import sys

lst = []

for _ in range(int(sys.stdin.readline())):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst)

for i in range(len(lst)):
    print(lst[i])