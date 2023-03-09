sum = 0
lst = []
distinction1 = 0
distinction2 = 0
for _ in range(10):
    num = int(input())
    lst.append(num)

for i in range(len(lst)):
    sum2 = sum
    sum += lst[i]
    distinction1 = 100 - sum2
    distinction2 = 100 - sum
    if distinction1 < -distinction2:
        print(100 - distinction1)
        break
    elif distinction1 == distinction2:
        print(sum)
        break
    elif i+1 == len(lst):
        print(sum)
