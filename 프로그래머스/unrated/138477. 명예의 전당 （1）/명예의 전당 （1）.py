def solution(k, score):
    answer = []
    temp = []
    
    for i in range(len(score)):
        if i < k:
            temp.append(score[i])
            temp.sort(reverse=True)
        else:
            if score[i] > temp[-1]:
                temp.pop()
                temp.append(score[i])
                temp.sort(reverse=True)
            
        answer.append(temp[-1])
    
    return answer

#k번째까지는 가장 작은 수
#k번째 이후-> 그 전 회차 명예의 전당에서 가장 작은 수와 새 점수 비교
#               - 새 점수가 더 클 경우 명예의 전당에서 두번째 작은 수
#               - 새 점수가 더 작을 경우 원래 수 그대로