def solution(left, right):
    result = 0
    countDiv = 0
    nn = []
    for n in range(1,32):
        nn.append(n*n)
    
    for num in range(left,right+1):
        if num not in nn:
            result = result + num
        else:
            result = result - num
    
    return result