def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    
    name = set(name)
    
    for pht in photo:
        temp = 0
        for nm in pht:
            if nm in name:
                temp = temp + dict[nm]
        answer.append(temp)
    
    return answer

# 이름을 키, 그리움점수를 값으로 가지는 딕셔너리 생성
# 반복문으로 각 사진의 인물들과 name을 비교해 name에 있으면 딕셔너리 값을 더한다
# 리스트보다 셋이 더 빠름 -> name에 있는지 비교하기 전 set으로 전환