def solution(n):
    temp = []
    
    while len(temp) < n:
        if len(temp)+1 == 1:
            temp.append(1)
        elif len(temp)+1 == 2:
            temp.append(2)
        else:
            temp.append((temp[-1]+temp[-2])%1234567)
        
    return temp[-1]