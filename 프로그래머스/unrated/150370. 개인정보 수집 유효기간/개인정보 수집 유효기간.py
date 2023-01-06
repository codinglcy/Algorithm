def solution(today, terms, privacies):
    answer = []
    termDic = {}
    temp = []
    
    today = int("".join(today.split('.')))
    
    for term in terms:
        term = term.split(' ')
        termDic[term[0]] = term[1]
    
    
    for privacy in privacies:
        privacy = privacy.split(' ')
        privacyDate = privacy[0].split('.')
        
        plusyear = 0
        plusmonth = int(termDic[privacy[1]])
        if plusmonth >= 12:
            plusyear = plusmonth//12
            plusmonth = plusmonth%12
            
        if int(privacyDate[1]) + plusmonth > 12:
            plusyear = plusyear + 1
            privacyDate[1] = str(int(privacyDate[1]) + plusmonth - 12)
        else:
            privacyDate[1] = str(int(privacyDate[1]) + plusmonth)
            
        if int(privacyDate[1]) < 10:
            privacyDate[1] = '0' + privacyDate[1]
        
        privacyDate[0] = str(int(privacyDate[0]) + plusyear)
        temp.append(int(''.join(privacyDate)))
    
    for i in range(len(temp)):
        if today >= temp[i]:
            answer.append(i+1)
    
    return answer