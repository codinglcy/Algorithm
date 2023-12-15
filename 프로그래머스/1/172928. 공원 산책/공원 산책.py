def solution(park, routes):
    answer = []
    XX = set()
    
    #S,X의 위치좌표
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                answer.append(i)
                answer.append(j)
            elif park[i][j] == 'X':
                XX.add((i,j))
    
    #명령수행 전 확인
    def check(now, op, n):
        H = now[0]
        W = now[1]
        
        for i in range(1,n+1):
            if op == 'N':
                H = H-1
            elif op == 'S':
                H = H+1
            elif op == 'W':
                W = W-1
            elif op == 'E':
                W = W+1
            
            if H >= len(park) or W >= len(park[0]) or H < 0 or W < 0:
                return now
            
            go = (H,W)
            if go in XX:
                return now
        
        return [H,W]
    
    
    for i in range(len(routes)):
        #방향=op,이동거리=n
        [op, n] = routes[i].split(" ")
        n = int(n)
        
        answer = check(answer, op, n)
    
    return answer

