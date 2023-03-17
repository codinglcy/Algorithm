def solution(arr):
    result = 0
    
    for n in arr:
        result = result + n
    
    return result/len(arr)