def solution(n, arr1, arr2):
    answer = []
    dict = {'0' : ' ', '1' : '#'}

    temp = [bin(i | j)[2:] for i , j in zip(arr1, arr2)]

    for i in range(len(temp)) :
        if len(temp[i]) != n :
            temp[i] = '0'*(n - len(temp[i])) + temp[i]

    for i in temp :
        transtable = i.maketrans(dict)
        answer.append(i.translate(transtable))

    return answer

n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))