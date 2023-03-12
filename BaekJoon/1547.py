import sys

input = sys.stdin.readline

frequency = int(input())
lst = [x for x in range(1, 4)]

for _ in range(frequency):
    a, b = map(int, input().split())

    i = lst.index(a)
    j = lst.index(b)

    lst[i], lst[j] = lst[j], lst[i]

print(lst[0])