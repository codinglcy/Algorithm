def solution(s):
    temp = []
    
    for c in s:
        if len(temp) == 0:
            temp.append(c)
        else:
            if c == temp[-1]:
                temp.pop()
            else:
                temp.append(c)

    if len(temp) == 0:
        return 1
    return 0

# 스택 사용
# 차례로 스택에 넣다가 스택의 제일 위 문자와 넣을 문자가 동일하면
#   스택에 있는 문자를 빼낸다.
#   아니면 스택에 쌓는다.
# 반복문을 다 돌고 나서 스택에 숫자가 남아있으면 0, 아니면 1 리턴