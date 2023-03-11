lst = [] ; total = 0

for _ in range(10):
    a, b = map(int, input().split())
    total += b-a
    lst.append(total)
    
print(max(lst))
