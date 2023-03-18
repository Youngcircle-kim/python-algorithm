import sys

A, B, V = map(int, sys.stdin.readline().split())
res = (V-B)/(A-B)

print(int(res) if res == int(res) else int(res)+1)
