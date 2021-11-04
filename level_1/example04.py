def solution(nums):
    answer = 0

    tmp = len(nums) / 2

    nums = list(set(nums))
    nums = len(nums)


    if(tmp < nums) :
        answer = int(tmp)

    else :
        answer = nums

    return answer

num = [3, 1, 2, 3]

print(solution(num))