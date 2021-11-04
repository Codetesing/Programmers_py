def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for i in new_id :
        if ((ord(i) >= 97) and (ord(i) <= 122)) or ((ord(i) >= 48) and (ord(i) <= 57)) or (i == '.') or (i == '_') or (i == '-'):
           answer = answer + i

    while(answer.find("..") != -1) :
        answer = answer.replace("...", ".")
        answer = answer.replace("..", ".")

    if answer[0] == '.' :
        answer = answer[1:]

        if len(answer) != 0 :
            if answer[len(answer) - 1] == '.':
                answer = answer[:-1]

    if len(answer) == 0 :
        answer = 'a'

    else:
        if len(answer) > 15 :
            answer = answer[:15]
        if answer[len(answer) - 1] == '.':
            answer = answer[:-1]

    if len(answer) <= 2 :
        add = answer[len(answer) - 1]
        while(len(answer) != 3) :
            answer = answer + add

    return answer

new_id = "......................"
print(solution(new_id))