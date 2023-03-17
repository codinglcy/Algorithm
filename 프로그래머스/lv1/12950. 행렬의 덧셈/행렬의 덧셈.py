def solution(arr1, arr2):
    answer = []
    
    for idx in range(len(arr1)):
        mini = []
        for i in range(len(arr1[idx])):
            mini.append(arr1[idx][i] + arr2[idx][i])
        answer.append(mini)
    
    return answer