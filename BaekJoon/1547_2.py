import sys

n = 1

for _ in range(int(sys.stdin.readline())):
    a, b = map(int, sys.stdin.readline().split())
    if a == n:
        n =b
    elif b == n:
        n = a
print(n)