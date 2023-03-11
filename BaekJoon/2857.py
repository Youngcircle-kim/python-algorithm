names = []

for _ in range(5):
    names.append(input())

n = 0
for i in range(len(names)):
    if 'FBI' in names[i]:
        print(i+1, end=' ')
        n = 1
if n ==0:
    print('HE GOT AWAY!')