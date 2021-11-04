def solution(s):
    temp2 = []

    temp = s.split()

    for i in temp :
        temp2.append(int(i))

    answer = str(min(temp2)) + ' ' + str(max(temp2))

    return answer

s = "1 2 3 4"

print(solution(s))