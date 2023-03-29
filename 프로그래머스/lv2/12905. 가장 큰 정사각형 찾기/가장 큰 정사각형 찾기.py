def solution(board):
    temp = set()
    
    if len(board) > 1 and len(board[0]) > 1:
        for y in range(1, len(board)):
            for x in range(1, len(board[0])):
                if board[y][x] == 1:
                    temp.add(1)
                    luNum = board[y-1][x-1]
                    lNum = board[y][x-1]
                    uNum = board[y-1][x]
                    if luNum > 0 and lNum > 0 and uNum > 0:
                        minNum = min(luNum,lNum,uNum)
                        board[y][x] = minNum + 1
                        temp.add(minNum+1)
        if len(temp) == 0:
            return 0
        return max(temp)**2
    else:
        for b in board:
            for d in b:
                temp.add(d)
        if 1 in temp:
            return 1
        return 0
    

# board의 길이와 board[0]의 길이가 모두 1 이상일 경우 (board[y][x])
#   - y range(1,len(board))
#       - x range(1,len(board[0]))
#           - luNum(위대각선), lNum(왼쪽), uNum(위) 숫자들이 모두 0이 아닐때
#               - luNum, lNum, uNum중 작은 숫자 + 1을 해당 칸의 값으로
#
# board의 길이가 1이거나 board[0]의 길이가 1일 경우
#   - 1이 존재하면 return 1
#   - 모두 0이면 return 0