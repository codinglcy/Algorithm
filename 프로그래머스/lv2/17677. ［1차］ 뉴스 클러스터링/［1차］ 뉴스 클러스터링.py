import math

def solution(str1, str2):
    groupA = []
    groupB = []
    groupPlus = [] #합집합
    groupSame = [] #교집합
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            groupA.append(str1[i].lower()+str1[i+1].lower())
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            groupB.append(str2[j].lower()+str2[j+1].lower())
    
    Copy_groupA = groupA
    for s in groupB:
        if s in Copy_groupA:
            Copy_groupA.remove(s)
            groupSame.append(s)
            
    groupPlus = groupA + groupB
    
    if len(groupSame) == 0 and len(groupPlus) == 0:
        return 1*65536
    
    return math.floor(len(groupSame)/len(groupPlus)*65536)
    