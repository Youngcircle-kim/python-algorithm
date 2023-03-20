import sys

num = int(sys.stdin.readline())
res = 0

if 0 <= num < 4 and num != 2:
    print(-1)
    sys.exit()

res += num // 5
num %= 5

if num % 2 ==0:
    res += num // 2
    num %= 2
    print(res)
else:
    res -= 1;num += 5
    res += num // 2
    num %= 2
    print(res)