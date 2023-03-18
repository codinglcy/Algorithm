def solution(arr):
    answer = []

    for n in arr:
        if len(answer) == 0:
            answer.append(n)
        elif answer[-1] == n:
            continue
        else:
            answer.append(n)
    
    return answer