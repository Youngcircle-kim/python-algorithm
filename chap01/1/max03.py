# 세 정수를 입력받아 최댓값 구하기

print('세 정수의 최댓값을 구합시다.')

a = int(input('정수 a의 값을 입력하세요. '))
b = int(input('정수 b의 값을 입력하세요. '))
c = int(input('정수 c의 값을 입력하세요. '))

maximum = a # 파이썬은 타입 지정 굳이 안해도 된다.

if b > maximum:
    maximum = b

if c > maximum:
    maximum = c

print(f'최댓값은 {maximum}입니다.')