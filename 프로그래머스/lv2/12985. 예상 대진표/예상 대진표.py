import math

def solution(n,a,b):
    totalRound = int(math.log2(n))

    while n > 1:
        if a <= n//2 and b <= n//2:
            n = n // 2
            totalRound = totalRound - 1
            continue
            
        if a <= n//2 or b <= n//2:
            return totalRound
            
        else:
            a = a - n//2
            b = b - n//2
            n = n // 2
            totalRound = totalRound - 1
    

# 1 2 / 3 4 / 5 6 / 7 8
#  1     4  /  5    7
#     4          7
#           4

# 반으로 나눴을 때 다른 쪽에 있으면 결승에서 보게 된다=> (지수)리턴 : 2의2승일때 2번째 라운드가 결승이다. 
# 반으로 나눴을 때 같은 쪽에 있으면 또 반으로 나눠서 같은 쪽에 있는지 확인