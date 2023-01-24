def solution(k, m, score):
    answer = 0
    temp = []
    
    score.sort(reverse=True)

    for i in range(0, len(score), m):
        temp.append(score[i:i+m])
    
    if len(temp[-1]) != m:
        temp.pop()
    
    for box in temp:
        answer = answer + box[-1] * m
    
    return answer

# score sort 한 뒤 큰것부터 m개씩 묶음
# 각 묶음의 가장 작은 점수 p
# p*m = 각 묶음의 이익