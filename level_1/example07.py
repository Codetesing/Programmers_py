def solution(answers):
    answer = []
    tmp = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i in range(len(tmp)) :
        len_tmp = len(tmp[i])
        k = 0
        key = 0

        for j in range(len(answers)) :
            if(tmp[i][k] == answers[j]) :
                key = key + 1
            k = int((k + 1) % len_tmp)
        answer.append(key)

    max_ans = max(answer)

    return [i + 1 for i, j in enumerate(answer) if j == max_ans]

answer = [1, 2, 3, 4, 5]
print(solution(answer))