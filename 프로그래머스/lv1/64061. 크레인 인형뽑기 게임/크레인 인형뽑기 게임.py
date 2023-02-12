def solution(board, moves):
    answer = 0
    temp = []
    
    for move in moves:
        pickLine = move - 1
        
        if board[-1][pickLine] == 0:
            continue
            
        for line in range(len(board)):
            if board[line][pickLine] == 0:
                continue
            else:
                if len(temp) == 0:
                    temp.append(board[line][pickLine])
                    
                elif temp[-1] == board[line][pickLine]:
                    answer = answer + 2
                    temp.pop()
                else:
                    temp.append(board[line][pickLine])
                    
                board[line][pickLine] = 0
                break
    
    return answer

# moves로 for문
# 그 안에 board 길이로 for문
#   - board의 마지막 원소의 moves에 해당하는 부분이 0이면 탈출
#       아니면 첫번째부터 차례로 0이 아닌 수가 나올때까지
#           0이 아닌 수가 나오면 그걸 뽑아 temp[]에 담는다
#           temp의 마지막 원소가 뽑은 수와 같으면 둘다 사라지고 answer+2