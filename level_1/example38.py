def solution(strings, n):
    answer = []
    temp = {}

    for i in strings :
        temp[i] = i[n]

    temp = sorted(temp.items())

    temp.sort(key = lambda x:x[1])

    for i in temp :
        answer.append(i[0])

    return answer

strings = ["abce", "abcd", "cdx"]
n = 2

print(solution(strings, n))