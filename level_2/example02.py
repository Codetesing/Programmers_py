def solution(s):
    answer = ''

    for i in range(len(s)) :

        if i == 0 :
            answer += s[i].upper()

        else :
            if s[i].isupper() :
                if s[i - 1] != ' ' :
                    answer += s[i].lower()
                else :
                    answer += s[i]
            else :
                if s[i - 1] == ' ':
                    answer += s[i].upper()
                else:
                    answer += s[i]

    return answer

s = "3people unFollowed me"

print(solution(s))