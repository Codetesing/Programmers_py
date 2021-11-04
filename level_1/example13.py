a, b = map(int, input().strip().split(' '))

for i in range(b) :
    tmp = '*'
    for j in range(a-1) :
        tmp += '*'
    print(tmp)