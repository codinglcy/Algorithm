import math

def solution(n):
    answer = 1
    
    if n == 2:
        return answer
    
    for num in range(3, n+1):
        untilnum = int(math.sqrt(num+1))
        for nn in range(2, untilnum+1):
            if num % nn == 0:
                break
            if nn == untilnum:
                answer = answer + 1
                
    
    return answer