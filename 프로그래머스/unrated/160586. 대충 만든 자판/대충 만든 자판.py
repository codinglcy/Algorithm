def solution(keymap, targets):
    answer = []
    keyDic = {}
    
    for i in keymap:
        for j in range(len(i)):
            al = i[j]
            if keyDic.get(al) == None:
                keyDic[al] = j
            else:
                if keyDic[al] > j:
                    keyDic[al] = j
    
    for i in targets:
        count = 0
        for al in i:
            if keyDic.get(al) == None:
                count = -1
                break
            else:
                count = count + keyDic[al]+1
        answer.append(count)
    
    return answer

# keymap을 이용해 딕셔너리에 각 알파벳을 입력하기 위한 누르는 횟수의 최솟값 저장
# targets에 있으나 딕셔너리 키에 없는 알파벳이 나오면 그 인덱스의 값은 -1