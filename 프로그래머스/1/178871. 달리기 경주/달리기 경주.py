def solution(players, callings):
    dicNo = {}
    dicNm = {}
    
    for idx,name in enumerate(players):
        dicNo[idx] = name
        dicNm[name] = idx
    
    for fast in callings:
        nowNo = dicNm[fast]
        pre = dicNo[nowNo-1]
        
        dicNm[fast] = nowNo-1
        dicNm[pre] = nowNo
        dicNo[nowNo] = pre
        dicNo[nowNo-1] = fast
    
    return list(dicNo.values())

# 1. players를 딕셔너리에 넣어놓고 callings 하나씩 보고 수정?
#    - 등수, 이름 둘 중 어느게 키가 되더라도 값으로 키를 한번은 찾게되는게 번거롭다.

# 2. 각player 이름에 등수를 붙인 튜플을 셋에 넣는다...? : {(1,"mumu"),(2,"soe")...}
#    - 등수까지 아는게 아니면 해당 원소를 찾아 제거할수 없음(셋의 원소는 수정이 안됨)

# 3. callings 하나씩 돌면서 players를 해당 선수앞까지 pop하고 순서 바꿔서 다시 append(스택)

# 4. callings 하나씩 돌면서 players에서 해당 이름의 인덱스 찾아 앞 인덱스와 교체

# 5. 1.딕셔너리 이용해보기: 딕셔너리를 두개 만들면?(등수가 키값인것과 이름이 키값인것)