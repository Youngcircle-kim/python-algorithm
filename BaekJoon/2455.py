total = 0
lst = []

for _ in range(4):
    a, b = map(int, input().split())
    total -= a
    lst.append(total)
    total += b
    lst.append(total)
print(sorted(lst)[-1])