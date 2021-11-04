def SAME_NUM_1(n) :
    temp = bin(n)[2:]

    return temp.count('1')


def solution(n):
    answer = 0

    temp = bin(n)[2:]

    num_1 = temp.count('1')

    for i in  range(n + 1, 10000001, 1) :
        if num_1 == SAME_NUM_1(i) :
            answer = i
            break

    return answer

n = 78

print(solution(n))