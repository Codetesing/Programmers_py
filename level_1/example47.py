def solution(d, budget):
    answer = 0

    d.sort()

    for i in d :
        if budget >= i :
            budget -= i
            answer += 1

        else :
            break

    return answer

d = [1,3,2,5,4]
budget = 9

print(solution(d, budget))