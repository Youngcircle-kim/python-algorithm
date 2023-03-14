import sys

str = sys.stdin.readline().upper()
unique = list(set(str))

cntLst = []
for s in unique:
    cnt = str.count(s)
    cntLst.append(cnt)

if cntLst.count(max(cntLst)) > 1:
    print('?')
else:
    max_index = cntLst.index(max(cntLst))
    print(unique[max_index])
