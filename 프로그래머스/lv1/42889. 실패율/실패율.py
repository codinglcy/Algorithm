def solution(N, stages):
    answer = []
    dicN = {}
    playNum = len(stages)
    
    for n in range(1, N+2):
        dicN[n] = 0
    
    for stage in stages:
        dicN[stage] = dicN[stage] + 1
        
    
    for n in range(1,len(dicN)+1):
        if dicN[n] != 0:
            failNum = dicN[n]
            dicN[n] = failNum / playNum
            playNum = playNum - failNum
        if n == len(dicN):
            del dicN[n]
    
    dicN = sorted(dicN.items(), key = lambda item: item[1], reverse = True)
    
    for nn in dicN:
        answer.append(nn[0])
    
    return answer

# 1부터 N+1까지의 키를 가진 딕셔너리 dicN 생성
# stages에 든 원소들 개수를 dicN에 입력
#
# dicN을 이용해 실패율 구하기 - 1스테이지부터 구해서 dicN 각 스테이지 값 변경
# 실패율이 큰 순, 같으면 스테이지 순