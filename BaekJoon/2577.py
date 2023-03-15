res = 1
for _ in range(3):
    res *= int(input())

for i in range(10):
    print(str(res).count(str(i)))