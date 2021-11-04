def solution(dirs):
    answer = 0
    visit = []
    cur = [0, 0]

    for pos in dirs :
        tok = 0
        next = [cur[0], cur[1]]

        if pos == 'U' :
            next[1] = cur[1] + 1
        elif pos == 'D' :
            next[1] = cur[1] - 1
        elif pos == 'R' :
            next[0] = cur[0] + 1
        elif pos == 'L' :
            next[0] = cur[0] - 1

        for temp in next :
            if temp > 5 or temp < -5 :
                tok = 1

        if tok == 0 :
            if [cur, next] not in visit :
                visit.append([[cur[0], cur[1]], [next[0], next[1]]])
                visit.append([[next[0], next[1]], [cur[0], cur[1]]])
                answer = answer + 1
            cur = next

    return answer

dirs = "ULURRDLLU"

print(solution(dirs))