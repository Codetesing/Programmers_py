def solution(m, musicinfos):
    answer = []

    trans_musicinfo = []

    for music in musicinfos :
        temp = music.split(',')
        start_time = temp[0].split(':')
        end_time = temp[1].split(':')

        time = (int(end_time[0]) * 60 + int(end_time[1])) - (int(start_time[0]) * 60 + int(start_time[1]))

        temp.append(time)

        lens = 0

        for i in temp[3] :
            if i == '#' : lens = lens + 1

        while time > len(temp[3]) - lens:
            temp[3] = temp[3] * 2
            lens = lens * 2

        j = 0
        while j <= time :
            if len(temp[3]) == j :
                break

            if temp[3][j] == '#' :
                time = time + 1
            j = j + 1

        temp[3] = temp[3][:time]
        trans_musicinfo.append(temp)

    for music in trans_musicinfo :
        if m in music[3] :
            answer.append([music[2], music[4]])

    if len(answer) != 1 :
        answer = sorted(answer, key = lambda x : x[1])

    if len(answer) == 0 :
        return "(None)"

    return answer[0][0]

m = "CCB"
musicinfos = ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]

print(solution(m, musicinfos))