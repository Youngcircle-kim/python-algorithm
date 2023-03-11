from sys import stdin

for _ in range(3):
    lst = []
    index = int(stdin.readline())
    for _ in range(index):
        lst.append(int(stdin.readline()))

    if sum(lst) > 0:
        print('+')
    elif sum(lst) < 0:
        print('-')
    else:
        print(0)