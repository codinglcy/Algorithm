def solution(bandage, health, attacks):
    dic = {}
    fullHealCnt = bandage[0]
    heal = bandage[1]
    bonus = bandage[2]
    nowHp = health
    healCnt = 0
    
    for [time,amount] in attacks:
        dic[time] = amount
    
    for sec in range(1,attacks[-1][0]+1):
        if sec in dic:
            healCnt = 0
            nowHp = nowHp - dic[sec]
            
            if nowHp <= 0:
                return -1
        else:
            if nowHp < health:
                healCnt = healCnt + 1
                nowHp = min(nowHp+heal, health)
                if healCnt == fullHealCnt:
                    healCnt = 0
                    nowHp = min(nowHp+bonus, health)
    return nowHp


# 공격시간-키 피해량-값의 딕셔너리 생성

# 마지막 공격의 공격시간까지 반복문 (attacks[-1][0])
# 몬스터가 공격하는 시간이면 
#   - 회복연속성공 = 0
#   - 체력 감소
#       - 체력이 0 이하면 return -1
# 공격하는 시간이 아니면
#   - 현재체력이 최대체력보다 작으면
#       - 회복연속성공(healCnt) = healCnt + 1
#       - 체력 회복 (최대체력과 비교 했을때 작은것)
#       - healCnt가 최대연속수면
#           - healCnt = 0
#           - 체력 보너스 (최대체력과 비교 했을때 작은것)