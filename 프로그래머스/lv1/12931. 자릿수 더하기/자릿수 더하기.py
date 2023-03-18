def solution(n):
    answer = 0
    strn = str(n)
    
    for nn in strn:
        answer = answer + int(nn)

    return answer