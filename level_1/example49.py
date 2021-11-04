def solution(left, right):

    answer = sum([i for i in range(left, right + 1)])

    if answer != 1 :
        for i in range(1, 33) :
            if i * i <= right :
                if i * i >= left :
                    answer -= 2 * i * i
            else :
                break
    else :
        answer = 0

    return answer

left = 1
right = 1

print(solution(left, right))