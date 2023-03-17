def solution(x):
    xplus = 0
    
    for n in str(x):
        xplus = xplus + int(n)
    
    return x%xplus == 0