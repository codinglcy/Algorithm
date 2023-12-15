def solution(board, h, w):
    answer = 0
    color = board[h][w]
    
    if h > 0: #상
        if board[h-1][w] == color:
            answer = answer + 1
            
    if w > 0: #좌
        if board[h][w-1] == color:
            answer = answer + 1
            
    if h < len(board)-1: #하
        if board[h+1][w] == color:
            answer = answer + 1
            
    if w < len(board[0])-1: #우
        if board[h][w+1] == color:
            answer = answer + 1
    
    return answer