def solution(ingredient):
    stack = []
    result = 0
    
    for ing in ingredient:
        stack.append(ing)
        if len(stack)>3:
            if stack[-1] == 1:
                if stack[-2] == 3:
                    if stack[-3] == 2:
                        if stack[-4] == 1:
                            result = result + 1
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            stack.pop()
    
    return result

# 스택 사용
# ingredient 원소들을 하나씩 스택에 push
#   - 위에서부터 차례로 1,3,2,1인지 확인
#       - 맞으면 result + 1, 네개 모두 pop
