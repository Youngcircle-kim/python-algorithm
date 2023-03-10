N = int(input())
arr1 = [0] * 3
arr2 = [0] * 3

for _ in range(N):
    x, y, z = map(int, input().split())

    arr1[0] += x
    arr1[1] += y
    arr1[2] += z

    arr2[0] += (x * x)
    arr2[1] += (y * y)
    arr2[2] += (z * z)

max_value = max(arr1)
if arr1.count(max_value) == 1:
    for i in range(len(arr1)):
        if arr1[i] == max_value:
            print(i + 1, max_value)
            break
else:
    pow_max_value = max(arr2)
    idx = 0
    for i in range(len(arr2)):
        if arr2[i] == pow_max_value:
            idx = i
            break

    if arr2.count(pow_max_value) > 1:
        print(0, arr1[idx])

    else:
        print(idx + 1, arr1[idx])
