def solution(numbers):
    answer = 0

    temp = [i for i in range(10)]

    for i in temp :
        if i not in numbers :
            answer += i

    return answer

numbers = [1,2,3,4,6,7,8,0]

print(solution(numbers))