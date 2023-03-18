import sys

N, M = map(int, sys.stdin.readline().split())
lst1 = []
lst2 = []
for i in range(1, N+1):
    if N % i == 0:
        lst1.append(i)
for i in range(1, M+1):
    if M % i == 0:
        lst2.append(i)
res = set(lst1) & set(lst2)

res = sorted(list(res))

print(list(res)[-1])
print(N*M // list(res)[-1])
