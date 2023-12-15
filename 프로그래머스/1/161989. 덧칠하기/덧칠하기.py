def solution(n, m, section):
    answer = 0
    count = 0
    sect = set(section)
    
    for i in range(1,n+1):
        if i in sect:
            if count == 0:
                count = m-1
                answer = answer+1
            else:
                count = count - 1
        else:
            if count > 0:
                count = count - 1
            continue

    return answer

# n - 전체 길이
# m - 롤러 길이
# section - 칠해야하는 칸 리스트 (오름차순 정렬)

# section 리스트중 최댓값과 최솟값의 차가 m 미만일때, result는 1

# 재귀

# 2023.12.15
# i 1에서 n까지 for문
#   section에 i 없으면 continue
#        페인트칠하는중(count가 0이 아님)이면 count-1하고 continue
#   section에 i 있으면
#        페인트칠하는중(count가 0이 아님)이면 count-1
#        페인트칠하는중이 아니면(count 0) count=m-1, answer=answer+1