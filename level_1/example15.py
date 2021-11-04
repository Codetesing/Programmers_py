def solution(x, n) :
    answer = []

    for i in range(1, n + 1) :
        answer.append(x * i)

    return answer

x = -4
n = 2

print(solution(x, n))