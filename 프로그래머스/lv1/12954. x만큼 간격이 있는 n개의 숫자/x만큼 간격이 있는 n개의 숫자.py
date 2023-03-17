def solution(x, n):
    answer = []
    xEnd = 0
    temp = x
    
    if x == 0:
        return [0]*n
    
    for cnt in range(n):
        answer.append(temp)
        temp = temp + x
    
    return answer