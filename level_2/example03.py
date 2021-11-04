def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)) :
        temp = []
        for j in range(len(arr2[0])) :
            temp2 = 0
            for k in range(len(arr1[0])) :
                temp2 += arr1[i][k] * arr2[k][j]
            temp.append(temp2)

        answer.append(temp)

    return answer

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))