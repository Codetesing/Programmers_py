import itertools

def is_Prime(num) :
    i = 2

    if num == 2 :
        return True
    elif num == 3 :
        return True

    else :
        if num % i == 0 :
            return False

        else :
            i = 3

            while(i * i <= num) :
                if num % i == 0 :
                    return False
                i += 2
            return True

def solution(nums):
    answer = 0

    tmp = itertools.combinations(nums, 3)

    for i in tmp :
         if is_Prime(sum(i)) :
            answer += 1

    return answer

nums = [1,2,7,6,4]
print(solution(nums))