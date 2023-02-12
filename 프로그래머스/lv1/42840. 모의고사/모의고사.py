def solution(answers):
    answer = []
    corr = {1:0, 2:0, 3:0}
    
    for i in range(len(answers)):
        num = i + 1
        
        #1번학생
        if num % 5 == 0 and answers[i] == 5:
            corr[1] = corr[1] + 1
        elif num % 5 == answers[i]:
            corr[1] = corr[1] + 1
        
        #2번학생
        if num % 2 == 1 and answers[i] == 2:
            corr[2] = corr[2] + 1
        elif num % 8 == 2 and answers[i] == 1:
            corr[2] = corr[2] + 1
        elif num % 8 == 4 and answers[i] == 3:
            corr[2] = corr[2] + 1
        elif num % 8 == 6 and answers[i] == 4:
            corr[2] = corr[2] + 1
        elif num % 8 == 0 and answers[i] == 5:
            corr[2] = corr[2] + 1
        
        #3번학생
        if (num % 10 == 1 or num % 10 == 2) and answers[i] == 3:
            corr[3] = corr[3] + 1
        elif (num % 10 == 3 or num % 10 == 4) and answers[i] == 1:
            corr[3] = corr[3] + 1
        elif (num % 10 == 5 or num % 10 == 6) and answers[i] == 2:
            corr[3] = corr[3] + 1
        elif (num % 10 == 7 or num % 10 == 8) and answers[i] == 4:
            corr[3] = corr[3] + 1
        elif (num % 10 == 9 or num % 10 == 0) and answers[i] == 5:
            corr[3] = corr[3] + 1
        
    for i in corr:
        if corr[i] == max(corr.values()):
            answer.append(i)
    
    return answer

# 1번 수포자 : [1,2,3,4,5] 반복 (5개)
# 2번 수포자 : [[2,1],[2,3],[2,4],[2,5]] 반복 (8개)
# 3번 수포자 : [[3,3],[1,1],[2,2],[4,4],[5,5]] 반복 (10개)
#
# 1번 - n%5==1의 경우 답이 1이면 맞는 것, n%5==0의 경우 답이 5이면 맞는 것..
# 2번 - n%2==1의 경우 답이 2이면 맞는 것, n%8==2의 경우 답이 1이면 맞는 것..
# 3번 - n%10==1이나 2일 경우 답이 3이면 맞는 것, 3이나 4일 경우 답이 1이면 맞는 것..
#
# corr 딕셔너리에 각 학생이 맞힌 문제 수 세기