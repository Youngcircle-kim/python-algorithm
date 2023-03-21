import sys

k = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))
res = 0
cnt = 0

for i in range(k):
    cnt += lst[i]
    res += cnt
print(res)