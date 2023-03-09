n = int(input())
org_n = n
i = 0

while True:
    first = n // 10
    second = n % 10
    tmp = first + second
    n = second * 10 + tmp % 10
    i += 1
    if n == org_n:
        break
print(i)