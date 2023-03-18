import sys

for _ in range(int(sys.stdin.readline())):
    N = int(input())
    M = int(input())

    lst = [i for i in range(1,M+1)]

    for i in range(N):
        for j in range(1, M):
            lst[j] += lst[j-1]

    print(lst[-1])