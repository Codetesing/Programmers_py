import string

def solution(msg):
    answer = []
    dic = list(string.ascii_uppercase)

    while True :
        i = 0
        temp = msg[i]

        if msg in dic :
            answer.append(dic.index(msg) + 1)
            break

        while temp in dic:
            i = i + 1
            temp = temp + msg[i]

        dic.append(temp)
        answer.append(dic.index(temp[:-1]) + 1)
        msg = msg[len(temp) - 1:]

    return answer

msg = "TOBEORNOTTOBEORTOBEORNOT"

print(solution(msg))