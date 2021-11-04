def solution(seoul):
    answer = ''

    ind = str(seoul.index("Kim"))

    answer = "김서방은 " + ind + "에 있다"

    return answer

seoul = ["Jane", "Kim"]

print(solution(seoul))