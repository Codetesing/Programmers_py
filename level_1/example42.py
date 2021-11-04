def score(n, tok) :

    if type(n) != int :
        return 0

    if tok == 'S' :
        return n

    elif tok == 'D' :
        return n * n

    elif tok == 'T' :
        return n * n * n


def solution(dartResult):
    answer = 0
    temp = []
    temp2 = ''
    temp3 = []

    for i in dartResult :
        if ord(i) >= 48 and ord(i) <= 57 :
            temp2 += i

        else :
            if temp2 != '' :
                temp.append(int(temp2))

            temp.append(i)
            temp2 = ''

    i = 0
    while(i < len(temp)) :

        if i + 2 < len(temp) :
            if type(temp[i + 2]) != int :
                if temp[i + 2] == '*' :
                    temp3.append(score(temp[i], temp[i + 1]))

                else :
                    temp3.append(score(temp[i], temp[i + 1]))

                temp3.append(temp[i + 2])
                i += 1

            else :
                temp3.append(score(temp[i], temp[i + 1]))

        else:
            temp3.append(score(temp[i], temp[i + 1]))

        i += 2

    i = 0
    while (i < len(temp3)):

        if i + 1 < len(temp3):
            if type(temp3[i + 1]) != int:
                if temp3[i + 1] == '*':
                    if i != 0 :
                        if type(temp3[i - 1]) != int :
                            temp3[i - 2] *= 2

                        else :
                            temp3[i - 1] *= 2

                    temp3[i] *= 2

                else:
                    temp3[i] *= -1

                i += 1

        i += 1

    for i in temp3 :
        if type(i) == int:
            answer += i

    return answer

dartResult = "1T2D3D#"

print(solution(dartResult))