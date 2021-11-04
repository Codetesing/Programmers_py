def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)) :
        answer.append([x + y for x, y in zip(arr1[i], arr2[i])])

    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution(arr1, arr2))