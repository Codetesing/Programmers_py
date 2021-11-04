def solution(s):

    if len(s) == 4 or len(s) == 6:
        for i in s :
            if ord(i) < 48 or ord(i) > 57 :
                return False

        return True

    else :
        return False

s = "0123456789"

print(solution(s))