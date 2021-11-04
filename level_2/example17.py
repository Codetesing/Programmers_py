def solution(skill, skill_trees):
    answer = 0

    for temp in skill_trees :
        is_sorted = []
        for skil in temp :
            index = skill.find(skil)

            if index != -1 :
                is_sorted.append(index)

        if len(is_sorted) == 0 :
            answer = answer + 1

        elif len(is_sorted) == 1 :
            if is_sorted[0] == 0:
                answer = answer + 1

        else :
            if is_sorted[0] == 0 and all(is_sorted[i] == is_sorted[i + 1] - 1 for i in range(len(is_sorted) - 1)) :
                answer = answer + 1

    return answer

skill = "CBD"
skill_trees = ["C", "D", "CB", "BDA"]

print(solution(skill, skill_trees))