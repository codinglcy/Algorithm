def solution(m, n, board):
    count = 0
    deleteTemp = set()
    
    while True:
        for j in range(m-1):
            for i in range(n-1):
                alpha = board[j][i]
                if alpha == '0':
                    continue
                right = board[j][i+1]
                down = board[j+1][i]
                downRight = board[j+1][i+1]
                if alpha == right and alpha == down and alpha == downRight:
                    deleteTemp.add((j,i))
                    deleteTemp.add((j,i+1))
                    deleteTemp.add((j+1,i))
                    deleteTemp.add((j+1,i+1))
                
        if len(deleteTemp) == 0:
            break
        deleteTemp = sorted(list(deleteTemp), key = lambda x: -x[0])

        while len(deleteTemp):
            (y,x) = deleteTemp.pop()
            count = count + 1
            for yy in range(y,0,-1):
                getAl = board[yy-1][x]
                if getAl == '0':
                    break
                board[yy] = board[yy][:x] + getAl + board[yy][x+1:]
                board[yy-1] = board[yy-1][:x] + '0' + board[yy-1][x+1:]
        deleteTemp = set(deleteTemp)
    
    return count

# 1. board[0][0]부터 board[-2][-2]까지 해당 위치 알파벳과 오른쪽,아래,오른쪽아래 위치 알파벳이 같은지 확인
# 2. 모두 같을 경우 제거할 알파벳 위치 셋(deleteTemp)에 해당 위치들 append
# 3. 한바퀴 돌고 난 후
# 3-1. deleteTemp의 길이가 0이면 count의 값 리턴
# 3-2. deleteTemp의 위치들에 위쪽 알파벳 채워넣고 count+1, deleteTemp pop() 작업, 빈칸은 0으로 채우기
# 1~3 반복