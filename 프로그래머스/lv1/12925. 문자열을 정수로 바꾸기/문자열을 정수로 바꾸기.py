def solution(s):
    answer = 0
    temp = ''
    
    if s[0] == '+':
        temp = s[1:]
    else:
        temp = s
    
    answer = int(temp)
    
    return answer