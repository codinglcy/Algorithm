from collections import deque

def solution(maps):
    n = len(maps)-1
    m = len(maps[0])-1
    
    if maps[n][m-1]==0 and maps[n-1][m]==0 and maps[n-1][m-1]==0:
        return -1
    
    def playing(i, j, count, maps, n, m):
        q = deque()
        q.append((i,j,count))
        
        while q:
            i, j, count = q.popleft()
            
            if i==n and j==m:
                return count
            
            if i<0 or j<0 or i>n or j>m:
                continue
            
            if not maps[i][j] == 1:
                continue
                
            maps[i][j] = count
            
            
            if i+1 <= n:
                q.append((i+1, j, count+1))
            if j+1 <= m:
                q.append((i, j+1, count+1))
            if i-1 >= 0:
                q.append((i-1, j, count+1))
            if j-1 >= 0:
                q.append((i, j-1, count+1))
        return -1
    
    return playing(0, 0, 1, maps, n, m)

# 가장 빠르게 상대 진영에 도달하는 방법 <(i,j)에 위치할 경우>
# - 아래 칸(i+1,j)이나 오른쪽(i,j+1) 칸에 길이 있다면 무조건 그곳으로
#   - 만약 둘 다 길이 있다면 해당 칸 저장 후 아래로 간 경우와 오른쪽으로 간 경우 비교
# - 위 경우가 모두 벽이라면 위쪽 칸(i-1,j)으로
# - 왼쪽만 길이 있다면 왼쪽(i,j-1)으로

# 이동 전에 상대팀 진영이 벽으로 막혀있는지 확인 (n,m-1)(n-1,m)(n-1,m-1)

# 1인 곳은 무조건 간다
#   - 1대신 해당 칸 누적 숫자 저장
#   - dic을 이용해 상하좌우에 1이 있는 곳 탐색
#   - 1이 있는 곳에 가서 또 반복
# 1보다 큰 곳은 그냥 둔다

