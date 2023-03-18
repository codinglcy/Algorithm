def solution(s):
    answer = ''
    idx = 0
    
    for c in s:
        if c == ' ':
            idx = 0
            answer = answer + c
        else:
            if (idx+1) % 2 == 0:
                answer = answer + c.lower()
            else:
                answer = answer + c.upper()
            idx = idx + 1

    return answer