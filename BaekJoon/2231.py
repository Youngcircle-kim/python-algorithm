import sys

num = int(sys.stdin.readline())

for i in range(1, num+1):
    res = i + sum(map(int, str(i)))
    if res == num:
        print(i)
        sys.exit()
    if i == num:
        print(0)