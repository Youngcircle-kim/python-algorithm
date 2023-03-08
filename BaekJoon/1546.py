n = int(input())

lst = list(map(int, input().split()))

max = 0

for i in range(len(lst)):
    if max < lst[i]:
        max = lst[i]

sum = 0.0

for i in range(len(lst)):
    sum += lst[i]/max*100

print(round((sum/n), 2))