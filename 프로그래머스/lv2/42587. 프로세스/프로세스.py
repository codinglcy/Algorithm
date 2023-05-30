def solution(priorities, location):
    dic = {}
    dicList = []
    process = list(range(0,len(priorities)))
    count = 0
    
    for pri in priorities:
        if pri not in dic:
            dic[pri] = 1
        else:
            dic[pri] = dic[pri] + 1
    dic = dict(sorted(dic.items(), reverse=True))
    dicList = list(dic.keys())
    
    while len(process)>0:
        nowProcess = process.pop(0)
        nowPriority = priorities.pop(0)
        if nowPriority == dicList[0]:
            count = count + 1
            if location == nowProcess:
                return count
            dic[nowPriority] = dic[nowPriority] - 1
            if dic[nowPriority] == 0:
                dic.pop(nowPriority)
                dicList = list(dic.keys())
        else:
            priorities.append(nowPriority)
            process.append(nowProcess)
    
# priorities의 숫자들을 키로 하는 딕셔너리 dic 생성, 각 키의 개수 세기
# dic의 키값 리스트 dicList
#
# 프로세스는 초기 priorities의 인덱스로 한다.
# 
# while True:
#   프로세스 pop
#   해당 프로세스에 해당하는 우선순위 pop
#   꺼낸 우선순위가 dicList[0]와 같으면:
#       해당 프로세스 끝
#       dic개수 줄이기
#       dic[popPri]가 0일 경우:
#           dic.pop(popPri)
#           dicList = dic.keys()
#   꺼낸 우선순위가 dicList[0]이 아니면:
#       pop한 것들 다시 append