import sys

L = int(sys.stdin.readline())
line = input()
r = 31
res = 0

for i in range(L):
    num = ord(line[i]) - 96
    j = r ** i
    res += num * j
print(res % 1234567891)
