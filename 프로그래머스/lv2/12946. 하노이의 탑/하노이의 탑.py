def solution(n):
    answer = []
    
    def mini(num, start, go, result):
        if num == 1:
            result.append([start, go])
        else:
            mini(num-1, start, 6-start-go, result)
            result.append([start, go])
            mini(num-1, 6-start-go, go, result)
        return result
            
    
    return mini(n, 1, 3, answer)

#4:25
# 1: [[1,3]]
# 2: [[1,2],[1,3],[2,3]]
# 3: [[1,3],[1,2],[3,2],[1,3],[2,1],[2,3],[1,3]]
#
# n개를 3번에 옮기는 방법
#   n-1개를 2번으로 옮긴다 
#   3번에 가장 큰걸 옮긴다
#   n-1개를 3번으로 옮긴다
#        ...
