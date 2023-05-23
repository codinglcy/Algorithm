def solution(clothes):
    dic = {}
    answer = 1
    
    for cloth,Ctype in clothes:
        if Ctype in dic:
            dic[Ctype] = dic[Ctype] + 1
        else:
            dic[Ctype] = 1
    
    for count in dic.values():
        answer = answer * (count+1)
    
    return answer-1

# 각 리스트의 1번째 인덱스의 값을 키로 하는 딕셔너리 값 저장, 벨류는 해당 종류 의상개수
# ((각 개수+1)**len(딕셔너리))-1 값 리턴
# -1은 모두 안입을 경우 제외하기 위해