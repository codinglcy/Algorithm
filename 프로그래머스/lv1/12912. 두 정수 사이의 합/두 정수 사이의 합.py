def solution(a, b):
    answer = 0
    
    if a == b:
        return a
    
    if a < b:
        for i in range(a,b+1):
            answer = answer + i
    else:
        for j in range(b,a+1):
            answer = answer + j
    
    return answer