import sys

num = int(sys.stdin.readline())

if num == 1:
    print(1)
    sys.exit()
a_n = 2; b_n = 1; n = 2
while 1:
    a_n += 6 * (n-2)
    b_n += 6 * (n-1)
    if a_n <= num <= b_n:
        print(n)
        sys.exit()
    n += 1