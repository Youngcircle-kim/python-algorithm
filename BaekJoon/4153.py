import sys
while 1:
    lst = list(map(int, sys.stdin.readline().split()))
    lst = sorted(lst)
    x, y, z = lst[0], lst[1], lst[2]
    if x == 0 or y == 0 or z == 0:
        sys.exit()
    if x*x + y*y == z*z:
        print("right")
    else:
        print("wrong")
