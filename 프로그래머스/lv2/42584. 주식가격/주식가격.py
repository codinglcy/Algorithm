def solution(prices):
    answer = [0]*len(prices)
    stack = [(prices[0],0)]
    
    for i in range(1, len(prices)):
        if len(stack) > 0 and stack[-1][0] > prices[i]:
            while len(stack) > 0 and stack[-1][0] > prices[i]:
                (tempV, tempIdx) = stack.pop()
                answer[tempIdx] = i - tempIdx
                    
        if i == len(prices)-1:
            while len(stack) > 0:
                (tempV, tempIdx) = stack.pop()
                answer[tempIdx] = i - tempIdx
                
        stack.append((prices[i],i))

    return answer

# 하나씩 stack에 넣기 (값,인덱스)
# stack의 마지막 요소의 값이 price[i]보다 크면:
#   stack의 마지막 요소의 값이 price[i]과 같거나 작아질때까지
#       (tempV, tempIdx) = stack.pop()
#       answer[tempIdx] = i - tempIdx
#   (price[i],i) stack에 추가
#