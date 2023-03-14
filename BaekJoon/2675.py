import sys

for _ in range(int(sys.stdin.readline())):
    num, str = sys.stdin.readline().split()
    res = ''
    for i in range(len(str)):
        res += str[i] * int(num)
    print(res)