def solution(n):
    temp = ''

    while n != 0:
        div, mod = divmod(n, 3)

        temp += str(mod)
        n = div

    return int(temp, 3)

n = 125

print(solution(n))