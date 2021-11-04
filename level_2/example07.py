def Seq(i, n) :
    temp = 0

    for j in range(i, n + 1) :
        temp += j
        if temp == n :
            return True
        elif temp > n :
            return False

def solution(n):
    answer = 0

    for i in range(1, n + 1) :
        if Seq(i, n) :
            answer += 1

    return answer

n = 15

print(solution(n))