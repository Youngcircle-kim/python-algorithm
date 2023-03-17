import sys

N, K = map(int, sys.stdin.readline().split())
res1 = 1
res2 = 1
for i in range(N, N-K, -1):
    res1 *= i
for i in range(1, K+1):
    res2 *= i
print(res1 // res2)