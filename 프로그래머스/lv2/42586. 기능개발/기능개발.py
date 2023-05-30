def solution(progresses, speeds):
    answer = []
    temp = []
    
    for idx in range(len(progresses)):
        leftProgre = 100 - progresses[idx]
        leftDay = leftProgre // speeds[idx]
        if leftProgre % speeds[idx] > 0:
            leftDay = leftDay + 1
        progresses[idx] = leftDay
        
    while len(progresses) > 0:
        if len(temp) == 0:
            popPro = progresses.pop(0)
            temp.append(popPro)
        else:
            if temp[0] >= progresses[0]:
                popPro = progresses.pop(0)
                temp.append(popPro)
            else:
                answer.append(len(temp))
                temp = []
    answer.append(len(temp))
                
    return answer

# 각각 작업이 끝나기까지 남은 일수를 구한다
#
#
# temp에 하나씩 담기 (temp[0]보다 progresses가 클 때까지)
#   temp개수 answer에 저장 후 temp 비우기
#
# 반복