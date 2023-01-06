def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        tMini = int(t[i:i+len(p)])
        if tMini <= int(p):
            answer = answer + 1
    
    return answer