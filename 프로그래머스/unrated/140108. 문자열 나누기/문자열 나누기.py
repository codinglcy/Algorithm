def solution(s):
    answer = 0
    sList = list(s)
    index = 0
    
    while index < len(sList):
        xCount = 1
        notxCount = 0
        listSlice = sList[index:]
        
        for i in range(len(listSlice)):
            index = index + 1
            
            if index == len(sList):
                answer = answer + 1
                break
                        
            if i == 0:
                continue
            
            if listSlice[i] == listSlice[0]:
                xCount = xCount + 1
            else:
                notxCount = notxCount + 1
            
            if xCount == notxCount:
                answer = answer + 1
                break

    return answer

# 문자열 리스트화
# while문+for문 - 리스트에 있는 것 차례로, 셋 사용, 분리되는 순간 answer+1