s = input()
sss = 'abcdefghijklmnopqrstuvwxyz'
for ss in sss:
    try:
        print(s.index(ss), end=" ")
    except:
        print(-1, end=" ")
