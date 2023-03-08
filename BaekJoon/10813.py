first_line = list(map(int, input().split()))

lst = [x for x in range(1, first_line[0]+1)]

for _ in range(0, first_line[1]):
    line = list(map(int, input().split()))
    index1 = line[0]-1
    index2 = line[1]-1
    lst[index1], lst[index2] = lst[index2], lst[index1]

for i in range(len(lst)):
    print(f'{lst[i]}', end=" ")