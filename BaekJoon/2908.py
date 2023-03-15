num1, num2 = map(str, input().split())

reversed_num1 = int(num1[::-1])
reversed_num2 = int(num2[::-1])

if reversed_num2 < reversed_num1:
    print(reversed_num1)
else:
    print(reversed_num2)

