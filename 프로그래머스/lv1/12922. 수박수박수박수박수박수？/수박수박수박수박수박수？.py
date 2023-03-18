def solution(n):
    answer = ''
    dic = {1:'수', 2:'수박'}
    
    answer = dic[2]*(n//2) + dic[1]*(n%2)
    
    return answer