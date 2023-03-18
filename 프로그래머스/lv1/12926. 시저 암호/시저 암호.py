def solution(s, n):
    answer = ''
    
    for c in s:
        ordc = ord(c)
        if c == ' ':
            answer = answer + c
        elif ordc >= 65 and ordc <= 90:
            if (ordc + n) > 90:
                temp = 65 + (ordc+n-91)
                answer = answer + chr(temp)
            else:
                answer = answer + chr(ordc+n)
        else:
            if (ordc + n) > 122:
                temp = 97 + (ordc+n-123)
                answer = answer + chr(temp)
            else:
                answer = answer + chr(ordc+n)
    
    return answer

# 'A': 65 'Z': 90 'a': 97 'z': 122