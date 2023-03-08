input_list = list(map(int, input().split()))

lsts = [0] * input_list[0]

for _ in range(input_list[1]):

    line = list(map(int, input().split()))
    for i in range(line[0]-1, line[1]):
        lsts[i] = line[2]

for lst in lsts:
    print(lst,  end=" ")
