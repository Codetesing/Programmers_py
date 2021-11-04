def solution(board, moves):
    answer = 0
    buk = []
    tmp = -1

    for i in moves :
        for j in range(len(board)) :
            if(board[j][i - 1] != 0) :
                if(tmp == -1) :
                    buk.append(board[j][i - 1])
                    tmp = tmp + 1
                else :
                    if(buk[tmp] == board[j][i - 1]) :
                        del buk[tmp]
                        answer = answer + 2
                        tmp = tmp - 1
                    else :
                        buk.append(board[j][i - 1])
                        tmp = tmp + 1

                board[j][i - 1] = 0
                break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))