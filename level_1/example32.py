def solution(n):
    answer = ''

    for i in range(n) :
        answer += "수박"

    answer = answer[:len(answer)//2]

    return answer

n = 4

print(solution(n))