k = input()

pan = ['AAAA', 'BB']
board = k.replace('XXXX', pan[0])
board = board.replace('XX', pan[1])

if 'X' in board:
    print(-1)
else:
    print(board)