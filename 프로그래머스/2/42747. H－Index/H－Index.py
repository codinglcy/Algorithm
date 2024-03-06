def solution(citations):
    sortCit = sorted(citations,reverse=True)
    
    if set(citations) == {0}:
        return 0
    
    if sortCit[-1] > len(sortCit):
        return len(sortCit)
    
    for h in range(len(sortCit)):
        if sortCit[h] >= h+1 and sortCit[h+1] <= h+1:
            return h+1
    
    
# n = len(citations)
# citations를 정렬했을때 뒤에서 h번째 숫자가 h이상이고, 뒤에서 h+1번째 숫자가 h이하인 경우
# 0만 있는 경우는 0