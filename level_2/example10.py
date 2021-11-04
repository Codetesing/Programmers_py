def n_bin(n, base) :
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return n_bin(q, base) + T[r] if q else T[r]


def solution(n, t, m, p):
    answer = ''
    num = 0
    turn = 0

    while len(answer) < t :
        bin_num = n_bin(num, n)

        for i in bin_num :
            turn += 1
            if turn == p :
                answer += i

            if turn == m :
                turn = 0

        num += 1

    return answer[:t]

n = 2
t = 4
m = 2
p = 1

print(solution(n, t, m, p))