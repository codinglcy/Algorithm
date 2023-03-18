def solution(s):
    answer = True
    pCount = 0
    yCount = 0
    setS = set(s.lower())
    
    if 'p' not in setS and 'y' not in setS:
        return True
    elif 'p' not in setS or 'y' not in setS:
        return False
    
    for c in s.lower():
        if c == 'p':
            pCount = pCount + 1
        elif c == 'y':
            yCount = yCount + 1

    return pCount == yCount