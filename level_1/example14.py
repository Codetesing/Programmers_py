def solution(N, stages):
    answer = [0 for i in range(N + 1)]
    add = [0 for i in range(N + 1)]
    temp = []

    for i in stages :
        answer[i - 1] += 1

    add[N] = answer[N]

    for i in range(N - 1, -1, -1) :
        add[i] = answer[i] + add[i + 1]

    for i in range(len(answer)) :
        if add[i] != 0:
            answer[i] = answer[i] / add[i]

    answer.pop()

    for i in range(len(answer)) :
        temp.append(answer.index(max(answer)) + 1)
        answer[answer.index(max(answer))] = -1

    return temp

N = 4
stages = [4,4,4,4,4]

print(solution(N, stages))