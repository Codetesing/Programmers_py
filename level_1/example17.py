def solution(phone_number):
    temp = []
    temp2 = []

    for i in range(len(phone_number) - 4) :
        temp.append("*")

    for i in range(len(phone_number) - 4, len(phone_number)) :
        temp2.append(phone_number[i])

    temp = temp + temp2

    answer = ''.join(temp)

    return answer

phone_number = "01033334444"

print(solution(phone_number))