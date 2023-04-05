def solution(begin, end):
    answer = [0]
    maxNum = min(10000000,end//2)
    
    for i in range(begin,end+1):
        if i == 1:
            answer.append(0)
        elif i < 4:
            answer.append(1)
        else:
            temp1 = []
            temp2 = []
            for j in range(2, int(i**(1/2))+1):
                if i%j == 0:
                    if j <= maxNum:
                        temp1.append(j)
                    if i//j <= maxNum:
                        temp2.append(i//j)
            if temp2:
                temp = temp2[0]
            else:
                if temp1:
                    temp = temp1[-1]
                else:
                    temp = 1
            answer.append(temp)
                
    
    answer.pop(0)
    return answer

# 나타낼 수 있는 가장 큰 수: end//2
# 리스트의 인덱스는 0부터 시작하므로 계산을 편하게 하기 위해 인덱스0에 0을 넣어둔 후 답을 리턴할때 뺀다.