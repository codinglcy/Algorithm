def solution(n):
    answer = 0
    num = 1
    first = 1
    
    while first <= n:
        
        if (n-first)%num == 0:
            answer = answer + 1
        
        num = num + 1
        first = first + num
    
    return answer

# 두개씩 묶었을때: 3 5 7 9 11 13 15 ...
# 세개씩 묶었을때: 6 9 12 15 18 21 ...
# 네개씩 묶었을때: 10 14 18 22 26 30 ...
# 다섯씩 묶었을때: 15 20 25 30 35 ...