def solution(n):
    temp = [0]*n
    
    def queen(y, temp):
        if y == n:
            return 1
        
        answer = 0
        for x in range(n):
            if can(y, x, temp):
                temp[y] = x
                answer = answer + queen(y+1, temp)
                
        return answer
        
        
    def can(y, x, temp):
        for i in range(y):
            if x == temp[i] or abs(temp[i]-x) == abs(y-i):
                return False
        return True
    
    
    return queen(0, temp)

# <설명 참고 생각 정리>
# 어차피 한 줄(가로)에 한 퀸만 놓을 수 있으니 1차원 배열 사용 temp[x,x,x,x..]
# 배열에는 0부터 n-1까지의 숫자가 하나씩만 들어갈 수 있다(세로줄에도 한 퀸만 가능)
# 각 인덱스끼리의 차와 값끼리의 차가 같으면 안된다(대각선상에도 하나만 가능하다)