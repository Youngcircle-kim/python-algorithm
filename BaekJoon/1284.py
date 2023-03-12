while True:
    str = input()
    res = 0
    if str == '0':
        break
    for i in range(len(str)):
        res += 1
        if str[i] == '1':
            res += 2
        elif str[i] == '0':
            res += 4
        else:
            res += 3

    res += 1

    print(res)