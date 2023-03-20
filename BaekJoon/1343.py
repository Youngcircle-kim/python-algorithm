import os
import sys

lst = list(map(str, input().split(".")))

for i in range(len(lst)):
    if len(lst[i]) % 2 != 0:
        print(-1)
        sys.exit()


for i in range(len(lst)):
    cnt = 0
    for j in range(len(lst[i])):
        if lst[i][j] == 'X':
            cnt += 1
        if cnt%4 == 0:
            cnt -= 4
            print('AAAA',end='')
    if cnt == 2:
        print('BB', end='')
    if i != len(lst)-1:
        print('.', end='')