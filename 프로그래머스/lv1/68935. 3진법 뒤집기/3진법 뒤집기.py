def solution(n):
    temp = []
    
    while n>0:
        (n, mod) = divmod(n,3)
        temp.append(str(mod))
    
    answer = int(''.join(temp), 3)
    return answer

# 진법변환(10->n) - divmod(숫자, 진법) -> (몫, 나머지) => 몫이 0이 될때까지
# 진법변환(n->10) - int(string, 진법)