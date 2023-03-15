def solution(dartResult):
    answer = dartResult[0]
    dic = {'S':' **1 ', 'D':' **2 ', 'T':' **3 ', '#':' * (-1) '}
    
    for i in range(1,len(dartResult)):
        c = dartResult[i]
        if c.isdecimal():
            if len(dartResult)-2 > i:
                if dartResult[i+2] == '*':
                    answer = answer + ' *2 '

            if c == '0':
                if dartResult[i-1] == '1':
                    answer = answer + c
                else:
                    answer = answer + ' + ' + c
            else:
                answer = answer + ' + ' + c
        else:
            if c == '*':
                answer = answer + ' *2'
            else:
                answer = answer + dic[c]
    
    return eval(answer)