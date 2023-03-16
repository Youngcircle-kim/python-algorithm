import sys

for _ in range(int(sys.stdin.readline())):
    x, y, z = map(int, sys.stdin.readline().split())
    room = z//x +1
    floor = z % x
    if floor == 0:
        room -= 1
        floor= x
    print(f'{floor * 100 + room}')