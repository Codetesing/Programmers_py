def solution(lottos, win_nums) :

    answer = []

    num_same = set(lottos) & set(win_nums)
    num_same = len(num_same)
    num_0 = lottos.count(0)

    answer.append(num_same + num_0)
    answer.append(num_same)

    for i in range(len(answer)):
        if answer[i] == 0 :
            answer[i] = 6

        else:
            answer[i] = 7 - answer[i]


    return answer

#Lottos = [44, 1, 0, 0, 31, 25]
#Lottos = [0, 0, 0, 0, 0, 0]
Lottos = [45, 4, 35, 20, 3, 9]

#Win_nums = [31, 10, 45, 1, 6, 19]
#Win_nums = [38, 19, 20, 40, 15, 25]
Win_nums = [20, 9, 3, 45, 4, 35]

print(solution(Lottos, Win_nums))