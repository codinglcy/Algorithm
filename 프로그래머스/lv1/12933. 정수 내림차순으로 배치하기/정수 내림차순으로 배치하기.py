def solution(n):
    answer = ''
    temp = []
    
    for num in str(n):
        temp.append(int(num))
    temp.sort(reverse=True)
    
    for i in temp:
        answer = answer + str(i)
    
    return int(answer)