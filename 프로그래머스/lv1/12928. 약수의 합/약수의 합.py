import math

def solution(n):
    answer = 1 + n
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    for num in range(2, int(math.sqrt(n))+1):
        if n % num == 0:
            temp = n // num
            if temp == num:
                answer = answer + num
            else:
                answer = answer + temp + num
    
    return answer