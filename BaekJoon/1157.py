str = input().upper()
unique = list(set(str))

cntLst = []
for s in unique:
    cnt = str.count(s)
    cntLst.append(cnt)

if cntLst.count(max(cntLst)) > 1:
    print('?')
else:
    print(unique[cntLst.index(max(cntLst))])
