def solution(n):
    answer = [0, 1]

    if n < 2 :
        return answer[n]

    for i in range(2, n + 1) :
        answer.append((answer[i - 2] + answer[i - 1]) % 1234567)

    return answer[n]

n = 100000

print(solution(n))