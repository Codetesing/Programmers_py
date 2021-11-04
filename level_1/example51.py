def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    left_h = '*'
    right_h = '#'

    for i in numbers :
        if i in left :
            answer += 'L'
            left_h = i
        elif i in right :
            answer += 'R'
            right_h = i
        else :
            for temp in phone :
                if i in temp :
                    temp_list = [[phone.index(temp), temp.index(i)]]
                    break
            for temp in phone :
                if left_h in temp :
                    temp_list += [[phone.index(temp), temp.index(left_h)]]
                    break
            for temp in phone :
                if right_h in temp :
                    temp_list += [[phone.index(temp), temp.index(right_h)]]
                    break
            temp1 = abs(temp_list[0][0] - temp_list[1][0]) + abs(temp_list[0][1] - temp_list[1][1])
            temp2 = abs(temp_list[0][0] - temp_list[2][0]) + abs(temp_list[0][1] - temp_list[2][1])

            if temp1 > temp2 :
                answer += 'R'
                right_h = i

            elif temp1 < temp2 :
                answer += 'L'
                left_h = i

            else :
                if hand == 'right' :
                    answer += 'R'
                    right_h = i
                else :
                    answer += 'L'
                    left_h = i

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))