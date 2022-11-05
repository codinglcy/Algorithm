def solution(food):
    answer = ''
    temp = []
    
    for i in range(1,len(food)):
        for count in range(food[i]//2):
            temp.append(str(i))
    
    for num in temp:
        answer += num
    answer += '0'
    for num in temp[::-1]:
        answer += num
    
    return answer