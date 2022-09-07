def solution(survey, choices):
    result = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    answer = ''
    
    for i in range(len(survey)):
        plusType = ''
        if choices[i]>4:
            plusType = survey[i][1]
            result[plusType] = result[plusType] + choices[i]-4
        elif choices[i]==4:
            continue
        else:
            plusType = survey[i][0]
            result[plusType] = result[plusType] + 4-choices[i]
    
    typeList = list(result.keys())
    
    for i in range(0,8,2):
        if result[typeList[i]]-result[typeList[i+1]]>0:
            answer = answer + typeList[i]
        elif result[typeList[i]]-result[typeList[i+1]]<0:
            answer = answer + typeList[i+1]
        else:
            if typeList[i]<typeList[i+1]:
                answer = answer + typeList[i]
            else:
                answer = answer + typeList[i+1]
    
    return answer