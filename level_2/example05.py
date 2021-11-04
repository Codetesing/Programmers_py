def solution(A,B):
    answer = 0

    start_a = 0
    start_b = 0
    len_a = len(A) - 1
    len_b = len(B) - 1

    A.sort(reverse=-1)
    B.sort(reverse = -1)

    for i in range(len(A)) :
        m_a = A[start_a]
        m_b = B[start_b]

        if m_a > m_b :
            m_b = B[len_b]
            start_a += 1
            len_b -= 1
        else :
            m_a = A[len_a]
            start_b += 1
            len_a -= 1

        answer += (m_a * m_b)

    return answer

A = [1, 4, 2]
B = [5, 4, 4]

print(solution(A, B))