def solution(n, t, m, p):
    answer = ''
    total = ''
    
    for i in range(m*t):
        if i == 0:
            total = total + '0'
        else:
            tempNum = changeNum(i, n)
            total = total + tempNum
    
    for j in range(p-1,len(total),m):
        answer = answer + total[j]
        
        if len(answer) == t:
            break
    
    return answer

def changeNum(num, n):
    dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    result = ''
    q = num
    
    while q > 0:
        q,r = divmod(q, n)
        result = result + dic[r]
    
    return result[::-1]

# 0에서 t-1까지의 수들을 n진법으로 변환해 하나의 문자열로 나열한다.
# m으로 나눈 나머지가 p인 번째의 문자가 튜브가 말해야 하는 것 -> answer에 하나씩 추가