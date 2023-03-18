import sys
lst = [0] * 10001
# 계수 정렬
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    lst[n-1] += 1

for i in range(10001):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i+1)