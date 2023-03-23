def solution(n):
    temp = [3, 11]
    
    if n % 2 == 1:
        return 0
    if n == 2:
        return temp[0]
    if n == 4:
        return temp[1]
    
    for i in range(2,n//2):
        temp.append((temp[i-1]*4 - temp[i-2])%1000000007)
    
    
    return temp[-1]