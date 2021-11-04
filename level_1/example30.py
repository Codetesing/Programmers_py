def solution(s, n):
    answer = ''

    for i in s :
        if i != ' ' :
            temp = ord(i)

            if temp <= 90 :
                i = chr(((ord(i) + n - 65) % 26) + 65)
            else :
                i = chr(((ord(i) + n - 97) % 26) + 97)

        answer += i

    return answer

s = "a B z"
n = 4

print(solution(s, n))