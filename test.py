input_str = input("Input string: ")

start = -1
end = -1
i = 0
cnt = len(input_str)

#영어만 거르기 때문에 알파벳만 모음
s = "abcdefghijklmnopqrstuvwxyz"

while i< cnt:
    if start < 0 and not (input_str.lower()[i] in s):
        start = i+1

    #start가 이미 양수로 적용이 된 후, 영어가 처음 나올 때를 조건으로 제시
    if start > 0 and input_str.lower()[i] in s:
        end = i

        #end까지 구했으니 더 이상 돌리는건 불필요하기 때문에 break
        break
    i += 1

print(input_str[start:end])