import sys

for _ in range(int(sys.stdin.readline())):
    str = sys.stdin.readline()
    ans = 0; res = 0

    for x in str:
        if x == 'O':
            ans += 1
            res += ans
        else:
            ans = 0
    print(res)
