def solution(s):
    sList = []
    i = 0
    
    while i<len(s):
        if s[i]>='0' and s[i]<='9':
            sList.append(s[i])
            i = i + 1
        else:
            if s[i]=='z':
                sList.append('0')
                i = i + 4
            elif s[i]=='o':
                sList.append('1')
                i = i + 3
            elif s[i]=='t':
                if s[i+1]=='w':
                    sList.append('2')
                    i = i + 3
                else:
                    sList.append('3')
                    i = i + 5
            elif s[i]=='f':
                if s[i+1]=='o':
                    sList.append('4')
                    i = i + 4
                else:
                    sList.append('5')
                    i = i + 4
            elif s[i]=='s':
                if s[i+1]=='i':
                    sList.append('6')
                    i = i + 3
                else:
                    sList.append('7')
                    i = i + 5
            elif s[i]=='e':
                sList.append('8')
                i = i + 5
            elif s[i]=='n':
                sList.append('9')
                i = i + 4
    result = ''.join(sList)
    return int(result)
                
                
                
                