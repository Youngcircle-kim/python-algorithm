lst = []
for _ in range(10):
    lst.append(int(input()) % 42)

set1 = set(lst)

print(len(set1))