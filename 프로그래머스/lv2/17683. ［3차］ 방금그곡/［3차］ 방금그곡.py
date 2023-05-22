def solution(m, musicinfos):
    temp = {}
    mChange = changeSharp(m)
    
    for music in musicinfos:
        [start,end,title,info] = music.split(",")
        [startH, startM] = map(int,start.split(":"))
        [endH, endM] = map(int,end.split(":"))
        playTime = 0
        infoChange = changeSharp(info)
        infoLen = len(infoChange)
        count = 0
        totalTemp = ""
        
        if endM < startM:
            playTime = (60 - startM) + endM + (endH-startH-1)*60
        else:
            playTime = endM - startM + (endH-startH)*60

        if playTime < infoLen:
            totalTemp = ("").join(infoChange[:playTime])
        else:
            while playTime > 0:
                if count >= infoLen:
                    count = count - infoLen
                else:
                    totalTemp = totalTemp + infoChange[count]
                    count = count + 1
                    playTime = playTime - 1
        
        if mChange in totalTemp:
            if len(totalTemp) in temp:
                continue
            else:
                temp[len(totalTemp)] = title

    if len(temp) == 0:
        return "(None)"
    else:
        return temp[max(temp.keys())]

def changeSharp(getString):
    infos = {"C":"Z", "D":"Y", "F":"X", "G":"W", "A":"V", "E":"U"}
    temp = ""
    
    if "#" in getString:
        templist = getString.split("#")
        for partm in templist[:-1]:
            partm = partm[:-1] + infos[partm[-1]]
            temp = temp + partm
        temp = temp+templist[-1]
        return temp
    
    return getString

    
    
# 각 곡의 시작과 끝, 악보를 이용해 총 멜로디를 구하고 m이 들어있는지 확인
# 조건을 만족하면 temp 딕셔너리에 재생시간:곡제목 으로 저장
# temp 길이가 0이면 (None)리턴, 아니면 가장 큰 키의 값 리턴

# 총 멜로디 구하기
# 1. 재생시간을 구한다
# 2. totalTemp 변수에 악보 음 하나씩 재생시간동안 추가

# '#'붙은 음 교체
# '#'으로 split 후 각 끝문자를 V,W,X,Y,Z 중 하나로 교체
