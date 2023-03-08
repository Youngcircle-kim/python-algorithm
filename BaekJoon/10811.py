lst1 = list(map(int, input().split()))

main_list = [x for x in range(1, lst1[0]+1)]

for _ in range(lst1[1]):
    line = list(map(int, input().split()))

    index1 = line[0]-1
    index2 = line[1]

    main_list[index1:index2] = main_list[index1:index2][::-1]

for x in main_list:
    print(x, end=" ")