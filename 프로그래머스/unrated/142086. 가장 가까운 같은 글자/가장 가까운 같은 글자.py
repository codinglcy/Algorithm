def solution(s):
    answer = []
    sList = list(s)
    
    for i in range(len(sList)):
        char = sList[i]
        tempList = sList[:i]
        sSet = set(tempList)
        count = 0
        
        if char in sSet:
            for j in range(len(tempList)-1,-1,-1):
                count = count + 1
                if char == tempList[j]:
                    answer.append(count)
                    break
        else:
            answer.append(-1)
                
    return answer
    
    
#재귀함수? 반복문?
#count 변수
#우선 리스트를 처음부터 해당 번째까지 slice, set으로 변환, in으로 있는지 확인