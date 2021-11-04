def solution(x):
    answer = True
    tmp = x
    tmp2 = 0
    tmp3 = 0

    while tmp != 0 :
        tmp, tmp2 = divmod(tmp, 10)
        tmp3 = tmp3 + tmp2

    if (x % tmp3) == 0 :
        answer = True

    else :
        answer = False

    return answer

x = 10

print(solution(x))