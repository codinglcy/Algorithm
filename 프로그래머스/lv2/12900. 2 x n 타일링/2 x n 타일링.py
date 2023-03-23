from collections import deque

def solution(n):

    temp = deque([1,2])
    if n == 1:
        return temp[0]
    if n == 2:
        return temp[1]
    
    for i in range(2, n):
        temp.append((temp[i-1] + temp[i-2])%1000000007)
    
    return temp[-1]
