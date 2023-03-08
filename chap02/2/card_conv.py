def card_conv(x: int, r: int) -> str:
    """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

    d = ''
    dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x > 0:
        d += dchar[x % r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    print('10진수를 n진수로 변환합니다.')
    print('End를 입력하시면 프로그램이 종료됩니다.')

    while True:
        x = input('원하는 정수를 입력해주세요.: ')
        if x == 'End':
            break

        n = int(input('n값을 입력해주세요.: '))
        print(card_conv(int(x), n))


