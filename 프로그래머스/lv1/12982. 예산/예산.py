def solution(d, budget):
    temp = 0
    
    d.sort()
    
    for i in range(len(d)):
        temp = temp + d[i]
        
        if i < len(d) and temp > budget:
            return i

    return len(d)
