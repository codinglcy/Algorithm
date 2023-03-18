def solution(s):
    answer = ''
    temp = []
    
    for c in s:
        asciiC = ord(c)
        temp.append(asciiC)
    
    temp.sort(reverse=True)
    
    for i in temp:
        ic = chr(i)
        answer = answer + ic
    
    return answer