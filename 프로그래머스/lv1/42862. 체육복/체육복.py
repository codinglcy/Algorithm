def solution(n, lost, reserve):
    answer = n
    
    lostDel = set(lost) - set(reserve)
    resDel = set(reserve) - set(lost)
    
    lostDel = sorted(list(lostDel))
    
    for n in lostDel:
        if n-1 in resDel:
            answer = answer + 1
            resDel.remove(n-1)
        elif n+1 in resDel:
            answer = answer + 1
            resDel.remove(n+1)
    
    return answer - len(lostDel)

# 총인원 n에서 lost의 길이를 뺀다. -> answer에 저장
# lost로 for문 실행
#   각 원소의 -1 이나 +1에 해당하는 숫자가 reserve에 있으면
#       answer에 +1
#       reserve에서 해당 숫자 삭제