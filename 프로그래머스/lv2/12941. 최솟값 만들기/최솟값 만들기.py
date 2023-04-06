def solution(A,B):
    answer = []
    temp = 0
    sortA = sorted(A)
    sortB = sorted(B)
    
    for i in range(len(A)):
        temp = temp + (sortA[i] * sortB[(-1)*i - 1])
    answer.append(temp)
    
    for i in range(len(A)):
        temp = temp + (sortB[i] * sortA[(-1)*i - 1])
    answer.append(temp)
    
    return min(answer)

# 가장큰수*가장작은수로 차례대로하는것이 가장 작아진다
# A에서 가장작은수를 고르는 경우 & B에서 가장작은수를 고르는 경우