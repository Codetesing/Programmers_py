import math

def solution(n):

    up = math.ceil(math.sqrt(n))
    down = math.floor(math.sqrt(n))

    if up == down :
        answer = pow(up + 1, 2)

    else :
        answer = -1

    return answer

n = 121

print(solution(n))