def solution(n):
    answer = 0

    for i in range(1, n + 1) :

        if i * i > n :
            break

        elif i * i == n:
            answer += i
        else :
            if n % i == 0 :
                answer += i
                answer += n // i

    return answer

n = 1

print(solution(n))