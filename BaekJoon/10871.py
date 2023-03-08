first = list(map(int, input().split(" ")))
second = list(map(int, input().split(" ")))

for i in range(len(second)):
    if first[1] > second[i]:
        print(f'{second[i]}', end=" ")