def solution(n, lost, reserve):
    answer = n

    tmp = set(lost) & set(reserve)
    tmp = list(tmp)

    for i in range(len(tmp)) :
        reserve.remove(tmp[i])
        lost.remove(tmp[i])

    for i in range(len(lost)) :

        if lost[i] - 1 in reserve :
            reserve.remove(lost[i] - 1)

        elif lost[i] + 1 in reserve :
            reserve.remove(lost[i] + 1)

        else :
            answer = answer - 1

    return answer

n = 5
lost = [1, 2, 3]
reserve = [2, 3, 4]

print(solution(n, lost, reserve))