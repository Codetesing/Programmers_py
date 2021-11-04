def solution(num):
    answer = 0

    while(num != 1) :

        if answer == 500 :
            return -1

        div, mod = divmod(num, 2)

        if(mod == 0) :
            num = div

        else :
            num = num * 3 + 1

        answer += 1

    return answer

n = 626331
print(solution(n))