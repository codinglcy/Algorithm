def solution(n):
    answer = [0,1]
    
    for i in range(2,n+1):
        answer.append((answer[-1]+answer[-2])%1234567)
    
    return answer[-1]