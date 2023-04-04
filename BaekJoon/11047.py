import sys

n, m = map(int, sys.stdin.readline().split())
lst = []
res = 0

for _ in range(n):
    lst.append(int(sys.stdin.readline()))

for i in range(n-1,-1, -1):
    if m//lst[i] > 0:
       res += m//lst[i]
       m %= lst[i]

print(res)