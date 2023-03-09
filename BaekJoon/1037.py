n = int(input())

lst = list(map(int, input().split()))

if len(lst) == n:
    lst.sort()
    print(lst[0] * lst[len(lst)-1])

