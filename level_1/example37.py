def solution(s):
    p_num = 0
    y_num = 0

    s = s.lower()

    for i in s :
        if i == 'p' :
            p_num += 1

        elif i == 'y' :
            y_num += 1

    if p_num == y_num :
        return True

    else :
        return False

s = "pPoooyY"

print(solution(s))