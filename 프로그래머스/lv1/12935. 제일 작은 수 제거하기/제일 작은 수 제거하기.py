def solution(arr):
    minarr = min(arr)
    answer = []
    
    if len(arr) == 1:
        return [-1]
    
    for n in arr:
        if not n == minarr:
            answer.append(n)
    
    return answer