from sys import stdin

n = int(stdin.readline())

str = stdin.readline().rstrip()

lst = []

for i in range(0, len(str), n):
    lst.append(list(str[i: i + n]))

for i in range(len(lst)):
    if i % 2 != 0:
        data = list(reversed(lst[i]))
        lst[i] = data

res = ''

for j in range(n):
    for i in range(len(lst)):
       res += lst[i][j]

print(res)