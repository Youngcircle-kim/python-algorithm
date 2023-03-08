n = int(input())

for _ in range(n):

    str_list = input()

    if len(str_list) == 1:
        print(f'{str_list[0]}{str_list[0]}')
    else:
        print(f'{str_list[0]}{str_list[len(str_list)-1]}')
