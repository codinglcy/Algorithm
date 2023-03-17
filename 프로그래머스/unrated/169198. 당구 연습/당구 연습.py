import math

def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX, startY]
    
    def dotsLen(start, goal):
        xLen = abs(start[0] - goal[0])
        yLen = abs(start[1] - goal[1])
        result = (xLen*xLen) + (yLen*yLen)
        return result
    
    for goal in balls:
        temp = math.inf
        if not (startX==goal[0] and startY<goal[1]):
            #위쪽 벽에 부딪힐 경우
            goalX_U = goal[0]
            goalY_U = n + (n-goal[1])
            dotsLen_U = dotsLen(start, [goalX_U, goalY_U])
            if temp > dotsLen_U:
                temp = dotsLen_U
        
        if not (startY==goal[1] and startX>goal[0]):
            #왼쪽 벽에 부딪힐 경우
            goalX_L = goal[0] * (-1)
            goalY_L = goal[1]
            dotsLen_L = dotsLen(start, [goalX_L, goalY_L])
            if temp > dotsLen_L:
                temp = dotsLen_L
        
        if not (startY==goal[1] and startX<goal[0]):
            #오른쪽 벽에 부딪힐 경우
            goalX_R = m + (m-goal[0])
            goalY_R = goal[1]
            dotsLen_R = dotsLen(start, [goalX_R, goalY_R])
            if temp > dotsLen_R:
                temp = dotsLen_R
        
        if not (startX==goal[0] and startY>goal[1]):
            #아래쪽 벽에 부딪힐 경우
            goalX_D = goal[0]
            goalY_D = goal[1] * (-1)
            dotsLen_D = dotsLen(start, [goalX_D, goalY_D])
            if temp > dotsLen_D:
                temp = dotsLen_D
        
        #꼭짓점에 부딪혀도 목표로 갈 수 있다면1
        goalIf1 = startX==startY and goal[0]==goal[1]
        if m==n and goalIf1:
            if startX<goal[0]:
                #꼭짓점에 부딪힐 경우(왼쪽아래)
                startX_LD = startX * (-1)
                startY_LD = startY * (-1)
                dotsLen_LD = dotsLen([startX_LD, startY_LD], goal)
                if temp > dotsLen_LD:
                    temp = dotsLen_LD

            if startX>goal[0]:
                #꼭짓점에 부딪힐 경우(오른쪽위)
                startX_RU = m + (m-startX)
                startY_RU = n + (n-startY)
                dotsLen_RU = dotsLen([startX_RU, startY_RU], goal)
                if temp > dotsLen_RU:
                    temp = dotsLen_RU
        
        #꼭짓점에 부딪혀도 목표로 갈 수 있다면2
        goalIf2 = startX+startY==m and goal[0]+goal[1]==m
        if m==n and goalIf2:
            if startX<goal[0]:
                #꼭짓점에 부딪힐 경우(왼쪽위)
                startX_LU = startX * (-1)
                startY_LU = n + (n-startY)
                dotsLen_LU = dotsLen([startX_LU, startY_LU], goal)
                if temp > dotsLen_LU:
                    temp = dotsLen_LU
            
            if startX>goal[0]:
                #꼭짓점에 부딪힐 경우(오른쪽아래)
                startX_RD = m + (m-startX)
                startY_RD = startY * (-1)
                dotsLen_RD = dotsLen([startX_RD, startY_RD], goal)
                if temp > dotsLen_RD:
                    temp = dotsLen_RD
                
        answer.append(temp)
    
    return answer

# 고려할 경우
#   1. 상하좌우 벽에 부딪힐 경우
#       - 각 벽으로 향하는 중 목표가 있으면 안된다.
#   2. 꼭짓점에 부딪힐 경우
#       - m과 n이 같고
#       - 칠 공의 x값과 y값이 같을때 목표공도 x값과 y값이 같거나
#       - 칠 공의 x+y값이 m과 같을때 목표공도 x+y값이 m과 같아야 함
#       - 각 꼭짓점으로 향하는 중 목표가 있으면 안된다.

# 필요한 개념
# - 원래 생각했던 방법: 복잡하고 오차가 생기기 쉽다.
# - 부딪힐 벽에 목표점을 대칭시켜 해당 위치와 칠 공 위치의 최소길이를 구한다.

# 각 경우마다 나오는 거리를 temp와 비교
#   - temp보다 작을 시 해당 거리를 temp에 저장 
