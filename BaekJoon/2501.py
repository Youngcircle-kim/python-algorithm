a, b = map(int, input().split())
lst = []

for i in range(1, a+1):
    if a % i == 0:
        lst.append(i)
try:
    print(sorted(lst)[b-1])
except:
    print(0)