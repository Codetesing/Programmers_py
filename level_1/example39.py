def solution(a, b):

    return sum([i for i in range(min(a, b), max(a, b) + 1)])

a = 5
b = 3

print(solution(a, b))