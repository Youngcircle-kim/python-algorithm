import sys

k = int(sys.stdin.readline())
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline()))

lst = sorted(lst, reverse=True)
res = 0
cnt = 1

for i in range(k):
    if cnt %3 == 0:
        cnt = 1
        continue

    res += lst[i]
    cnt += 1

print(res)