def solution(n, m):
    answer = []
    gcd = 0
    lcm = 0
    
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            gcd = i
            break
    lcm = n*m // gcd
    answer.append(gcd)
    answer.append(lcm)
    
    return answer

# math.gcd(n,m) -> 최대공약수
# math.lcm(n,m) -> 최소공배수