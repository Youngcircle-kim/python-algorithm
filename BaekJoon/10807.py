n = int(input())

input_num = input()

list = [int(num_str) for num_str in input_num.split()]

count = 0

num = int(input())

for i in range(len(list)):
    if list[i] == num:
        count += 1

print(count)