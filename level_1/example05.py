def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i] :
            return participant[i]

    return participant[len(completion)]

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

# 모범 정답 ----- (내장함수 사용)
#import collections
#def solution(participant, completion):
#   answer = collections.Counter(participant) - collections.Counter(completion)
#    return list(answer.keys())[0]