set1 = set([x for x in range(1, 31)])
lst = []

i =0
while i < 29:
    lst.append(int(input()))
    if len(lst) == 28:
        break
    i += 1

set2 = set(lst)

diff = set1.symmetric_difference(set2)

for i in diff:
    print(i)