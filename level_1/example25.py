def solution(n):
    answer = ''

    temp = list(map(int, str(n)))

    temp.sort(reverse = True)

    for i in temp :
        answer += str(i)

    answer = int(answer)

    return answer

n = 118372

print(solution(n))