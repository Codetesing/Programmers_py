def gcd(n, m) :
    if m == 0 :
        return n

    return gcd(m, n % m)

def lcm(n, m) :
    if n > m :
        return (n * m) // gcd(n, m)

    else :
        return (n * m) // gcd(m , n)

def solution(arr):
    answer = arr.pop()

    while len(arr) != 0 :
        n = arr.pop()
        answer = lcm(n, answer)

    return answer

arr = [2,6,8,14]

print(solution(arr))