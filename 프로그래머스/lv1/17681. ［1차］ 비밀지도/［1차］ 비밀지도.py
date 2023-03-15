def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        temp = str(bin(arr1[i]|arr2[i])[2:])
        res = ''
        
        if len(temp) < int(n):
            for j in range(int(n) - len(temp)):
                temp = '0' + temp

        for k in temp:
            if k == '1':
                res = res + '#'
            else:
                res = res + ' '
        answer.append(res)
        
    return answer