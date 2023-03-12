import sys

a, b = map(int, sys.stdin.readline().split())

a -= 1 ; b -= 1

print(abs(b // 4 - a // 4) + abs(b % 4 - a % 4))
