def solution(wallpaper):
    xSet = set()
    ySet = set()
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                xSet.add(i)
                ySet.add(j)

    answer = [min(xSet), min(ySet), max(xSet)+1, max(ySet)+1]
    return answer

    
# lux의 값은 '#'이 존재하는 위치들 중 가장 작은 x값
# luy의 값은 '#'이 존재하는 위치들 중 가장 작은 y값
# rdx의 값은 '#'이 존재하는 위치들 중 가장 큰 y값+1
# rdy의 값은 '#'이 존재하는 위치들 중 가장 큰 y값+1