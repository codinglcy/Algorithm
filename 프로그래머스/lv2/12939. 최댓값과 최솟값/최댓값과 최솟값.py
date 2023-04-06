def solution(s):
    answer = ''
    sList = list(map(int,s.split(" ")))
    
    answer = str(min(sList)) + " " + str(max(sList))
    
    return answer