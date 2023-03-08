n = int(input())
sum = 0
str = input()

if n == len(str):
    for i in range(len(str)):
        sum += int(str[i])
print(sum)