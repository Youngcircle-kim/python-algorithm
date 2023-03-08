list = []

for _ in range(0, 9):
    try:
        num = int(input())
    except:
        break
    list.append(num)

max = 0
index = 0

for i in range(len(list)):
    if list[i] > max:
        max = list[i]
        index = i+1

print(max)
print(index)
