def is_Prime(n) :
    for i in range(3, n + 1, 2) :
        if i * i > n :
            break
        else :
            if n % i == 0 :
                return False

    return True

def solution(n):

    if n <= 2 :
        answer = n - 1

    else :
        answer = 1
        for i in range(3, n + 1, 2) :
            if is_Prime(i) :
                answer += 1

    return answer

n = 10

print(solution(n))