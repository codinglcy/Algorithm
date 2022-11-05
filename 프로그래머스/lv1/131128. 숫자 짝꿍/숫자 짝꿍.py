def solution(X, Y):
    answer = -1
    temp = []
    Xdic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    Ydic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
    
    for x in X:
        Xdic[x] = Xdic[x]+1
    for y in Y:
        Ydic[y] = Ydic[y]+1
    
    for n in range(9,-1,-1):
        n = str(n)
        if Xdic[n] and Ydic[n]:
            count = min(Xdic[n], Ydic[n])
            for cnt in range(count):
                temp.append(n)
    
    if not temp:
        answer = '-1'
    elif temp.count('0')==len(temp):
        answer = '0'
    else:
        for tempnum in temp:
            if answer==-1:
                answer = tempnum
            else:
                answer += tempnum
    
    return answer