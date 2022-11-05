def solution(number):
    answer = 0
    
    for first in range(len(number)):
        for second in range(first+1,len(number)):
            for third in range(second+1,len(number)):
                if number[first]+number[second]+number[third] == 0:
                    answer += 1
    
    return answer