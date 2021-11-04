def solution(arr):
    answer = []
    temp = 0

    answer.append(arr[0])

    for i in arr :
        if answer[temp] != i :
            answer.append(i)
            temp += 1

    return answer

arr = [1,1,3,3,0,1,1]

print(solution(arr))