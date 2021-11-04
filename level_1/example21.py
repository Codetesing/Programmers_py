import math

def solution(n, m):
    answer = []

    answer.append(math.gcd(n, m))
    answer.append(int((n * m) / answer[0]))

    return answer

n = 3
m = 12

print(solution(n, m))