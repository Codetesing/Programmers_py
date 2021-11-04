def solution(s):
    answer = ''
    temp = 0

    for i in range(len(s)):
        if s[i] == ' ' :
            temp = 0
            answer += s[i]
        else :
            if temp % 2 == 0 :
                answer += s[i].upper()
            else :
                answer += s[i].lower()
            temp += 1

    return answer

s = "ab ab ab ab"

print(solution(s))