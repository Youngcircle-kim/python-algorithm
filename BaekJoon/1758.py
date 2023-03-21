import sys

n = int(sys.stdin.readline())
res = 0
lst = []

for _ in range(n):
    lst.append(int(sys.stdin.readline()))
lst = sorted(lst, reverse=True)

for i in range(len(lst)):
    if lst[i] - i < 0:
        continue
    else:
        res += lst[i] - i

print(res)