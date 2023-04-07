def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr2[0])):
            num = 0
            for k in range(len(arr2)):
                num = num + arr1[i][k]*arr2[k][j]
            temp.append(num)
        answer.append(temp)
    
    return answer

# 1 4      3 3
# 3 2      3 3
# 4 1
#
# 1*3+4*3 1*3+4*3
# 3*3+2*3 3*3+2*3
# 4*3+1*3 4*3+1*3
# 
#
# 2 3 2        5 4 3
# 4 2 4        2 4 1
# 3 1 4        3 1 1
#
# 2*5+3*2+2*3 2*4+3*4+2*1 2*3+3*1+2*1
# 4*5+2*2+4*3 4*4+2*4+4*1 4*3+2*1+4*1
# 3*5+1*2+4*3 3*4+1*4+4*1 3*3+1*1+4*1
