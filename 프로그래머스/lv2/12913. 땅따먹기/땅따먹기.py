def solution(land):
    before = land[0]
    floor = 1
    answer = 0
    
    while floor<len(land):
        land[floor][0] += max(before[1], before[2], before[3])
        land[floor][1] += max(before[0], before[2], before[3])
        land[floor][2] += max(before[1], before[0], before[3])
        land[floor][3] += max(before[1], before[2], before[0])
        
        if floor == len(land)-1:
            answer =  max(land[floor])
        before = land[floor]
        floor = floor + 1
    
    return answer
    