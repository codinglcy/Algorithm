def solution(s):
    answer = ''
    sList = s.split(" ")
    
    for i in range(len(sList)):
        sList[i] = sList[i].capitalize()
        if i == len(sList)-1:
            answer = answer + sList[i]
        else:
            answer = answer + sList[i] + " "
    
    return answer