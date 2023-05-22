def solution(msg):
    dic = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    number = 27
    answer = []

    while len(msg) > 0:
        if len(msg) == 1:
            answer.append(dic[msg])
            break
        
        cIdx = 1
        w = msg[0]
        c = msg[1]
        while w+c in dic:
            cIdx = cIdx + 1
            if cIdx == len(msg):
                answer.append(dic[msg])
                return answer
            else: 
                w = w + c
                c = msg[cIdx]
                
        answer.append(dic[w])
        dic[w+c] = number
        number = number + 1
        msg = msg[cIdx:]
    
    return answer

# while문 msg의 길이가 0보다 클 동안
#   while문 w+c가 dic에 없을때까지 w길이를 늘린다
#       w길이가 최대가 되었을때
#       answer.append(dic[w])
#       dic[w+c] = number
#       number = number+1
#   msg = msg[cIdx:]