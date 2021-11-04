def solution(s):

    answer = sorted(s , reverse = -1)

    return ''.join(answer)

s = "Zbcdefg"

print(solution(s))