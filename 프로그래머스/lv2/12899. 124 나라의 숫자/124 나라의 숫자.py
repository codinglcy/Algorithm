from collections import deque

def solution(n):
    answer = ''
    dic = {0:"1", 1:"2", 2:"4"}
    temp = deque()
    n = n-1
    
    while n > -1:
        if n == 0:
            temp.appendleft(n)
            break

        else:
            temp.appendleft(n%3)
            n = n // 3 -1
    
    for i in temp:
        answer = answer + dic[i]
    
    return answer

# 자릿수 - 3의 제곱수 누적
#   (3의 1제곱(3)까지: 한자리 / 3의 1제곱(3) + 3의 2제곱(9)까지(4~12): 두자리)
# 첫째자리 - 3으로 나눠떨어지는 경우 4, 나머지가 1이면 1, 나머지가 2면 2
# 둘째자리 - 3으로 나눈 몫을 다시 3으로 나눈 나머지로 첫째자리처럼
# 셋째자리 - 3으로 나눈 몫을 다시 3으로 나눈 몫의 3으로 나눈 나머지로 첫째자리처럼
# ...