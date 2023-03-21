import sys

max = 0
lst = []
n = int(sys.stdin.readline())

for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst = sorted(lst, reverse=True)

for i in range(len(lst)):
    if max < lst[i] * (i+1):
        max = lst[i] * (i+1)

print(max)