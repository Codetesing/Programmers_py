def solution(board):
    answer = 0

    for row in range(1, len(board)) :
        for col in range(1, len(board[0])) :
            if board[row][col] >= 1 :
                board[row][col] += min(board[row - 1][col - 1],board[row][col - 1],board[row - 1][col])

    for i in board :
        if answer < max(i) : answer = max(i)

    return answer * answer

board = [[1, 0], [0, 0]]

print(solution(board))